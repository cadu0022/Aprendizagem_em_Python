
def aplicar_desconto(valor):
   return valor * 0.90
  

def aplicar_taxa(valor):
    return valor * 0.95
    

total = 100 

total = aplicar_desconto(total)
total = aplicar_taxa(total)
print(total)