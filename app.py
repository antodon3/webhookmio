from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.route("/", methods=['POST'])
def webhook():
    Req = request.get_json(silent=True, force=True)
    risposta = 'ciao'
    
    #return make_response(jsonify({'fulfillmentText': risposta}))
    return make_response(jsonify({"speech": "Hello!",
    "displayText": "Hello!"
    }))
    

if __name__ == '__main__':
    app.run()
