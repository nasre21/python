print("programa de becas")
distancia_d_escuela = int(input("Intruduce la distancia a la escuela en km"))
print(distancia_d_escuela)

numero_hermanas = int(input("Intruduce la n de hermanas en el centro"))
print(numero_hermanas)

salario_faamiliar = int(input("Intruduce la salario bruto"))
print(salario_faamiliar)

if distancia_d_escuela>40 and numero_hermanas>2 or salario_faamiliar<=20000:
    print("Tienes derecho a la beca")

else:
    print("no tienes")