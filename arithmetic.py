import math 
def power_sum (k,n):
    sum = 0
    i = 1
    while i <= n:
        sum = sum + i**k
        i = i+1
    return sum 
#print (power_sum(10, 2))

def inverted_harmonic(x):
    sum = 0
    i = 1
    while sum < x : 
        sum = sum + 1/i
        i += 1
    return i-1
#print (inverted_harmonic(2))

def digit_sum(num):
    sum = 0
    for char in (str(num)) :
        sum = sum + int(char)
    return sum
#print(digit_sum(2013)) 

def hand_angle(h, m):
    
    if h > 12:
        h1 = (h - 12) * 5
    else :
        h1 = h * 5 
    if h1 > m :
        angle1 = (h1 - m + m/60) * 6 
        angle2 = (m + 60-h1 - m/60) * 6 
        angle_min = min(angle1, angle2)
    else: 
        angle1 = (m -h1 - m/60) * 6 
        angle2 = (h1 +  60-m + m/60) * 6
        angle_min = min(angle1, angle2)
        pass
    return math.floor(angle_min) ,  (angle_min-math.floor(angle_min)) * 60
print(hand_angle(17, 47))




    