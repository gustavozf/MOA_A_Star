import sys

media1 = media2 = 0.0
i =  0
arq = open(sys.argv[1], 'r')
arq.readline()
for linhas in arq:
	numeros = linhas.split("\t")
	numeros = [x for x in numeros if x]
	#print(numeros)	
	media1+= float(numeros[0][:-1])
	media2+= float(numeros[2][:-2])
	i+=1

print("Media da Memoria: "+ str(media1/i))
print("Media da CPU: " + str(media2/i))
