import requests

url = "https://enfoquetic.cl/datos.json"

response = requests.get(url)

if response.status_code == 200:
    clientes = response.json()

    print("Listado de Clientes Morosos Semestre 2023 :)")
    print("*******************************************************")
    for i, cliente in enumerate(clientes, start=1):
        nombre = cliente["nombre"]
        apellidos = cliente["paterno"] + " " + cliente["materno"]
        print(f"Id Cliente {i} ==> Nombre : {nombre} {apellidos}")
    print("*******************************************************")
else:
    print("Error al obtener los datos de los clientes. Código de estado:", response.status_code)
