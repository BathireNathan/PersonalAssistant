from flask import Flask, request, jsonify
from managetasks import manage_tasks_collection

app = Flask(__name__)
app.config["DEBUG"] = False


@app.route('/', methods=['GET'])
def home():
    print(request.args)
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/taskhandler', methods=['GET'])
def NotifMapper():
    manage_tasks_collection()
    return "success"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")