from flask import Flask, request

app = Flask(__name__)
@app.route('/welcome', methods=['GET'])
def index():
    return "welcome developer"

@app.route('/whatsapp', methods=['GET'])
def VerifyToken():
    try:
        accessToken = "78SAJSN3ANS76S8DSHDBSBDS"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token != None and challenge != None and token == accessToken:
            return challenge
        else:
            return "", 400
    except:
        return "", 400

@app.route('/whatsapp', methods=['POST'])
def ReceivedMessage() :

    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        number = message[ "from"]

        return "EVENT_RECEIVED"
    except :
        return "EVENT RECEIVED"
    
    

if(__name__== "__main__"):
   app.run()
