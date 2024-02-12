import math
height = float(input("Height:"))
base1 = float(input('Base, first value:'))
base2 = float(input('Base, second value:'))
answer = math.prod([math.fsum([base1,base2]) , 0.5 , height])
print('Expected output: ' + str(answer))