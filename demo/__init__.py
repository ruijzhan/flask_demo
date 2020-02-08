from flask import Flask
from demo.blueprints.demo import demo_bp

def create_app():
    app = Flask('demo')

    register_blueprints(app)

    return app

def register_blueprints(app):
    app.register_blueprint(demo_bp)

application = create_app()
