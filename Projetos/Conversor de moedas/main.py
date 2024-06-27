cota_moeda_original = 5
cota_moeda_destino = 1

if cota_moeda_original > cota_moeda_destino:
    taxa = cota_moeda_original * cota_moeda_destino
else:
    taxa = cota_moeda_original / cota_moeda_destino

print(f'Taxa: {taxa}')

valor_moeda_origem = float(input('Digite o valor do moeda original: '))
valor_moeda_destino = valor_moeda_origem * taxa

print(f'Origem: {valor_moeda_origem}')

