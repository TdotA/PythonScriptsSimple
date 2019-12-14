import turtle as t 

def regular_polygon(n,a):
    angle = 360/n
    for i in range(n):
        t.fd(a)
        t.lt(angle)
      
t.clear
#regular_polygon(5,200)

def arbelos(a, k):
    r_2 = a/(2*k+2)
    r_1 = k*r_2
    t.fillcolor('red')
    t.begin_fill()
    t.lt(90)
    t.circle(-a/2, 180)
    t.rt(180)
    t.circle(r_2,180)
    t.rt(180)
    t.circle(r_1, 180)
    t.end_fill()
t.clear
#arbelos(300,2)

def comb(n):
    t.lt(270)
    leng = 100
    div = 20
    for i in range(n):
        t.fd(leng)
        t.lt(90)
        t.fd(div)
        t.lt(90)
        t.fd(leng)
        t.lt(180)
#comb(10)

def sun(n):
    r= 25
    t.fillcolor('yellow')
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    for i in range(n) :
        t.circle(r, 360/n)
        t.rt(90)
        t.fd(60)
        t.rt(180)
        t.fd(60)
        t.rt(90)
#sun(15)

def spiral(n, s):
    for i in range(s):
        t.fd(n)
        t.lt(90)
        n = n-6
#spiral(90, 12)

import math as m 
def nested_squareI(x, k):
    for i in range(k):
        for i in range(4):
            t.fd(x)
            t.lt(90)
        t.fd(x/2)
        t.lt(45)
        x = m.sqrt(x**2/2)
#nested_squareI(100,6)

def nested_square2(x, k, r):
    for i in range(k):
        for i in range(4):
            t.fd(x)
            t.lt(90)
        t.fd(x - x * r)
        c = m.sqrt((x*r)**2 + (x-x*r)**2)
        ang = m.degrees(m.asin((x-x*r)/c))
        t.rt(-ang)
        x = c 

def mb():
    t.fillcolor('black')
    t.begin_fill()
    t.circle(300)
    t.end_fill()
    t.fillcolor('white')
    t.begin_fill()
    
    t.circle(280)
    t.end_fill()

#mb()

import networkx as nx
import matplotlib.pyplot as plt
g1 = nx.petersen_graph()
nx.draw(g1)
plt.show()



