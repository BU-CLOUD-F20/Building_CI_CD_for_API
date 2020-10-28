import os

# Import Flask
from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS

# Import DB
from backend.database.db import initialize_db
from backend.resources.routes import initialize_routes

# Initialization
app = Flask(__name__, static_folder="ui/build")
api = Api(app, catch_all_404s=True)
cors = CORS(app, resources=r"/*")

# cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Config
app.config["MONGODB_SETTINGS"] = {
    "host": "mongodb+srv://cicd-team:ec528@cicd-cluster0.s9vur.gcp.mongodb.net/doubly?retryWrites=true&w=majority"
}

initialize_db(app)
initialize_routes(api)


# Serve UI static files
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path == "":
        return send_from_directory("UI/build", "index.html")
    else:
        if os.path.exists("UI/build/" + path):
            return send_from_directory("UI/build", path)
        else:
            return send_from_directory("UI/build", "index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    # app.run(debug=True, port=5000)
