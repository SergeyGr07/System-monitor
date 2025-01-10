import json
from unittest.mock import patch


def test_index_route(client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"System Monitor" in response.data


@patch("psutil.cpu_percent")
@patch("psutil.virtual_memory")
@patch("psutil.disk_usage")
def test_metrics_route(mock_disk, mock_memory, mock_cpu, client):
    """
    GIVEN a Flask application
    WHEN the '/metrics' page is requested (GET)
    THEN check that the metrics are returned correctly
    """
    mock_cpu.return_value = 45.2
    mock_memory.return_value.percent = 68.7
    mock_disk.return_value.percent = 72.1

    response = client.get("/metrics")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["cpu"] == 45.2
    assert data["ram"] == 68.7
    assert data["disk"] == 72.1


@patch("psutil.cpu_percent")
@patch("psutil.virtual_memory")
@patch("psutil.disk_usage")
def test_start_recording(mock_disk, mock_memory, mock_cpu, client, app):
    """
    GIVEN a Flask application
    WHEN the '/start_recording' endpoint is posted to
    THEN check that the metrics are saved to the database
    """
    mock_cpu.return_value = 45.2
    mock_memory.return_value.percent = 68.7
    mock_disk.return_value.percent = 72.1

    response = client.post("/start_recording")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["success"] is True


def test_get_history(client, db_metrics):
    """
    GIVEN a Flask application with existing metrics
    WHEN the '/get_history' endpoint is requested
    THEN check that the correct history is returned
    """
    response = client.get("/get_history")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["cpu"] == 45.2
    assert data[0]["ram"] == 68.7
    assert data[0]["disk"] == 72.1
