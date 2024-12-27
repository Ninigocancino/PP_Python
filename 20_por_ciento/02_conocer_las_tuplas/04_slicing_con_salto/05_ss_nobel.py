
ganadores_nobel = "Albert Einstein","Niels Bohr","Richard Feynman","Stephen Hawking","Roger Penrose","Marie Curie","Linus Pauling","Dorothy Crowfoot Hodgkin","Frederick Sanger","Ada Yonath","Frances Arnold","Alexander Fleming","Jonas Salk","Barbara McClintock","James D. Watson","Susumu Tonegawa","Tu Youyou","Rabindranath Tagore","William Faulkner","Gabriel García Márquez","Toni Morrison","Bob Dylan","Olga Tokarczuk","Nelson Mandela","Madre Teresa de Calcuta","Malala Yousafzai","Barack Obama","Denis Mukwege","Tawakkol Karman"

c_nobel = len(ganadores_nobel)

corte_1 = ganadores_nobel[0::2]
corte_2 = ganadores_nobel[0:9:2]
corte_3 = ganadores_nobel[::-2]

print(c_nobel)
print(corte_1)
print(corte_2)
print(corte_3)