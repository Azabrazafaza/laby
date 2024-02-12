import math
number = float(input('Input number of sides: '))
length = float(input('Input the length of a side: '))
area = math.prod(([number , pow(length , 2)])) / math.prod([4 , math.tan(math.pi/number) ])
print('The area of the polygon is: {}'.format(round(area)))