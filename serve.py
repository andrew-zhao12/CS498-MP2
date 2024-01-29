from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

def stress_cpu():
    subprocess.Popen(["python", "stress_cpu.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.route("/", methods=["GET", "POST"])
def handle_requests():
    if request.method == "GET":
        private_ip = socket.gethostbyname(socket.gethostname())
        return private_ip

    elif request.method == "POST":
        stress_cpu()
        return "Stressing CPU in a separate process."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
