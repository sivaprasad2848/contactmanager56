contacts=[]
y=0
while(y==0):
    print("Contact Manager")
    print("1->For Create New Contact")
    print("2->For Display Contacts")
    print("3->For Edit Contact")
    print("4->For Delete Contact")
    opt=int(input("Enter Your Choice"))
    if(opt==1):
        name=input("Enter Name")
        email=input("Enter Email")
        mobile=input("Enter Mobile")
        #print(name+" "+email+" "+mobile)
        contacts.append((name,email,mobile))
    if(opt==2):
        #print(contacts)
        for item in contacts:
            print(item[0]+" "+item[1]+" "+item[2])
    y=int(input("Do you want to continue?press 0 for Yes"))