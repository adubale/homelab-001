from flask import Flask, render_template
import docker

app = Flask(__name__)

client = docker.from_env()

@app.route("/")
def home():
    containers = client.containers.list(all=True)

    return render_template(
            "index.html",
            containers=containers
            )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
