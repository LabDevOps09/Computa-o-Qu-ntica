# Ideia: A variação em altitude (latitude/longitude) reflete variação em outra dimensão (ex: pressão, temperatura).

latitude = 45.0
altitude = 1000  # metros
temperatura = 15 - (altitude / 100)  # modelo simples

print(f"Acima: Altitude {altitude}m -> Temperatura {temperatura}°C")
print(f"Abaixo: Latitude {latitude}° reflete o mesmo padrão de variação")
