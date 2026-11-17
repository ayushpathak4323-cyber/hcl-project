@echo off
echo ========================================================
echo   Starting LoanPulse Full Stack System
echo ========================================================
start "LoanPulse Backend (Django ASGI)" cmd /k "%~dp0run_backend.bat"
start "LoanPulse Frontend (React 19 Vite)" cmd /k "%~dp0run_frontend.bat"
echo.
echo Both servers are launching in separate windows!
echo - Frontend: http://localhost:5173
echo - Backend:  http://localhost:8000
echo.
pause
