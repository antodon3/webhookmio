import json

from flask import Flask, request, make_response, jsonify

app = Flask(__name__)
log = app.logger


@app.route('/', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook
    This is meant to be used in conjunction with the weather Dialogflow agent
    """
    req = request.get_json(silent=True, force=True)
    parameters = req['queryResult']['parameters']
    text = parameters['text']

    print(parameters)

    risposta = "ciao"
    print('Response: ' + risposta)

    return make_response(jsonify({'fulfillmentText': risposta}))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
