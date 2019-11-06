import porta

#######################################################
f = porta.fechadura.Fechadura(1234)
f.trancar(1234)
#print(f)

p = porta.Porta(210)
p.setCor('Azul')
p.abrir()
p.fechar()
p.instalar(f)

print(p)
