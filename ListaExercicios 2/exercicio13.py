file = "dados.txt"
stream = open(file, mode = 'r',encoding = 'utf-8')
line = stream.readline()
count = 0
while line != '':
    count+=1
    print(line,end = '')
    line = stream.readline()
print("\nO arquivo possui",count,"linhas.")