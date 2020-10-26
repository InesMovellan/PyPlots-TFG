fw=open("./escribir.txt","w")
texto = "ines es la mas guapa"
condicion=True 
for i in range(2,10):
	if condicion:
		fw.write(str(i)+"\n")
fw.close()
