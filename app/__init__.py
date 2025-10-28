# app/__init__.py
import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)

    # Safe defaults
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "dev-key-change-me"),
    )

    # Allow tests (or other callers) to override config
    if test_config:
        app.config.update(test_config)

    # Register blueprints
    from . import routes
    app.register_blueprint(routes.bp)

    return app
