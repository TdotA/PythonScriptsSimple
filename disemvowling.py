def disemvoweling (text) :
    vowels = ''
    i = 0
    while i < len(text) :
        if  text[i] in 'aeiouAEIOU' :
            vowels = vowels + text[i]
            text = text - text[i]
        i+=1
    return (text + vowels)
print (disemvoweling("Banana is good!"))

def first_vowel (word) :
    vow = ['a','e','i','o','u']
    for char in word : 
        if char in vow : 
            return char
print (first_vowel('hamburger'))