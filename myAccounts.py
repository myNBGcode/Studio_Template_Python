#!/usr/bin/env python3
print ("Content-type: text/json\n\n")

import http.client

conn = http.client.HTTPSConnection("apis.nbg.gr")

#Replace the header values with the values you got when you created your sandbox
headers = {
    'x-ibm-client-id': "REPLACE_THIS_KEY",
    'sandbox_id': "REPLACE_THIS_VALUE",
    'application_id': "REPLACE_THIS_VALUE",
    'provider_username': "REPLACE_THIS_VALUE",
    'provider_id': "REPLACE_THIS_VALUE",
    'provider': "REPLACE_THIS_VALUE",
    'request_id': "REPLACE_THIS_VALUE",
    'accept': "text/json"
    }

conn.request("GET", "/public/sandbox/obp.account.sandbox/v1.1/obp/my/accounts", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
