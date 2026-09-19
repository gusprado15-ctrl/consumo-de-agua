print("Bem-vindo ao sistema de cálculo de consumo de água!")
#dados
tipoImovel = input("Digite o tipo de imóvel (casa, comercial, apartamento): ").strip().lower()
consumoAgua = int(input("Digite o consumo de água em metros cúbicos: "))
#cálculo do valor da conta de água
if tipoImovel == "comercial":
   print("Tarifa comercial aplicada – consulte o plano corporativo.")
if tipoImovel == "apartamento"and consumoAgua < 10:
   print("Consumo econômico – excelente controle de água!")
elif tipoImovel == "apartamento" or tipoImovel == "casa" and consumoAgua <= 25:
   print("Consumo moderado – dentro do padrão residencial.")
else:
   print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")