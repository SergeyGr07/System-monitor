import webview

from app import create_app

app = create_app()

if __name__ == "__main__":
    webview.create_window("System Monitor", "http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)
