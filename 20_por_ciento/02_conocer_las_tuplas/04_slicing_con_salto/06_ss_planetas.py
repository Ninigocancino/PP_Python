
planetas = ('Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno')


corte_1 = planetas[::2]
corte_2 = planetas[:3:2]
corte_3 = planetas[::-4]
corte_4 = planetas[:3:-2]

print(corte_1)
print(corte_2)
print(corte_3)
print(corte_4)