@echo off
REM Uploads this folder to Netlify WITH the save service, so the Admin Save works for everyone.
cd /d "%~dp0"
echo.
echo   Deploying Khalil Samour portfolio to Netlify
echo.
where npx >nul 2>nul
if errorlevel 1 (
  echo   Node.js is needed one time. Opening nodejs.org now.
  echo   Install the LTS version, then double-click this file again.
  start "" "https://nodejs.org/en/download"
  pause
  exit /b 1
)
echo   If a browser opens, log in to Netlify and click Authorize.
echo   If asked, choose "Link this directory to an existing site" and pick your site.
echo.
call npx --yes netlify-cli deploy --prod --dir . --functions netlify/functions
echo.
echo   Finished.
pause
