import json

import requests as requests


# Login a Paiweb con token como response
def login():
    url = ""

    tipoID = "CC"
    ID = ""
    password = ""

    payload = json.dumps({
        "tipoIdentificacion": tipoID,
        "Identificacion": ID,
        "Password": password
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'cookiesession1=678B76D54688024ABCDEFGHIJKLM2A49'
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    responsejson = response.json()

    token = responsejson['token']
    print(token)
    return token
