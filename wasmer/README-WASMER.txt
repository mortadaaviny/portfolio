Khalil Samour portfolio — Wasmer deploy

Everything is inside index.html: the website and the admin.
Open the admin from the "Admin" link in the footer, or add #admin to the address.

This folder (wasmer/) is a separate, self-contained deploy: a small Python
script (src/main.py) that serves the website AND the save service together,
using only Python's standard library (nothing to install). Saved content is
written to the data/ volume, which Wasmer keeps across restarts and redeploys.

I could not test an actual deploy to Wasmer myself (no Wasmer account/CLI
here), only the Python script's own logic, which I ran and verified
end-to-end on my side: creating the admin password, saving content, and
restarting the server to confirm the save survives. If "wasmer deploy"
reports an error about wasmer.toml or app.yaml, send me the exact message
and I will fix it.

DEPLOY (one time)
  1. Install the Wasmer CLI from https://wasmer.io/products/cli if you don't have it.
  2. Unzip this folder, open a terminal in wasmer/ (or just double-click the deploy file).
  3. Mac: double-click "Deploy to Wasmer (Mac).command"
          (if macOS blocks it: right-click it > Open > Open)
     Windows: double-click "Deploy to Wasmer (Windows).bat"
  4. Log in to Wasmer when asked, then let "wasmer deploy" finish.
  5. It prints your live address (yours is khalilsammour.wasmer.app).

FIRST TIME IN THE ADMIN
  Open your live site, click Admin, and create your password right away.

EDITING
  Change anything, press Save. Every visitor sees it right away, on any device.
  You only need to deploy again when the site's design or code changes.

Files
  wasmer.toml, app.yaml     Wasmer app settings (volume for saved data, env vars)
  src/main.py               website + save service, pure Python standard library
  public/                   the website files (index.html, content.json, images)
  data/                     where saved content is stored (the persistent volume)
  Deploy to Wasmer (...)    the deploy files
