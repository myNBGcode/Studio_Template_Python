#!/usr/bin/env python3
print ("Content-type: text/json\n\n")

import http.client

conn = http.client.HTTPSConnection("apis.nbg.gr")


#Change the REPLACE_SANDBOX_ID with the id you want for your Sandbox
payload = "{\"sandbox_id\":\"REPLACE_SANDBOX_ID\"}"

headers = {
    'content-type': "text/json",
    'accept': "text/json",
    'x-ibm-client-id': "REPLACE_THIS_KEY",
    'sandbox_id': "REPLACE_THIS_VALUE",
    'application_id': "REPLACE_THIS_VALUE",
    'provider_username': "REPLACE_THIS_VALUE",
    'provider_id': "REPLACE_THIS_VALUE",
    'provider': "REPLACE_THIS_VALUE",
    'request_id': "REPLACE_THIS_VALUE"
    }

conn.request("POST", "/public/sandbox/obp.account.sandbox/v1/sandbox", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
