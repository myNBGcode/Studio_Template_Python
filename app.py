from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import requests
import json
import os
import sys
import cgi
import cgitb
cgitb.enable()





app = Flask(__name__)

# Provide the required values for API Path - Version - Sandbox_id
# You can find the proper values in each APIs' product page. 
# For more info visit developers.nbg.gr

# with open ('fileToWrite.py','w') as fileOutput:
#    sandbox_id=request.POST["sandboxid"]
#     fileOutput.write(request.POST["sandboxid"])

# @app.route('/')
# def test():
# return render_template('test.html')

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
# result = request.form
# return render_template("index.html",result = result)


import cgi


# sandbox_id = "to be filled"
# api  = "to be filled"
# version = "to be filled"
# username = "to be filled"
# client_id = "to be filled"

@app.route("/",methods = ['POST', 'GET'])
def hello():
            return render_template('index.html')
    
@app.route("/variables.py",methods = ['POST', 'GET'])
def variables():
            form = cgi.FieldStorage()
            global sandbox_id
            sandbox_id = request.values.get('sandboxid')
            global api
            api = request.values.get('api')
            global version
            version = request.values.get('apiversion')
            global username
            username = request.values.get('username')
            global client_id
            client_id = request.values.get('clientid')
            return render_template('index.html', api=api, sandbox_id=sandbox_id, version=version, username=username, client_id=client_id)

    
@app.route('/createsandbox',methods = ['POST', 'GET'])
def createsandbox():
    url = "https://apis.nbg.gr/sandbox/"+api+"/headers/"+version+"/sandbox/"
    data = '''{"sandboxId":"%s"}''' %(sandbox_id)
    headers = {"Client-Id": "%s"  %(client_id)  , 
               "content-type": "application/json",
               "accept": "application/json"}
    myResponse = requests.post(url, data = data, headers = headers)
    statuscode = myResponse.status_code
    data= json.loads(myResponse.content)
    return render_template('calls.html', data=data , api=api, sandbox_id=sandbox_id, version=version, username=username, client_id=client_id, statuscode=statuscode)

@app.route('/exportsandbox')
def exportsandbox():
    url = "https://apis.nbg.gr/sandbox/"+api+"/headers/"+version+"/sandbox/"+sandbox_id+"/"
    data = '''{"sandboxId":"%s"}''' %(sandbox_id)
    headers = {"Client-Id": "%s"  %(client_id),
                "content-type": "application/json",
                "accept": "application/json"}
    myResponse = requests.get(url, data = data, headers = headers)
    statuscode = myResponse.status_code
    data= json.loads(myResponse.content)
    return render_template('calls.html', data=data, api=api, sandbox_id=sandbox_id, version=version, username=username, client_id=client_id, statuscode=statuscode)
        
@app.route('/deletesandbox')
def deletesandbox():
    url = "https://apis.nbg.gr/sandbox/"+api+"/headers/"+version+"/sandbox/"+sandbox_id+"/"
    headers = {"Client-Id": "%s"  %(client_id)}
    myResponse = requests.delete(url, headers = headers)
    statuscode = myResponse.status_code
    if (statuscode==204):
        data="Sandbox deleted successfully! Warning: This is a custom written message; usually there is no response in delete requests." 
    elif (statuscode==404):
        data= json.loads(myResponse.content)
    return render_template('calls.html', data=data, api=api, sandbox_id=sandbox_id, version=version, username=username, client_id=client_id, statuscode=statuscode)

@app.route('/myaccounts')
def myaccounts():
    url = "https://apis.nbg.gr/sandbox/"+api+"/headers/"+version+"/obp/my/accounts"
    headers = { "content-type": "application/json",
                "accept": "application/json",
                "Client-Id": "%s"  %(client_id),
                "sandbox_id": "%s" %(sandbox_id),
                "application_id": "FCB4CCD2-8111-424A-A7A3-2BB8B82F49DD",
                "provider_username": "NBG.gr",
                "provider_id": "NBG",
                "provider": "NBG.GR",
                "request_id": "REQUEST_CHECK_1"
                }
    myResponse = requests.get(url, headers = headers)
    data= json.loads(myResponse.content)
    return render_template('index.html', data=data)

@app.route('/createsandboxuser')
def createsandboxuser():
    url = "https://apis.nbg.gr/sandbox/"+api+"/headers/"+version+"/sandbox/"+sandbox_id+"/users"
    data = '''{"Username":"%s"}''' %(username)
    headers = {"content-type": "application/json",
               "accept": "application/json",
               "Client-Id": "%s"  %(client_id)
              }
    myResponse = requests.post(url, data = data, headers = headers)
    statuscode = myResponse.status_code
    data= json.loads(myResponse.content)
    return render_template('calls.html', data=data, api=api, sandbox_id=sandbox_id, version=version, username=username, client_id=client_id, statuscode=statuscode)



if __name__== "__main__":
            print ("hello")
            app.run(debug=True, host="0.0.0.0", port=8000)
        
            
            