def obtener_dias_mes(nombre_mes):
    meses = {
        "Enero": 31,
        "Febrero": 28,
        "Marzo": 31,
        "Abril": 30,
        "Mayo": 31,
        "Junio": 30,
        "Julio": 31,
        "Agosto": 31,
        "Septiembre": 30,
        "Octubre": 31,
        "Noviembre": 30,
        "Diciembre": 31,
    }
    return meses.get(nombre_mes, None)

def obtener_festivos(nombre_mes):
    festivos = {
        "Enero": ["Año Nuevo"],
        "Febrero": ["Día de San Valentín"],
        "Marzo": ["Día de San José"],
        "Mayo": ["Día del Trabajador"],
        "Diciembre": ["Navidad"],
    }
    return festivos.get(nombre_mes, [])

if __name__ == "__main__":
    nombre_mes = input("Ingrese el nombre de un mes del año: ")

    dias = obtener_dias_mes(nombre_mes)
    festivos = obtener_festivos(nombre_mes)

    if dias is not None:
        print(f"{nombre_mes} tiene {dias} días.")
        if festivos:
            print(f"Festivos en {nombre_mes}: {', '.join(festivos)}")
        else:
            print("No hay festivos registrados para este mes.")
    else:
        print("Mes no válido. Asegúrese de ingresar un nombre de mes válido.")

