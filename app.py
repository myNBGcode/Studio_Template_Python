from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')
    


@app.route('/createsandbox')
def createsandbox():
    url = "https://apis.nbg.gr/public/sandbox/obp.account.sandbox/v1.1/sandbox"
    data = '''{"sandbox_id":"REPLACE_THIS_VALUE"}'''
    headers = {"x-ibm-client-id": "REPLACE_THIS_VALUE",
                "content-type": "application/json",
                "accept": "application/json"}
    myResponse = requests.post(url, data = data, headers = headers)
    data= myResponse.content
    print (data)
    return (data)

@app.route('/deletesandbox')
def deletesandbox():
    url = "https://apis.nbg.gr/public/sandbox/obp.account.sandbox/v1.1/sandbox/REPLACE_THIS_VALUE"
    headers = {"x-ibm-client-id": "REPLACE_THIS_VALUE"}
    myResponse = requests.delete(url, headers = headers)
    data= myResponse.content
    print (data)
    return (data)

@app.route('/myaccounts')
def myaccounts():
    url = "https://apis.nbg.gr/public/sandbox/obp.account.sandbox/v1.1/obp/my/accounts"
    headers = { "content-type": "application/json",
                "accept": "application/json",
                "x-ibm-client-id": "REPLACE_THIS_VALUE",
                "sandbox_id": "REPLACE_THIS_VALUE",
                "application_id": "REPLACE_THIS_VALUE",
                "provider_username": "REPLACE_THIS_VALUE",
                "provider_id": "REPLACE_THIS_VALUE",
                "provider": "REPLACE_THIS_VALUE",
                "request_id": "REPLACE_THIS_VALUE"
                }
    myResponse = requests.get(url, headers = headers)
    data= myResponse.content
    print (data)
    return (data)

if __name__== "__main__":
	app.run(debug=True, host="0.0.0.0", port=8000)
