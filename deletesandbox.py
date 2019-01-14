#!/usr/bin/env python3
print ("Content-type: text/json\n\n")

import http.client

conn = http.client.HTTPSConnection("apis.nbg.gr")

#Change REPLACE_SANDBOX_ID with the ID of your sandbox
conn.request("DELETE", "/public/sandbox/obp.account.sandbox/v1.1/sandbox/REPLACE_SANDBOX_ID")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
