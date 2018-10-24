from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.route("/webhook", methods=['POST'])
def webhook():
    Req = request.get_json(silent=True, force=True)
    risposta = 'ciao'
    
    return make_response(jsonify({'fulfillmentText': risposta}))


if __name__ == '__main__':
    app.run()
