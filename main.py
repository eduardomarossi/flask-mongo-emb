from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/', methods=['POST'])
def insert_student_progress():
    REQUIRED_FIELDS = ['name', 'time', 'id', 'url']
    for k in REQUIRED_FIELDS:
        if k not in request.form:
            return jsonify(status='ERROR', error='Missing field {}'.format(k))

    client = MongoClient(host='###', username='###', password='####', authSource='###')
    db = client['test']
    collection = db['progress']
    collection.insert_one(request.form.to_dict())
    print(request.form)
    return jsonify(status='OK')