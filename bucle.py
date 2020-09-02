ccs = input("Enter your ccs: ")

cc1=ccs[0:28]
cc2=ccs[28:56]
cc3=ccs[56:84]
cc4=ccs[84:112]
cc5=ccs[112:140]
cc6=ccs[140:168]
cc7=ccs[168:196]
cc8=ccs[196:224]
cc9=ccs[224:252]
cc10=ccs[252:280]

listaccs=[]
listaccs.append(cc1)
listaccs.append(cc2)
listaccs.append(cc3)
listaccs.append(cc4)
listaccs.append(cc5)
listaccs.append(cc6)
listaccs.append(cc7)
listaccs.append(cc8)
listaccs.append(cc9)
listaccs.append(cc10)
listaa=[]
for i in range(10):
	ccx=listaccs[i]
	listaa.append(ccx.split("|", 29))
print()

for i in range(10):
	for x in range(4):
		if x==0:
			Num=listaa[i][x]
			pass
		if x==1:
			Mes=listaa[i][x]
			pass
		if x==2:
			Ano=listaa[i][x]
			pass
		if x==3:
			cvv=listaa[i][x]
			pass
	print('Numero', Num, 'Mes', Mes, 'Año', Ano,'Cvv', cvv)