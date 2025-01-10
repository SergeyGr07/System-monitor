from datetime import datetime

from app import db


class SystemMetrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    cpu_usage = db.Column(db.Float)
    ram_usage = db.Column(db.Float)
    disk_usage = db.Column(db.Float)

    def __init__(self, cpu_usage=None, ram_usage=None, disk_usage=None):
        super().__init__()
        self.timestamp = datetime.utcnow()
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
        self.disk_usage = disk_usage
