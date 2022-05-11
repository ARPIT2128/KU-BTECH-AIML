tup = ("The", "quick", "brown", "fox")
index = 0
while index < len(tup):
    new = tup[ index ][1 : ] + tup[ index ][ 0 ] + "ay"
    print (new, end = " ")
    index += 1
