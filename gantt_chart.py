##########################################################################
# Gantt chart
#
# A Gantt chart is a type of bar chart that illustrates a schedule. We
# will prepare several functions which will help us to produce Gantt
# charts in ASCII art. Our charts will look like this:
#
# 0--------10--------20--------30--------40--------50
# |       ###### priprava       |         |         |
# |         |    ############# delo       |         |
# |         |         |    ################# zabava |
# 0--------10--------20--------30--------40--------50
##########################################################################



##########################################################################
# Write a function ruler(n) that takes an integer n and returns a "ruler"
# of size n. This is a string of length $n + 1$ that is composed mainly of
# characters '-'. Characters at indices that are multiples of 10 should
# be '0'. Then other digits should be added so that the integer sequence
# $0, 10, 20, 30, \ldots$ appears in the string. Example:
# 
#     >>> ruler(29)
#     '0--------10--------20--------3'
##########################################################################
def ruler(n):
    ruler = '0'
    num = 1
    for i in range(n+2):
        if len(ruler) == n+2:
            return ruler[0:n+1]
        elif (i+1) % 9 == 0:
            ruler += str(num)+'0'
            num += 1
        else:
            ruler += '-'
print(ruler(29))
#print(ruler(3))

##########################################################################
# Write a function task(task_name, a, b, n) that will produce a string which
# represents one line of the Gantt chart. This string should be of length
# $n + 1$ and mainly composed of characters ' ' (spaces), with character
# '|' at every index that is a multiple of 10. The substring from index
# a to index b (including a and b) should be composed of characters '#'.
# The last '#' should be followed by a space and then the name of the task.
# Example:
# 
#     >>> task('delo', 15, 27, 50)
#     '|         |    ############# delo       |         |'
#     '|         |    ############# delo       |         |'
##########################################################################
def task(task_name, a, b, n):
    task = ''
    i=0
    while i < (n+1):
        if i % 10 == 0:
            task += '|'
            i += 1
        elif i == a:
            for x in range(b-a+1):
                task += '#'
            task += ' '+ task_name
            i = i + (b-a+2+len(task_name))
        else:
            task += ' '
            i += 1
    return task

#print(task('delo', 15, 27, 50))

##########################################################################
# Write a function diagram(n, l) that takes an integer n and a list l.
# The function should print (and not return) the Gantt diagram of width n.
# Each element of the list l is a tuple of three elements: the name of
# the task, the starting index and the ending index. The diagram
# should contain len(l) + 2 lines (the first and the last line should be
# rulers). Example:
# 
#     >>> diagram(50, [('priprava', 8, 13), ('delo', 15, 27), ('zabava', 25, 41)])
#     0--------10--------20--------30--------40--------50
#     |       ###### priprava       |         |         |
#     |         |    ############# delo       |         |
#     |         |         |    ################# zabava |
#     0--------10--------20--------30--------40--------50
##########################################################################
def diagram(n, l):
    print(ruler(n))
    for i in l:
        print(task(i[0],i[1],i[2],n))
    print(ruler(n))

#diagram(50, [('priprava', 8, 13), ('delo', 15, 27), ('zabava', 25, 41)])
##########################################################################
# Write a function save_diagram(n, l, file_name) which takes three arguments:
# n and l are the same as in the previous task, and file_name is a string
# which contains a name of a file. The only difference between this and
# the previous function is that this function writes the output to the
# file named file_name. Example:
#
#     >>> save_diagram(50, [('priprava', 8, 13), ('delo', 15, 27), ('zabava', 25, 41)],
#                      'gantt_diagram.txt')
#
# Note: After this function call a file named gantt_diagram.txt should
# be created on the disk.
##########################################################################
def save_diagram(n, l, file_name):
    f = open(file_name,"w")
    s = ''
    s = s + ruler(n) + "\n"
    for i in l:
        s = s + task(i[0],i[1],i[2],n) + "\n"
    s += ruler(n)
    f.write(s)
    f.close()
#save_diagram(50, [('priprava', 8, 13), ('delo', 15, 27), ('zabava', 25, 41)],'gantt_diagram.txt')

