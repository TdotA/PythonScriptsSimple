i = 1
c = '012'
def toString(List): 
	return ''.join(List)

def permute (s, f, l):
    b =[]
    if l==f: 
        b = b.append(toString(s))
        print(b[3])
            
    else: 
        for i in xrange(f, l+1):

            s[f], s[i] = s[i], s[f]
            permute(s, f+1, l)
            s[f], s[i] = s[i], s[f]
        
        
        
    
a = list(c)
n = len(c)
permute(a, 0, n-1)
