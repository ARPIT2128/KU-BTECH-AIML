str = input ("Enter the Word :- ")
letter = input ("Enter a letter to count :- ") 
count = 0
for i in str :
    if i == letter :
        count += 1
print ("Number of letter :- ", count )
