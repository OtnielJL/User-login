#Creating and saving username and password under conditions
def passcheck():

    done = False
    while not done:
        pas = input("Please enter password\n")
        if len(pas)<8:
         print("Password must be atleast 8 characters")
        else:
         ul=0
         ll=0
         di=0
         sp=0
         s=0
         for char in pas:
              if char.isupper():
                  ul+=1
              elif char.islower():
                  ll+=1
              elif char.isdigit():
                  di+=1
              elif char.isspace():
                  sp+=1
              else:
                  s+=1
         if ul == 0:
             print("Password must have atleast one uppercase letter")
             input("Please enter Password again\n")
         elif ll == 0:
             print("Password must have atleast one lowercase letter")
             input("Please enter Password again\n")
         elif di == 0:
             print("Password must have atleast one digit")
             input("Please enter Password again\n")
         elif s == 0:
             print("Password must have atleast one special character")
             input("Please enter Password again\n")
         elif sp == 1:
             print("Password must not have white space")
             input("Please enter Password again\n")
         else:
            print("Your Password is created")
            done = True
    return pas


def usercheck():
    user = input ("Please choose username\n")
    while not (len(user)> 0 and len(user) < 26):
        user = input ("Username must be between 0 and 25 characters")
    return user
username = usercheck()
password = passcheck()

f = open("details.txt","w")
f.write(username+"\n")
f.write(password)
f.close()
