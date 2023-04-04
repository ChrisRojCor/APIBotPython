import json
import requests
import time

from login import login


def solictudCambio():
    url = ""

    f = open("personas.json")
    data = json.load(f)
    token = f'Bearer {login()}'
    print(token)
    finalList = []
    listAccepted = []
    listError = []
    badRequest = []
    countToken = 0
    countTotal = 0
    countAccepted = 0
    countError = 0
    countBadRequest = 0

    for i in data:

        if countToken >= 500:
            token = f'Bearer {login()}'
            countToken = 0

        payload = json.dumps({
            "TipoDocumento": str(i["TipoDocumento"]),
            "NroDocumento": str(i["NroDocumento"]),
            "PrimerNombre": str(i["PrimerNombre"]),
            "PrimerApellido": str(i["PrimerApellido"]),
            "FechaNacimiento": str(i["FechaNacimiento"]),
            "Sexo": str(i["Sexo"]),
            "CodigoVacuna": int(i["CodigoVacuna"]),
            "NroDosis": int(i["NroDosis"]),
            "TipoEsquema": int(i["TipoEsquema"]),
            "CodigoInstitucion": str(i["CodigoInstitucion"]),
            "CodigoEstrategia": int(i["CodigoEstrategia"]),
            "FechaAplicacion": str(i["FechaAplicacion"]),
            "CorreoElectronico": str(i["CorreoElectronico"])
        })
        print(payload)

        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)

        countToken = countToken + 1
        countTotal = countTotal + 1
        finalList.append(str(i) + ',' + str(response.json()))

        if response.status_code == 200:
            listAccepted.append(str(i) + ',' + str(response.json()))
            countAccepted = countAccepted + 1

        if response.status_code == 202:
            listError.append(str(i) + ',' + str(response.json()))
            countError = countError + 1

        if response.status_code == 400:
            badRequest.append(str(i) + ',' + str(response.json()))
            countBadRequest = countBadRequest + 1

        if response.status_code == 500:
            print("Error en Servidor")

        print(f'Contador renovar token: {countToken}')
        print(f'Contador registros: {countTotal}')
        time.sleep(0.5)

    # Escribir lista con todos los registros
    with open('personasFinal.json', 'w') as personasFinal:
        json.dump(finalList, personasFinal)
        personasFinal.close()
        print("terminado JSON final")

    # Escribir lista con los registros aceptados
    with open('personasAceptadas.json', 'w') as personasAceptadas:
        json.dump(listAccepted, personasAceptadas)
        personasAceptadas.close()
        print("terminado JSON personasAceptadas")

    # Escribir lista con los registros con errores
    with open('personasErrores.json', 'w') as personasErrores:
        json.dump(listError, personasErrores)
        personasErrores.close()
        print("terminado JSON Errores")

    # Escribir lista con los registros que no pudieron cargarse
    with open('personasBadRequest.json', 'w') as personasBadRequest:
        json.dump(badRequest, personasBadRequest)
        personasBadRequest.close()
        print("terminado JSON Bad Request")

    print(f'Proceso de solicitud de cambios finalizada con un total de {countTotal} registros')
    print(f'Total exitosos: {countAccepted}')
    print(f'Total con error: {countError}')
    print(f'Total con bad request: {countBadRequest}')
