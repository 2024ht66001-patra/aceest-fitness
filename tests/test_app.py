import importlib
import pytest

def _load_flask_app():
    """Load a Flask app from app.py.
    Supports either:
      - app.py with a global `app` (Flask instance), or
      - app.py with a `create_app()` factory that returns a Flask instance.
    The returned app is configured for testing.
    """
    try:
        mod = importlib.import_module("app")
    except ModuleNotFoundError as e:
        raise RuntimeError(
            "Could not import 'app.py'. Create app.py with either a global 'app' "
            "or a 'create_app()' function."
        ) from e

    # App factory pattern
    if hasattr(mod, "create_app") and callable(getattr(mod, "create_app")):
        app = mod.create_app({"TESTING": True})
        return app

    # Global app pattern
    if hasattr(mod, "app"):
        app = getattr(mod, "app")
        try:
            app.config.update(TESTING=True)
        except Exception:
            pass
        return app

    raise RuntimeError(
        "No Flask application found. In app.py, define either a global 'app' "
        "or a 'create_app()' function."
    )

@pytest.fixture(scope="session")
def app():
    return _load_flask_app()

@pytest.fixture()
def client(app):
    return app.test_client()

def test_health_endpoint_returns_ok(client):
    """ /health should exist and return JSON with status='ok'. """
    resp = client.get("/health")
    assert resp.status_code == 200, "Expected 200 OK from /health"
    try:
        data = resp.get_json()
    except Exception:
        data = None
    assert isinstance(data, dict), "Expected JSON body from /health"
    assert str(data.get("status")).lower() == "ok", "Expected status='ok' in /health response"

def test_index_route_returns_200(client):
    """ / should respond 200 and contain a friendly message. """
    resp = client.get("/")
    assert resp.status_code == 200, "Expected 200 OK from /"
    body = resp.data or b""
    assert any(
        token in body for token in [b"Welcome", b"ACEest", b"Fitness", b"Hello"]
    ), "Homepage should contain a friendly greeting or brand text."
