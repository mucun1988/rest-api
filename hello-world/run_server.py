# curl -X POST -H "Content-Type: application/json" -d '{"a":1,"b":"2"}' http://localhost:5000/add

import flask

app = flask.Flask(__name__)

@app.route("/add", methods=["POST"])
def add():
    data = {"success": False}
    if flask.request.method=='POST':
        content = flask.request.get_json()
        a = float(content['a'])
        b = float(content['b'])
        data['sum'] = a + b

    return flask.jsonify(data)

if __name__ == "__main__":
	app.run(debug=False, threaded=False)