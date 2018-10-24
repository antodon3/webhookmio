from flask import Flask, request, make_response, jsonify

app = Flask(__name__)
log = app.logger


@app.route('/', methods=['POST'])
def webhook():
    risposta = "ciao"

    return make_response(jsonify({'fulfillmentText': risposta}))


if __name__ == '__main__':
    app.run()
