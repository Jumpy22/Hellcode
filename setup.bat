@echo off

REM Check if Python is installed
where python > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

REM Install required packages
python -m pip install urllib3 requests cryptography

echo Installation completed successfully.
