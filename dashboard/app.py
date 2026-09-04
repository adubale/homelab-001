from flask import Flask, render_template
import docker
import psutil
import time


app = Flask(__name__)


client = docker.from_env()


def format_uptime(seconds):
    days, remainder = divmod(int(seconds), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, _ = divmod(remainder, 60)

    if days:
        return f"{days}d {hours}h"
    if hours:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"


@app.route("/")
def home():
    containers = client.containers.list(all=True)


    system = {
            "cpu": psutil.cpu_percent(interval=0.5),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage("/").percent,
            "uptime": format_uptime(time.time() - psutil.boot_time())
    }


    return render_template(
            "index.html",
            containers=containers,
            system=system
            )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
