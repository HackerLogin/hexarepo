# api.py
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return open("index.html").read()

@app.route("/start", methods=["POST"])
def start():
    external_port = create_container()  # 자동 생성 코드
    url = f"http://{SERVER_IP}:{external_port}"

    return jsonify({"url": url})

@app.post("/stop")
def stop():
    subprocess.Popen(["python3", "auto_stop.py"])
    return {"status": "stopped"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
