from logica import calcular_valores, punicao_arvore, punicao_credito




energia_gasta = 300
gasolina_gasta = 40
gas_gasto = 30
carro_gasto = 50
moto_gasto = 80
onibus_gasto = 90

total = calcular_valores(energia_gasta, gasolina_gasta, gas_gasto, carro_gasto, moto_gasto, onibus_gasto)


print(f"Seu valor gasto foi de {total:.2f} KG de C02, voce pode pagar {punicao_credito(total):.2f} em creditos de carbono, ou plantar {punicao_arvore(total)} mudas de arvores.")