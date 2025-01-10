from app.models import SystemMetrics
from datetime import datetime


def test_new_metrics(app):
    """
    GIVEN a SystemMetrics model
    WHEN a new SystemMetrics is created
    THEN check the cpu_usage, ram_usage, disk_usage and timestamp fields are defined correctly
    """
    metrics = SystemMetrics(cpu_usage=45.2, ram_usage=68.7, disk_usage=72.1)

    assert metrics.cpu_usage == 45.2
    assert metrics.ram_usage == 68.7
    assert metrics.disk_usage == 72.1
    assert isinstance(metrics.timestamp, datetime)


def test_metrics_timestamp(app):
    """
    GIVEN a SystemMetrics instance
    WHEN the metrics is created
    THEN check the timestamp is set automatically
    """
    metrics = SystemMetrics()

    assert metrics.timestamp is not None
    assert isinstance(metrics.timestamp, datetime)
