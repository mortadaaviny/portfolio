Khalil Samour portfolio

Everything is inside index.html: the website and the admin.
Open the admin from the "Admin" link in the footer, or add #admin to the address.

IMPORTANT
  Do not drag and drop this folder onto Netlify. Netlify does not run the save
  service for drag-and-drop uploads, so Save cannot reach visitors.
  Use the Deploy file below instead. Your saved content is kept across deploys.

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

FIRST TIME IN THE ADMIN
  Open your live site, click Admin, and create your password right away.

EDITING
  Change anything, press Save. Every visitor sees it right away, on any device.
  You only need to deploy again when the site's design or code changes.

Files
  index.html                      website and admin
  content.json, images/           starting content
  netlify/functions/content.mjs   the save service (stores content in Netlify)
  netlify.toml                    settings
  Deploy to Netlify (...)         the deploy files
