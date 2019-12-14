image_example = [
         [1.00, 0.72, 0.56, 0.45],
         [0.92, 0.64, 0.48, 0.32],
         [0.80, 0.57, 0.42, 0.25],
         [0.73, 0.49, 0.35, 0.21]
              ]
def average_color(image,r, c):
    lis = []
    sum = 0
    for el in image:
        index1 = image.index(el) 
        for i in el: 
            index2 = el.index(i)
            #print(index2)
            if abs(index1 - r)<=1 and abs(index2 - c) <=1:
               # print (i)
                sum = sum + i
                lis.append(i)
    result = sum/len(lis)
    return result

#print(average_color(image_example,1,2))

def load_image(filename):
    f = open(filename, 'r')  
    g = f.readlines()
    for i in g :
        print(i)c 
        break 
        g.pop(0)
        g.append(list(i1))
    return g
print(load_image('image.txt'))

        