from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://localhost:27017/crudapp'
mongo = PyMongo(app)

CORS(app)
db = mongo.db.users

@app.route("/users", methods=["POST"])
def createUser():
    try:
        inserted_id = db.insert_one({
            'name': request.json['name'],
            'email': request.json['email'],
            'contact': request.json['contact'],
            'address': request.json['address'],
        }).inserted_id

        return jsonify({'id': str(inserted_id), 'msg': "User is Added Successfully!!!" })

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route("/")
def index():
    return "<h1>Hello, Prashant</h1>"

if __name__ == '__main__':
    app.run(debug=True)
