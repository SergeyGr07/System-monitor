import sys
from pathlib import Path
import pytest
from app import create_app, db
from app.models import SystemMetrics

sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture
def app():
    app = create_app()
    app.config.update({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def sample_metrics():
    return {"cpu_usage": 45.2, "ram_usage": 68.7, "disk_usage": 72.1}


@pytest.fixture
def db_metrics(app):
    metrics = SystemMetrics(cpu_usage=45.2, ram_usage=68.7, disk_usage=72.1)
    db.session.add(metrics)
    db.session.commit()
    return metrics
