print("".center(35 , "-"))
print("Programa de impuestos".center(35, " "))
print("".center(35, "-"))

#><
def calcular_impuesto(estrato, cant_personas):
  """
  """
  if estrato == 1:

    if cant_personas <= 3:
      impuesto_persona = 10000
    else:
      impuesto_persona = 25000


  elif estrato == 2:
    if cant_personas <= 3:
      impuesto_persona = 15000
    else:
      impuesto_persona = 35000


  elif estrato == 3:
    if cant_personas <= 3:
      impuesto_persona = 20000
    else:
      impuesto_persona = 45000


  elif estrato == 4:
    if cant_personas <= 3:
      impuesto_persona = 25000
    else:
      impuesto_persona = 55000


  elif estrato == 5:
    if cant_personas <= 3:
      impuesto_persona = 30000
    else:
      impuesto_persona = 65000

  else:
    if cant_personas <= 3:
      impuesto_persona = 35000
    else:
      impuesto_persona = 75000

  return impuesto_persona * cant_personas

# ingresar los datos
total_impuesto_estrato = {}
while True:
  estrato = int(input("ingresa el estrato 1, 2, 3, 4, 5 0 6:--> "))
  cant_personas = int(input("ingresa el numero de personas--> "))

  impuesto = calcular_impuesto(estrato, cant_personas)

  # Acumular total por estrato
  if estrato not in total_impuesto_estrato:
    total_impuesto_estrato[estrato] = 0
  total_impuesto_estrato[estrato] += impuesto

  # dejar de registrar personas y salirse del ciclo
  respuesta = input("Desea continuar? s o n: ")
  if respuesta.lower() == "n":
    break

# imprimir los resultados
for estrato, total_impuesto in total_impuesto_estrato.items():
  print(f"Total impuesto del estrato {estrato} es: {total_impuesto}")
