from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)

def str_return(RGW):
    global RGS
    global live_counter
###################################################
    body = "No data"
    try:
        if request.method == 'POST':
            CCH = request.form['Body']
            print(request.form['Body'])
    except:
        print "No request.form['Body']"
####################################################
    if CCH == 'ref':
        new_word()
    for i in range(len(RGW)):
        if RGW[i] == CCH:
            RGL = list(RGS)
            RGL[i] = CCH
            RGS = "".join(RGL)

####################################################
    print(RGS)
    if RGS == RGW:
    	return 'You win'
    else:
        return (RGS)	 	
RGW = ''
RGS = ''
live_counter = 0
def new_word():
    global RGW
    global RGS
    global live_counter
    url = "http://watchout4snakes.com/wo4snakes/Random/RandomWord"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Body\"\r\n\r\n4+19999\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {}

    response = requests.request("POST", url, data=payload, headers=headers)

    RGW = response.text
        
    RGS = ''

    live_counter = 5

    for i in range(len(RGW)):
         RGS += '_'
    return()
new_word()
@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    global RGS
    global live_counter
    resp = MessagingResponse()
    respb = MessagingResponse()
    RGS2 = RGS
    RGS = str_return(RGW)
    if RGS == RGS2:
            live_counter = live_counter-1
    print(RGW)
    resp.message(RGS + ' ' +str(live_counter)) 
    if live_counter == 0: 
        return(" You lose, it was- " + RGW)
        new_word()
    else:
        return (str(resp))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
