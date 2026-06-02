valor=float(input("digite o valor a ser convertido:"))
origem=str(input('digite a moeda de origem:')).upper()
final=str(input('digite a moeda que sera entregue ')).upper()
taxas = {
    'USD': 1.0,  # Dólar americano
    'EUR': 6.20,  # Euro
    'GBP': 5.90,  # Libra esterlina (você tinha GPB, corrigi!)
    'BRL': 5.70,  # Real brasileiro
    'JPY': 149.50,  # Iene japonês
    'CAD': 1.36,  # Dólar canadense
    'AUD': 1.53,  # Dólar australiano
    'NZD': 1.40,  # Dólar neozelandês
    'ARS': 900.00,  # Peso argentino
    'MXN': 17.20,  # Peso mexicano
 }
if origem in taxas and final in taxas:
    taxa_origem = taxas[origem]
    taxa_final = taxas[final]
    resultado = (valor / taxa_origem) * taxa_final
    print(f'{valor} {origem} = {round(resultado, 2)} {final}')
else:
    print('moeda nao encontrada ')




