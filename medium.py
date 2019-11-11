import time


def number_of_holes(num) :
    holes = 0; 
    for i in range(len(str(num)) - 1):
        digit = num % 10 
        if digit == 0 or digit == 4 or digit == 6 or digit == 9 or digit == 0 :
            holes = holes + 1
        elif digit == 8:
            holes = holes + 2
        else:
            holes = holes
        num = int(str(num)[:-1])
    return holes


#print(number_of_holes(5348))

def find_divisors(num): #utility function for finding and summing divisors of numbers; will be used later
    divisors = [] 
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
        else:
            pass
    return sum(divisors)
#print(find_divisors(284))

def amicable(num) :
    i = 1
    while i <= num : 
        a = find_divisors(i)
        b=find_divisors(find_divisors(i))
        if (i == b) and (i < a) :
            print (str(i) + ' ' + str(i))
        else: 
            pass
        i = i+1
print(amicable(10000))


print(after - now)

def list_to_str (lists): #utility function
    string = ''
    for element in lists:
        string = string + element
    return string

def auto_numbering(s) : 
    i = 1 
    l = list(s)
    for char in s:
        if char == "#" :
            l[l.index(char)] = str(i)
            i = i + 1
        else :
            pass
    return list_to_str(l)
    
#print(auto_numbering ("I saw # cow, # rabitts and # mice!"))

def multiplication_table(num):
    for i in range(1, num+1):
        print('\n')
        for j in range (1, (num + 1)):
            print(i*j, end=' ')
            j = j+1
        i=i+1
#multiplication_table(5)

def All_Alphabetical (string):
    new = ""
    for char in string:
        if char.isalpha() :
            new = new + char 
        else:
            pass
    return new

def is_palindromic_sentence(sentence) :
    
    allAlphabetic= All_Alphabetical(sentence)
    noSpace = allAlphabetic.replace(" ","")
    reverse = noSpace[::-1]
    if reverse.lower() == noSpace.lower() :
        return True
    else :
        return False 
#print(is_palindromic_sentence("Ana voli milovana!"))
