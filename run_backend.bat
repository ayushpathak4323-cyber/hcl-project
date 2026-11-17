@echo off
echo ========================================================
echo   Starting LoanPulse Backend (Django + Channels ASGI)
echo ========================================================
cd /d "%~dp0backend"

if not exist "venv\Scripts\activate.bat" (
    echo Virtual environment not found. Creating venv...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Installing backend dependencies...
    pip install -r requirements.txt
    echo Applying database migrations...
    python manage.py migrate
) else (
    call venv\Scripts\activate.bat
)

echo.
echo Launching Django server on http://localhost:8000 ...
python manage.py runserver 0.0.0.0:8000
pause
