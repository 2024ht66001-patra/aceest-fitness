from flask import Flask, jsonify

def create_app(config=None):
    app = Flask(__name__)
    if config:
        app.config.update(config)

    @app.get("/")
    def index():
        return "Welcome to ACEest Fitness!", 200

    @app.get("/health")
    def health():
        return jsonify(status="ok"), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
