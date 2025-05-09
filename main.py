from helper import *
y=0
while(y==0):
    op=menu()
    if(op==1):
        create_contact()
    if(op==2):
        display_contact()
    if(op==3):
        edit_contact()
    if(op==4):
        delete_contact()
    y=int(input("Do you want to continue?press 0 for Yes"))
    if(y!=0):
        save_data()
