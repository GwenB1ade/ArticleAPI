#!/bin/bash


if ! docker info >/dev/null 2>&1; then
    echo "🐳 Docker is not running. Attempting to start..."
    
    # Для разных операционных систем
    case "$(uname -s)" in
        Linux*)
            # Для Linux (systemd)
            if command -v systemctl >/dev/null; then
                sudo systemctl start docker
            else
                echo "❌ Failed to start Docker (systemd not found)"
                exit 1
            fi
            ;;
        Darwin*)
            # Для MacOS
            open -a Docker
            ;;
        *)
            echo "❌ Unsupported OS"
            exit 1
            ;;
    esac
    
    echo "⏳ Waiting for Docker to start..."
    while ! docker info >/dev/null 2>&1; do
        sleep 1
    done
    echo "✅ Docker started successfully"
else
    echo "ℹ️ Docker is already running"
fi

if ! command -v docker-compose >/dev/null; then
    echo "❌ docker-compose is not installed"
    exit 1
fi

echo "🚀 Starting containers with docker-compose..."
docker-compose up -d

echo "🎉 Containers started successfully!"
echo "To view logs use: docker-compose logs -f"

echo "🐍 Creating virtual environment..."
python3 -m venv .venv
. .venv/bin/activate


if [ -f "req.txt" ]; then
    echo "📦 Installing dependencies..."
    
    if command -v uv &> /dev/null; then
        echo "⚡ Using uv pip (faster installation)..."
        uv run pip install -e .
    else
        echo "🐢 Using standard pip (install 'uv' for faster installs)..."
        pip install -e .
        
        echo "💡 Tip: Install 'uv' for much faster dependency installation:"
        echo "      curl -LsSf https://astral.sh/uv/install.sh | sh"
    fi
else
    echo "⚠️ req.txt not found. Skipping dependency installation."
fi

echo "🎉 The application was successfully installed. To run it, enter the following commands"
echo "chmod +x run.sh"
echo "./run.sh"