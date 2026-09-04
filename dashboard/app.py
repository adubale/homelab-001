from flask import Flask, render_template, redirect
import docker
import psutil
import time

app = Flask(__name__)

docker_client = docker.from_env()


def format_uptime(seconds):
    days, remainder = divmod(int(seconds), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, _ = divmod(remainder, 60)

    if days:
        return f"{days}d {hours}h"
    if hours:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"


def get_container_image(container):
    try:
        if container.image.tags:
            return container.image.tags[0]
        return "Unknown image"
    except docker.errors.ImageNotFound:
        return "Unknown image"


@app.post("/containers/<container_name>/start")
def start_container(container_name):
    container = docker_client.containers.get(container_name)
    container.start()

    return redirect("/")


@app.post("/container/<container_name>/stop")
def stop_container(container_name):
    container = docker_client.containers.get(container_name)
    container.stop()

    return redirect("/")


@app.post("/container/<container_name>/restart")
def restart_container(container_name):
    container = docker_client.containers.get(container_name)
    container.restart()

    return redirect("/")


@app.route("/")
def home():
    containers = docker_client.containers.list(all=True)

    container_data = []

    for container in containers:
        container_data.append({
            "name": container.name,
            "image": get_container_image(container),
            "status": container.status,
        })

    system = {
        "cpu": psutil.cpu_percent(interval=0.5),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "uptime": format_uptime(time.time() - psutil.boot_time()),
    }

    return render_template(
        "index.html",
        containers=container_data,
        system=system,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
