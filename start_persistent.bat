@echo off
title LoanPulse System
echo ========================================================
echo   LoanPulse — Auto-Launcher & Self-Healing Service
echo ========================================================

:: Check Backend port 8000
netstat -ano | findstr "LISTENING" | findstr ":8000" >nul
if %errorlevel% neq 0 (
    echo [1/2] Starting Backend Server (port 8000)...
    start "LoanPulse Backend" /min cmd /c "cd /d C:\Users\ayush\.gemini\antigravity\scratch\loanpulse\backend && .\venv\Scripts\python manage.py runserver 0.0.0.0:8000"
) else (
    echo [1/2] Backend Server is already active on port 8000.
)

:: Check Frontend port 5173
netstat -ano | findstr "LISTENING" | findstr ":5173" >nul
if %errorlevel% neq 0 (
    echo [2/2] Starting Frontend Server (port 5173)...
    start "LoanPulse Frontend" /min cmd /c "cd /d C:\Users\ayush\.gemini\antigravity\scratch\loanpulse\frontend && npm run dev"
) else (
    echo [2/2] Frontend Server is already active on port 5173.
)

:: If not launched with /silent parameter, open browser
if "%1" neq "/silent" (
    timeout /t 3 /nobreak >nul
    echo.
    echo Opening LoanPulse in your default browser...
    start http://localhost:5173
)
