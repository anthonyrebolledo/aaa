def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # Máximo 7 días
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para analizar las temperaturas
def analizar_temperaturas(temperaturas):
    max_temp = max(temperaturas)
    min_temp = min(temperaturas)
    promedio = sum(temperaturas) / len(temperaturas)
   
    dias_sobre_promedio = [i+1 for i, temp in enumerate(temperaturas) if temp > promedio]
   
    alertas = []
    for i, temp in enumerate(temperaturas):
        if temp >= 40:
            alertas.append(f"Alerta: Día {i+1} tuvo una temperatura de {temp}°C (muy alta)")
        elif temp <= 0:
            alertas.append(f"Alerta: Día {i+1} tuvo una temperatura de {temp}°C (muy baja)")
   
    return max_temp, min_temp, promedio, dias_sobre_promedio, alertas
# Programa principal
temperaturas = ingresar_temperaturas()
max_temp, min_temp, promedio, dias_sobre_promedio, alertas = analizar_temperaturas(temperaturas)
print("\nResultados:")
print(f"Lista de temperaturas ingresadas: {temperaturas}")
print(f"Temperatura máxima: {max_temp}°C")
print(f"Temperatura mínima: {min_temp}°C")
print(f"Días con temperatura sobre el promedio ({promedio:.2f}°C): {dias_sobre_promedio}")
if alertas:
    print("\nAlertas:")
    for alerta in alertas:
        print(alerta)
else:
    print("\nNo hubo alertas de temperaturas extremas.")
