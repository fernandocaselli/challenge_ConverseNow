import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'conversenow',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class tabla1(db.Document):
    client_id = db.StringField()
    path = db.StringField()
    sentence = db.StringField()
    up_votes = db.IntField()
    down_votes = db.IntField()
    age = db.StringField()
    gender = db.StringField()
    accent = db.StringField()
    locale = db.StringField()
    segment = db.StringField()
    def to_json(self):
        return {"client_id": self.client_id,
                "path": self.path,
                "sentence": self.sentence,
                "up_votes": self.up_votes,
                "down_votes": self.down_votes,
                "age": self.age,
                "gender": self.gender,
                "accent": self.accent,
                "locale": self.locale,
                "segment": self.segment}

@app.route('/', methods=['GET'])
def query_records():
    accent = request.args.get('accent')
    t1 = tabla1.objects(accent=accent).first()
    if not t1:
        return jsonify({'error': 'sin data'})
    else:
        return jsonify(t1.to_json())

if __name__ == "__main__":
    app.run(debug=True)