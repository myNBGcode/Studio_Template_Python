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

