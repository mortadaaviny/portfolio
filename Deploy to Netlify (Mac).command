#!/bin/bash
# Uploads this folder to Netlify WITH the save service, so the Admin's Save works for everyone.
cd "$(dirname "$0")"
echo ""
echo "  Deploying Khalil Samour portfolio to Netlify"
echo "  ---------------------------------------------"
if ! command -v npx >/dev/null 2>&1; then
  echo ""
  echo "  Node.js is needed (one time). Opening nodejs.org now."
  echo "  Install the LTS version, then double-click this file again."
  open "https://nodejs.org/en/download"
  echo ""
  read -p "  Press Enter to close."
  exit 1
fi
echo ""
echo "  If a browser opens, log in to Netlify and click Authorize."
echo "  If asked, choose 'Link this directory to an existing site' and pick your site."
echo ""
npx --yes netlify-cli deploy --prod --dir . --functions netlify/functions
echo ""
read -p "  Finished. Press Enter to close."
