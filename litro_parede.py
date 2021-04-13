largura = float(input("Qual a largura da parede: "))
altura = float(input("Qual a altura da parede: "))
area = largura * altura
tinta = area / 2

print(f"Sua parede tem a dimensão de {largura} por {altura} e a área é de {area:.3}m² ")
print(f"A quantidade de tinta nescessária para pintar essa parede é de {tinta:.3} litros")


