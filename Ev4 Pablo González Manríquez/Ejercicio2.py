import json
import requests
class Mindicador:
    def __init__(self, indicador, fecha):
        self.indicador = indicador
        self.fecha = fecha

    def InfoApi(self):
        url = f'https://mindicador.cl/api/{self.indicador}/{self.fecha}'
        response = requests.get(url)
        data = json.loads(response.text)
        return data

def main():
    print("Buscar Indicadores por Fecha")
    print("************************************************")
    print("Seleccione Indicador a Consultar.")
    print("1.- Valor UF")
    print("2.- Valor Dólar")
    print("3.- Valor Euro")
    print("************************************************")

    opcion = input("Ingrese una Opción: ")

    if opcion == '1':
        tipo_indicador = "uf"
    elif opcion == '2':
        tipo_indicador = "dolar"
    elif opcion == '3':
        tipo_indicador = "euro"
    else:
        print("Opción no válida.")
        return

    fecha_input = input("Ingrese la fecha a consultar (formato: DD-MM-YYYY): ")
    fecha = fecha_input.strip()

    mindicador = Mindicador(tipo_indicador, fecha)
    data = mindicador.InfoApi()

    if "serie" in data:
        valor = data["serie"][0]["valor"]
        print(f"El valor de la {tipo_indicador.upper()} para la fecha {fecha} es de ${valor:.2f}")
    else:
        print(f"No se encontró el valor para la fecha {fecha}.")

if __name__ == "__main__":
    main()
