from flask import Flask, render_template
import docker
import psutil
import time

app = Flask(__name__)

client = docker.from_env()

@app.route("/")
def home():
    containers = client.containers.list(all=True)

    system = {
            "cpu": psutil.cpu_percent(interval=0.5),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage("/").percent,
            "uptime": int(time.time() - psutil.boot_time())
    }

    return render_template(
            "index.html",
            containers=containers,
            system=system
            )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
