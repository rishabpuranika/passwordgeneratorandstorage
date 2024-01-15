import random #importing random module to generate a random password

#defining a function to generate a random password
def generate(): 
    p=int(input("Enter the length of the password required: "))
        # Define character sets
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
    u = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
    s = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # Combine all character sets into one list
    passwd = []
    passwd.extend(l)
    passwd.extend(u)
    passwd.extend(s)
    passwd.extend(n)
    
    # Shuffle the combined list randomly
    random.shuffle(passwd)

    # Return the first p elements of the shuffled list
    password = "".join(passwd[0:p])
    print(password)
    f=input("Do you want to save the password(y or n):")
    if f.lower()=='y':
        save(password)
    else:
        main1()

#defining a function to save the password
def save(password):
    website = input("For which website is this password: ")
    file=input("Enter the type of file you want to save the password in: ")
    if file.lower() =="csv":
        a=input("Enter the name of the csv file: ")
        with open(a+".csv", 'a') as file2:
            file2.write(f"{website}:{password}\n")
            print("Password saved successfully")
    elif file.lower()=='bin':
        n=input("Enter the name of the bin file: ")
        with open(n+".bin", 'ab') as file1:
            file1.write(password.encode())
            print("Password saved successfully")


#defining a function to display the password
def display():
    a=input("Enter the type of file of which you want to be displayed:")
    d=input("Enter the file name of which you want to see the details:")
    if a=="csv":
        print("1.Read all\n2.Read specific")
        with open(d+".csv",'r') as file4:
            b=int(input("Enter the task to be executed: "))
            if b==1:
                print(file4.read())
            elif b==2:
                m=input("Enter the password of website to be found: ")
                for i in file4:
                    if m in i:
                        print(i,"\n")
            else:
                print("Enter from the given options")  
            print(file4.read())
    elif a=="bin":
        with open(d+".bin",'rb') as file6:
            print("1.Read all\n2.Read specific")
            b=int(input("Enter the task to be executed: "))
            if b==1:
                print(file6.read())
            elif b==2:
                m=input("Enter the password of website to be found: ")
                for i in file6:
                    if m in i:
                        print(i,"\n")
    else:
        print("Enter from the given options")

#defining a function to save the password by the user directly to the file
def save1():
    v=input("Enter the password you want to save: ")
    website = input("For which website is this password: ")
    file=input("Enter the type of file you want to save the password in: ")
    if file.lower() == "csv":
        j=input("Enter the name of the file: ")
        with open(j+".csv", 'a') as file:
            j.write(v)
            print("Password saved successfully")
    elif file.lower()=='bin':
        k=input("Enter the name of the file: ")
        with open(k+".bin", 'ab') as file4:
            file4.write(v.encode())
            print("Password saved successfully")

#defining a function to execute the program
def main1():
    print("1: Generate\n2: Save\n3: Display")
    e = int(input("Enter the task to be executed: "))
    if e == 1:
        password = generate()
        h=input("Do you want to generate another password? (Enter y or n): ")
        if h.lower() == "y":
            generate()
        else:
            pass
    elif e == 2:
        save1()
    elif e == 3:
        display()
    else:
        print("Enter from the given options")