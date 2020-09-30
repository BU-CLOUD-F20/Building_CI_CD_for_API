# Import Flask
from flask import Flask
from flask_restful import Api
from flask_cors import CORS


# Import DB
from database.db import initialize_db
from resources.routes import initialize_routes


# Initialization
app = Flask(__name__)
CORS(app)
api = Api(app, catch_all_404s=True)

# Config
app.config['MONGODB_SETTINGS'] = {
    'host':
    'mongodb+srv://cicd-team:ec528@cicd-cluster0.s9vur.gcp.mongodb.net/doubly?retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    # app.run(debug=True, port=5000)
