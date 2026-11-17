@echo off
title Stop LoanPulse
echo ========================================================
echo   Stopping LoanPulse Servers
echo ========================================================

for /f "tokens=5" %%a in ('netstat -ano ^| findstr "LISTENING" ^| findstr ":8000"') do (
    echo Terminating backend process PID %%a...
    taskkill /f /pid %%a 2>nul
)

for /f "tokens=5" %%a in ('netstat -ano ^| findstr "LISTENING" ^| findstr ":5173"') do (
    echo Terminating frontend process PID %%a...
    taskkill /f /pid %%a 2>nul
)

echo.
echo All LoanPulse servers stopped successfully.
timeout /t 3
