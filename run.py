from app import create_app
import webview

app = create_app()

if __name__ == "__main__":
    webview.create_window("System Monitor", "http://localhost:5000")
    app.run(port=5000)
