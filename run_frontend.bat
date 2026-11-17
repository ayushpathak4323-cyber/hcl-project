@echo off
echo ========================================================
echo   Starting LoanPulse Frontend (React 19 + Vite)
echo ========================================================
cd /d "%~dp0frontend"

if not exist "node_modules" (
    echo node_modules not found. Installing frontend dependencies...
    call npm install
)

echo.
echo Launching Vite frontend on http://localhost:5173 ...
npm run dev
pause
