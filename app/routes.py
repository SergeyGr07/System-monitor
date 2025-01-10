from flask import Blueprint, render_template, jsonify
import psutil
from app.models import SystemMetrics
from app import db


main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/metrics")
def get_metrics():
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent

    return jsonify({"cpu": cpu_usage, "ram": ram_usage, "disk": disk_usage})


@main.route("/start_recording", methods=["POST"])
def start_recording():
    metrics = SystemMetrics(
        cpu_usage=psutil.cpu_percent(),
        ram_usage=psutil.virtual_memory().percent,
        disk_usage=psutil.disk_usage("/").percent,
    )
    db.session.add(metrics)
    db.session.commit()
    return jsonify({"success": True})


@main.route("/get_history")
def get_history():
    metrics = SystemMetrics.query.order_by(SystemMetrics.timestamp.desc()).all()
    history = []
    for metric in metrics:
        history.append(
            {
                "timestamp": metric.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "cpu": metric.cpu_usage,
                "ram": metric.ram_usage,
                "disk": metric.disk_usage,
            }
        )
    return jsonify(history)
