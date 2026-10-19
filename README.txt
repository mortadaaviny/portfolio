Khalil Samour portfolio

Everything is inside index.html: the website and the admin.
Open the admin from the "Admin" link in the footer, or add #admin to the address.

This zip has TWO ready-to-deploy options. Pick the one that matches where you
host the site. Since you're on Wasmer (khalilsammour.wasmer.app), use the
wasmer/ folder.

OPTION A - Wasmer (your current host)
  Use the wasmer/ folder. See wasmer/README-WASMER.txt for the exact steps.
  This is new and I could not fully test a real deploy myself (no Wasmer
  account/CLI here) - only the save logic itself, which I did verify. If
  "wasmer deploy" errors on wasmer.toml or app.yaml, send me the exact
  message and I'll fix it.

OPTION B - Netlify
  Use the files at the top level of this zip (index.html, netlify/, etc).
  Do not drag and drop this onto Netlify - Netlify does not run the save
  service for drag-and-drop uploads, so Save cannot reach visitors.

  DEPLOY (one time, about 3 minutes)
  1. Install Node.js (LTS) from https://nodejs.org if you do not have it.
  2. Unzip this folder.
  3. Mac: double-click "Deploy to Netlify (Mac).command"
          (if macOS blocks it: right-click it > Open > Open)
     Windows: double-click "Deploy to Netlify (Windows).bat"
  4. A browser opens: log in to Netlify and click Authorize.
  5. When asked, choose "Link this directory to an existing site" and pick your site
     (or "Create & configure a new site").
  6. When it finishes it prints your live address.

FIRST TIME IN THE ADMIN (either option)
  Open your live site, click Admin, and create your password right away.

EDITING (either option)
  Change anything, press Save. Every visitor sees it right away, on any device.
  You only need to deploy again when the site's design or code changes.

Files
  index.html, content.json, images/   website + starting content (both options use these)
  wasmer/                             Option A: deploy files for Wasmer
  netlify/, netlify.toml,             Option B: deploy files for Netlify
  Deploy to Netlify (...)
