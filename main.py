from solicitudCambioEstrategia import solictudCambio
from JSONCSV import JSONtoTXT
from CSVJSON import CSVtoJSON

print("Solicitud de corrección de registros")
input("presione tecla ENTER para continuar...")

# CSV a JSON
CSVtoJSON()

# Solicitud cambio de estrategia de vacunacion
solictudCambio()

# Resultados
JSONtoTXT()

print("Solicitudes registradas")
input("presione tecla ENTER para finalizar...")
