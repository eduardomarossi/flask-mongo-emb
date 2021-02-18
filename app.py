from flask import Flask, request, jsonify
from pymongo import MongoClient
from decouple import config

app = Flask(__name__)


MONGO_HOST = config('MONGO_HOST')
MONGO_USERNAME = config('MONGO_USERNAME')
MONGO_PASSWORD = config('MONGO_PASSWORD')

@app.route('/', methods=['POST'])
def insert_student_progress():
    REQUIRED_FIELDS = ['name', 'time', 'id', 'url', 'semester', 'course']
    for k in REQUIRED_FIELDS:
        if k not in request.form:
            return jsonify(status='ERROR', error='Missing field {}'.format(k))

    client = MongoClient(host=MONGO_HOST, username=MONGO_USERNAME, password=MONGO_PASSWORD, authSource='admin')
    db = client['test']
    collection = db['progress']
    collection.insert_one(request.form.to_dict())
    print(request.form)
    return jsonify(status='OK')
