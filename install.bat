@echo off
setlocal enabledelayedexpansion

:: Check if Docker is running
echo Checking Docker status...
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo � Docker is not running. Attempting to start...
    
    :: Try to start Docker Desktop (Windows-specific)
    start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    
    :: Wait for Docker to start
    echo ⏳ Waiting for Docker to start...
    :docker_wait_loop
    docker info >nul 2>&1
    if %errorlevel% neq 0 (
        timeout /t 1 >nul
        goto docker_wait_loop
    )
    echo ✅ Docker started successfully
) else (
    echo ℹ️ Docker is already running
)

:: Check for docker-compose
where docker-compose >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ docker-compose is not installed
    exit /b 1
)

:: Start containers
echo 🚀 Starting containers with docker-compose...
docker-compose up -d

echo 🎉 Containers started successfully!
echo To view logs use: docker-compose logs -f

:: Create Python virtual environment
echo 🐍 Creating virtual environment...
python -m venv .venv
call .venv\Scripts\activate.bat

:: Install dependencies
if exist req.txt (
    echo 📦 Installing dependencies...
    
    :: Check for uv pip
    where uv >nul 2>&1
    if %errorlevel% equ 0 (
        echo ⚡ Using uv pip (faster installation)...
        uv run pip install -e .
    ) else (
        echo 🐢 Using standard pip (install 'uv' for faster installs)...
        pip install -e .
        
        echo 💡 Tip: Install 'uv' for much faster dependency installation:
        echo      curl -LsSf https://astral.sh/uv/install.sh | sh
    )
) else (
    echo ⚠️ req.txt not found. Skipping dependency installation.
)

echo 🎉 The application was successfully installed. To run it, enter the following commands
echo run.bat

