#!/usr/bin/env python3
"""
Khalil Samour portfolio: static site + save API, in one process.
Standard library only (no pip install), so it runs on Wasmer's plain
Python template with no venv or dependency step.

GET  /api/content  -> {"content": <saved content or null>, "hasPassword": bool}
POST /api/content  -> {setup|password, check?, content?} -> create/verify password, save content
Anything else      -> served as a static file from ./public (index.html for unknown paths)
"""
import os, sys, json, time, hmac, hashlib, binascii, secrets
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

BASE = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIR = os.environ.get("PUBLIC_DIR", os.path.join(os.path.dirname(BASE), "public"))
DATA_DIR = os.environ.get("DATA_DIR", os.path.join(os.path.dirname(BASE), "data"))
CONTENT_PATH = os.path.join(DATA_DIR, "content.json")
AUTH_PATH = os.path.join(DATA_DIR, "auth.json")
PBKDF2_ITERS = 200_000

MIME = {".html":"text/html; charset=utf-8", ".js":"application/javascript; charset=utf-8",
        ".css":"text/css; charset=utf-8", ".json":"application/json; charset=utf-8",
        ".jpg":"image/jpeg", ".jpeg":"image/jpeg", ".png":"image/png", ".svg":"image/svg+xml",
        ".txt":"text/plain; charset=utf-8", ".ico":"image/x-icon"}

def read_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    os.replace(tmp, path)

def hash_password(password, salt_hex=None):
    salt = bytes.fromhex(salt_hex) if salt_hex else secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, PBKDF2_ITERS)
    return binascii.hexlify(salt).decode(), binascii.hexlify(dk).decode()

def verify_password(password, salt_hex, hash_hex):
    _, dk_hex = hash_password(password, salt_hex)
    return hmac.compare_digest(dk_hex, hash_hex)

class Handler(BaseHTTPRequestHandler):
    server_version = "PortfolioAPI/1.0"
    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _json(self, status, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _static(self, path):
        if path == "/" or path == "":
            path = "/index.html"
        safe = os.path.normpath(path).lstrip("/\\")
        full = os.path.join(PUBLIC_DIR, safe)
        if not os.path.abspath(full).startswith(os.path.abspath(PUBLIC_DIR)) or not os.path.isfile(full):
            full = os.path.join(PUBLIC_DIR, "index.html")
        ext = os.path.splitext(full)[1].lower()
        try:
            with open(full, "rb") as f:
                body = f.read()
        except Exception:
            self._json(404, {"error": "Not found."}); return
        self.send_response(200)
        self.send_header("Content-Type", MIME.get(ext, "application/octet-stream"))
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        p = urlparse(self.path).path
        if p == "/api/content":
            content = read_json(CONTENT_PATH)
            auth = read_json(AUTH_PATH)
            self._json(200, {"content": content, "hasPassword": bool(auth)})
        else:
            self._static(p)

    def do_POST(self):
        p = urlparse(self.path).path
        if p != "/api/content":
            self._json(405, {"error": "Method not allowed."}); return
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length) or b"{}")
        except Exception:
            self._json(400, {"error": "Bad request."}); return

        password = str(body.get("password") or "")
        auth = read_json(AUTH_PATH)

        if not auth:
            if not body.get("setup") or len(password) < 6:
                self._json(400, {"error": "Create a password of at least 6 characters."}); return
            salt_hex, hash_hex = hash_password(password)
            write_json(AUTH_PATH, {"salt": salt_hex, "hash": hash_hex})
        else:
            if not verify_password(password, auth["salt"], auth["hash"]):
                time.sleep(0.8)
                self._json(401, {"error": "Wrong password."}); return

        if body.get("check"):
            self._json(200, {"ok": True}); return

        content = body.get("content")
        if not isinstance(content, dict) or not isinstance(content.get("projects"), list) or not content.get("text"):
            self._json(400, {"error": "Invalid content."}); return
        content["updated"] = int(time.time() * 1000)
        write_json(CONTENT_PATH, content)
        self._json(200, {"ok": True, "updated": content["updated"]})

if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8000"))
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    print("Serving %s and /api/content on %s:%s" % (PUBLIC_DIR, host, port))
    ThreadingHTTPServer((host, port), Handler).serve_forever()
