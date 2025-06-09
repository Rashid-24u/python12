admin=["rashid"]
psward=["12345"]
user=[]
Library=[]
print("1. Admin \n2. User")
option=int(input("Select user type:"))
if option==1:
    uname=input("Enter the username: ")
    upsw=input("Enter the password: ")
    if uname in admin and upsw in psward:
        print("Welcome Admin Page\n")
        while True:
            print("\n--- Admin Menu ---")
            print("1. Add Book")
            print("2. Update Book")
            print("3. Delete Book")
            print("4. Display All Books")
            print("5. Exit")
            
            optn=input("Enter your choice: ")

            if optn=="1":
                b_id=input("Enter the Book id:")
                title=input("Enter the title:")
                author=input("Enter author name:")
                qnty=int(input("Enther the Quantity:"))
                Library.append([b_id,title,author,qnty])
                print("Book Added Successfully........")
    
            elif optn=="2":
                b_id=input("Enter the Book id to update: ")
                for i in Library:
                    if i[0]==b_id:
                        i[1]=input("Enter new Title: ")
                        i[2]=input("Enter new Author: ")
                        i[3]=int(input("Enter new Quantity: "))
                        print("Book Updated Successfully!")
                        break
                else:
                    print("Book id not found.")   

            elif optn=="3":
                b_id=input("Enter the Book id to delete: ")
                for i in Library:
                    if i[0]==b_id:
                        Library.remove(i)
                        print("Book Deleted Successfully!")
                        break
                else:
                    print("Book id not found.")

            elif optn=="4":
                if Library:
                    for i in Library:
                        print(i)
                else:
                    print("No books available.")

            elif optn=="5":
                print("Exiting Admin Menu.")
                break
            

            else:
                print("Invalid option. Please try again.")            

elif option==2:
    while True:
        print("\n--- User Menu ---")
        print("1. Registration")
        print("2. Login")
        print("3. Exit to Main Menu")
        choice=input("Enter your choice: ")

        if choice=="1":
            name=input("Enter your name: ")
            age=input("Enter your age: ")
            address=input("Enter your address: ")
            phone=input("Enter your phone number: ")
            username=input("Create a username: ")
            password=input("Create a password: ")
            if user:
                for usr in user:
                    if username==usr[4]:
                       print("Username already taken...")
                    elif phone==usr[3]:
                       print("Phone number already registered...")  
                    else:      
                       user.append([name,age,address,phone,username,password])
                       print("Registration successful!")
            else:
                user.append([name,age,address,phone,username,password])
                print("Registration successful!")               

        elif choice=="2":
            username=input("Enter your username: ")
            password=input("Enter your password: ")
            for u in user:
                if u[4]==username and u[5]==password:
                    print("login successfull")

                    while True:
                        print("\n--- User Menu ---")
                        print("1. Display All Book")
                        print("2. Search Book by Name")
                        print("3. Exit")    
                        select=input("Enter your option : ")  
            
                        if select=="1":
                            for i in Library:
                                print(i)

                        elif select=="2":
                            s_b=input("Enter name of the book: ")
                            
                            for book in Library:
                                if book[1].lower()==s_b.lower():
                                    print(book)
                                    break
                            else:
                                print("Book not found.")

                        elif select=="3":
                            print("Logging out....")
                            break
        


                else:
                    print("incorrect password or username")   

        elif choice=="3":         
            print("EXisting...")
            break            

else:
    print("Invalid option. Try again.")
 




            



