def anonymize_data(data):
    # Sustituir cada carácter por 'X' para anonimizar los datos
    anonymized_data = 'X' * len(data)
    return anonymized_data

numero_tarjeta_credito = input('Ingrese numero tarjeta de credito\n')

anonimizacion = anonymize_data(numero_tarjeta_credito)

print(anonimizacion)