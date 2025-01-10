def test_app_creation(app):
    """
    GIVEN a Flask application
    WHEN the app is created
    THEN check the basic configuration
    """
    assert app.config["TESTING"] is True
    assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:"


def test_db_creation(app, db_metrics):
    """
    GIVEN a Flask application and database
    WHEN the database is initialized with a metric
    THEN check the metric exists
    """
    from app.models import SystemMetrics

    metrics = SystemMetrics.query.all()
    assert len(metrics) == 1
    assert metrics[0].cpu_usage == 45.2
