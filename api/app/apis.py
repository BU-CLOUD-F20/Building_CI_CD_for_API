from app import app


@app.route("/")
def index():
    return "FLASK APP SETUP"
