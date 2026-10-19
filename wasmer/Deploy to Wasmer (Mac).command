#!/bin/bash
# Deploys this folder to Wasmer Edge WITH the save service, so the Admin's Save works for everyone.
cd "$(dirname "$0")"
echo ""
echo "  Deploying Khalil Samour portfolio to Wasmer"
echo "  --------------------------------------------"
if ! command -v wasmer >/dev/null 2>&1; then
  echo ""
  echo "  The Wasmer CLI is needed (one time). Opening wasmer.io now."
  echo "  After installing, close this window and double-click this file again."
  open "https://wasmer.io/products/cli"
  echo ""
  read -p "  Press Enter to close."
  exit 1
fi
echo ""
echo "  If a browser opens, log in to Wasmer and click Authorize."
echo "  If asked to create the app, accept the defaults (they are already set in app.yaml)."
echo ""
wasmer login
wasmer deploy
echo ""
read -p "  Finished. Press Enter to close."
