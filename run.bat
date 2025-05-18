call .venv\Scripts\activate.bat

:: Launch applications in parallel
echo 🚀 Launching applications...

:: FastAPI
start "FastAPI" cmd /c "cd src && python main.py run"

:: gRPC
start "gRPC" cmd /c "cd src && python main.py grpc"

:: Streamlit
start "Streamlit" cmd /k "cd web && streamlit run main.py --server.runOnSave True"

echo 🎉 All applications are running in separate windows!
echo Press any key to exit...
pause >nul