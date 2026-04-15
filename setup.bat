@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
where python >nul 2>nul
if %errorlevel%==0 (
    python "%SCRIPT_DIR%scripts\manage_env.py" setup
    exit /b %errorlevel%
)

where py >nul 2>nul
if %errorlevel%==0 (
    py -3 "%SCRIPT_DIR%scripts\manage_env.py" setup
    exit /b %errorlevel%
)

echo Python nao encontrado no PATH. Instale o Python 3.11+ e tente novamente.
exit /b 1
