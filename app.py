import os
import socket
from datetime import datetime, timezone

from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.get("/")
def home():
    return render_template(
        "index.html",
        app_name=os.getenv("APP_NAME", "Monkey Flask App"),
        environment=os.getenv("APP_ENV", "development"),
        hostname=socket.gethostname(),
        current_time=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    )


@app.get("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
