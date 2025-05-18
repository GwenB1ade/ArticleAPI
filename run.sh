. .venv/bin/activate


echo "🚀 Launching FastAPI app..."
cd src
python3 main.py run &

echo "🔌 Launching gRPC server..."
python3 main.py grpc &

echo "📊 Launching Streamlit app..."
cd ..
cd web
streamlit run main.py --server.runOnSave True &

echo "🎉 All applications are running!"

wait