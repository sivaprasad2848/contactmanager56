from tabulate import tabulate
contacts=[('sam','sam@gmail.com','723767676'),('amal','amal@gmail.com','65236565')]
def menu():
    print("Contact Manager")
    print("1->Create New Contact")
    print("2->Display Contacts")
    print("3->Edit Contact")
    print("4->Delete Contact")
    opt=int(input("Enter Your Choice"))
    return opt
def create_contact():
    name=input("Enter Name")
    email=input("Enter Email")
    mobile=input("Enter Mobile")
    #print(name+" "+email+" "+mobile)
    contacts.append((name,email,mobile))
def display_contact():
    #print(contacts)
    table1=[]
    for item in contacts:
        #print(item[0]+" "+item[1]+" "+item[2])
        table1.append([item[0],item[1],item[2]])
    print(tabulate(table1, headers=['Name', 'Email','Mobile']))
def edit_contact():
    display_contact()
    i=int(input("Enter the record index you want to Edit "))  
    name=input("Enter New Name")
    email=input("Enter New Email")
    mobile=input("Enter New Mobile")
    contacts[i]=(name,email,mobile)
    display_contact()

def delete_contact():
    display_contact()
    i=int(input("Enter the record index you want to delete "))
    del contacts[i]
    display_contact()