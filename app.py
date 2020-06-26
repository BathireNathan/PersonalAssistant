from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = False


@app.route('/', methods=['GET'])
def home():
    print(request.args)
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/NotifMapper', methods=['GET'])
def home():
    print(request.args)
    return "success"

app.run()