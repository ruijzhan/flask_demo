from flask import Flask

def create_app():
    app = Flask('demo')

    @app.route("/")
    def index():
        return "Hello Flask"

    return app

application = create_app()
