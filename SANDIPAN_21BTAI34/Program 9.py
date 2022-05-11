dic = {'Rahul' : "2002",
       'Nabarun' : "2001",
       'Anushka' : "2002",
       'Diya' : "2003",
       'Rohit' : "2002",
       'Sandipan' : "2001",
       'Ayush' : "2006",
       'Arpit' : "2007",
       'Srijib' : "2005",
       'Shivangi' : "2004" }

username = input("Enter username :- ")

if username in dic :
    password = input("Enter password :- ")
    if dic[username] == password :
        print ("You are now logged into the system.")
    else :
        print ("Invalid password.")
else :
    print ("You are not valid user.")
