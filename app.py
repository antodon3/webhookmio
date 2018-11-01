from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

# default route
@app.route('/)
def index():
    return 'Hello World!'

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    req = request.get_json(force=True)
    action = req.get('queryResult').get('action')
    risposta = 'ciao'
    
    return make_response(jsonify({'fulfillmentText': risposta}))
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

