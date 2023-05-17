# edad = 7

# if 0 < edad < 100:
#     print("Edad es correcta")

# else:
#     print("Edad incorecta")

salario = int(input("intruduce salario presedente"))
print(f"Salario presidente: {str(salario)}")

salario_1 = int(input("intruduce salario director"))
print(f"Salario director: {str(salario_1)}")

salario_2 = int(input("intruduce salario jefe area"))
print(f"Salario jefe area: {str(salario_2)}")

salario_3 = int(input("intruduce salario  administrativo"))
print(f"Salario administrativo: {str(salario_3)}")

if salario_3<salario_2<salario_1<salario:
    print("Todo funciona correctamente")
else:
    print("falta")