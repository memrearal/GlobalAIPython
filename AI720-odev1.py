liste1 = [1,3,5,7,9]
liste2 = [0,2,4,6,8]
liste3 = liste1+liste2
liste3 = [int(i*2) for i in liste3]
for i in liste3:
	print(type(i))