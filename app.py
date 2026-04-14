from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>MLOps Project 1: Containerized App is Running!</h1>"

if __name__ == "__main__":
    # Host 0.0.0.0 zaroori hai Docker ke liye
    app.run(host='0.0.0.0', port=5000)print("MLOps Project 1: Containerized App is Running!")
