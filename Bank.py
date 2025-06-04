accounts=[]
a=''
while a!='5':
    print("1. Create a new Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display account details")
    print("5. Exit")

    a=input("Choose (1 to 5): ")
    if a=='1':
        name=input("Store Name: ")
        number=input("Account Number: ")
        acc=0
        for i in accounts:
            if i['number']==number:
                acc='yes'

        if acc=='yes':
            print("Account number already exists")
        else:
            balance=float(input("Initial Balance: "))
            accounts.append({'name': name, 'number': number, 'balance': balance})
            print("Account created")

    elif a=='2':
        number=input("Account Number: ")
        for i in accounts:
            if i['number']==number:

                amount=float(input("Deposit Amount: "))
                if amount > 0:
                    i['balance'] += amount
                    print("Amount Deposited")
                else:
                    print("Enter positive number!")
            else:
                print("Account not available!")

    elif a=='3':
        number=input("Account Number: ")
        for i in accounts:
            if i['number']==number:
                amount=float(input("Withdraw Amount: "))
                if amount > 0:
                    if amount <= i['balance']:
                        i['balance'] -= amount
                        print("Amount Withdrawn")
                    else:
                        print("Not enough balance")
                else:
                    print("Enter positive number")
            else:
                print("Account not available")

    elif a=='4':
        number=input("Account Number: ")
        for i in accounts:
            if i['number']==number:
                print("Name:", i['name'])
                print("Account Number:", i['number'])
                print("Balance:", i['balance'])
            else:
                print("Account not available")

    elif a=='5':
        print("Exit")

    else:
        print("Invalid input")