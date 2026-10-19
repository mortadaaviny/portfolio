@echo off
cd /d "%~dp0"
echo.
echo   Deploying Khalil Samour portfolio to Wasmer
echo   --------------------------------------------
where wasmer >nul 2>nul
if errorlevel 1 (
  echo.
  echo   The Wasmer CLI is needed ^(one time^). Opening wasmer.io now.
  echo   After installing, close this window and double-click this file again.
  start https://wasmer.io/products/cli
  echo.
  pause
  exit /b 1
)
echo.
echo   If a browser opens, log in to Wasmer and click Authorize.
echo   If asked to create the app, accept the defaults ^(they are already set in app.yaml^).
echo.
wasmer login
wasmer deploy
echo.
pause
