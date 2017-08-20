from flask import Flask, request, redirect
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

#def hello_monkey():
#	url = "https://526c6f2d.ngrok.io"
#	headers ={}
#
#	response = requests.request("GET", url, headers=headers)
#	
#	return(response.text)
#
#	message=raw_input()
	
	
def cha():
	resp = MessagingResponse()
	resp.message('Hello,buy our products')
	return(str(resp))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
