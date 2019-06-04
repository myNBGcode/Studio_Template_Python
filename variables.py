from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import requests
import json
import os
import sys
import cgi
import cgitb

cgitb.enable()

print ("PRINTARE TWRA")
form = cgi.FieldStorage()
searchterm =  form.getvalue('sandboxid', 0)
print (searchterm)
print ("######################")

#api="replace"
#version="replace"
sandbox_id="replace"
#username="replace"
#client_id="replace"

formData = cgi.FieldStorage()    


# api = formData.getvalue('api')
# version=formData.getvalue('apiversion')
# sandbox_id= formData.getvalue('sandboxid')
# username=formData.getvalue('username')
# client_id=formData.getvalue('clientid')

# #if(method=='POST')
# f = open('UserDetails.py','a')
# api = formData.getvalue('api')
# f.write ("{} ".format(api))
# version=formData.getvalue('apiversion')
# f.write ("{}\n".format(version))
# f.close ()