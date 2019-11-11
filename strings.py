def emphasise(title):
    emphasised = ''
    for char in title: 
        emphasised = emphasised + char.upper() + ' '
    return emphasised
print(emphasise('jjajjj'))  

def emphasise_marked(text):
    s1 = s2 = '*'
    return text.replace((text.split(s1)[1].split(s2)[0]).upper(), (text.split(s1)[1].split(s2)[0]))
print(emphasise_marked('Breaking *news* on Donald *Trump*'))
