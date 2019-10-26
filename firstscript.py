import math
#ovo je moja "prva" skripta totalno
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c:'))
Age = int(input('Enter your age: '))
Name = input('Enter your name: ')




m = max(a,b) - min(a,b)
pl = a + b
pu = a * b
print(str(a) + ' ' + '+' + ' ' + str(b) + ' ' + '=' + ' ' + str(pl))
print(str(max(a,b)) + ' ' + '-' + ' ' + str(min(a,b)) + ' ' + '=' + ' ' + str(m))
print(str(a) + ' ' + '*' + ' ' + str(b) + ' ' + '=' + ' ' + str(pu))


if Name[len(Name)-1]== 'a' :
    gender = 'girl'
else : 
    gender = 'boy'
Place = 'Koper'

if Age>= 18 : 
   print ('Welcome to ' + Place + ',' + Name + ',you handsome' + gender + '!' )
else :
    print('Go back to highschool ' + Name + ', you filthy little' + gender) 

if Age <= 6 :
    print('Where are ur parents')
if 6 <= Age and Age <=18 :
   print('Go to highschool')
if 18<= Age and Age <=40 :
   print('Welcome!')
if Age >= 40 :
  print('Fuck off')


s = (a+b+c)/2
if a+b>c and a+c>b and b+c>a and max(b,c) - min(b,c)<a and max(b,a) - min(b,a) < c and max(a,c) - min(a,c) <b : 
    area = math.sqrt((s-a)*(s-b)*(s-c)*s)
    print('Area is: ' + str(area))
else : 
    print('not a triangle')
def Area_triangle ( a, b, c):
    s = (a+b+c)/2
    if a+b>c and a+c>b and b+c>a and max(b,c) - min(b,c)<a and max(b,a) - min(b,a) < c and max(a,c) - min(a,c) <b : 
        area = math.sqrt((s-a)*(s-b)*(s-c)*s)
        print('Area is: ' + str(area))
    else :     
        print('not a triangle')
Area_triangle(a, b, c)
i = 1
while i <= 100 :
    print (str(i) + '+' + str(i) + '=' + str(i+i))
    i+= 1

z = 0
for i in range(i, 11) :
    z = z+i**3
    print(str(c)) 



     
