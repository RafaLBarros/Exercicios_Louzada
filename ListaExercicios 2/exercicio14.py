from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()


    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(b, end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
