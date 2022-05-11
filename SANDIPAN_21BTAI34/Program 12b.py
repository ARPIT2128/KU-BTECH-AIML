tup =("heTay","uickqay","rownbay", "oxfay") 
index = 0
while index < len(tup):
    new = tup[ index ][ -3 ] + tup[ index ][0 : -3 ] 
    print (new, end = " ")
    index += 1
