from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
###################################################################
    """Respond to incoming calls with a simple text message."""
    body = "No data"
    try:
        if request.method == 'POST':
            body = request.form['Body']
            print(request.form['Body'])
    except:
        print "No request.form['Body']"
    ## Start our TwiML response

    # Add a message

    print (body)
########################Calc#####################
    url = "http://17b6dbf9.ngrok.io"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Body\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'c': body,
        'cache-control': "no-cache",
        'postman-token': "5de0c339-56fd-7f99-5315-5a6f13dbef43"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
#######################################################
    print(response.text)
    resp = MessagingResponse()
    #resp.message(u'Didn\'t you, {}, know that this is {}'.format(utg.text, response.text))
    resp.message(u'Didn\'t you know that this is {}'.format(response.text))
    #resp.message(u'{}'.format(utg.text)
    return str(resp)	 	

if __name__ == "__main__":
    app.run(debug=True, port=5000)
