# Import Flask
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

# Import DB
from database.db import initialize_db
from resources.routes import initialize_routes

# Initialization
app = Flask(__name__)
api = Api(app, catch_all_404s=True)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


# Config
app.config['MONGODB_SETTINGS'] = {
    'host':
    'mongodb+srv://cicd-team:ec528@cicd-cluster0.s9vur.gcp.mongodb.net/doubly?retryWrites=true&w=majority'
}

# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#     return response

initialize_db(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    # app.run(debug=True, port=5000)
