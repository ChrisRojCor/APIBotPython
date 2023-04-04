import pandas as pd


def JSONtoTXT():
    personasFinal = pd.read_json('personasFinal.json')
    personasAceptadas = pd.read_json('personasAceptadas.json')
    personasErrores = pd.read_json('personasErrores.json')
    personasBadRequest = pd.read_json('personasBadRequest.json')
    personasFinal.to_csv("personasFinal.csv")
    personasFinal.to_csv("personasFinal.txt")
    personasAceptadas.to_csv("personasAceptadas.txt")
    personasErrores.to_csv("personasErrores.txt")
    personasBadRequest.to_csv("personasBadRequest.txt")
