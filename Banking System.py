import csv
import random                   #8
"""
# Example Database format             #11
database = {'333 333 333':{'name':'Mg Mg','password':'123456','amount':5000}
            '444 444 444':{'name':'Kyaw Kyaw','password':'456789','amount':8000}
            }
"""
database = {}            #10



def home():                 #5
    print('         Welcome to Banking System') #1
    print('        *****************************')
    return (input('1. Create account\n2. Account Login\n Give your option: '))  #2

def menu():                #16
    return (input('1. Check Balance\n2.Deposit\n3. Withdraw\n4.Exit \nGive your option: '))

def create_acc():                  #7
    name = input('Name: ')
    password = input('Password: ')
    confirm_password = input('Confirmed Password: ')
    while password != confirm_password:
        print('Your password did not match. Please try again!')
        password = input('Password: ')
        confirm_password = input('Confirmed Password: ')

    account_no = random.randrange(100000000, 1000000000)
    while account_no in database:                #14
        account_no = random.randrange(100000000, 1000000000)      #15

    database[account_no] = {}                       #12
    database[account_no]['name'] = name              #13
    database[account_no]['password'] = password
    database[account_no]['amount'] = 0
    print('Your account No :',account_no)
    print('Your account has been registered.')
    print('#####################')
    # menu()                      #17  #26




# __________________________________________________________________________________
status = home()                   #6
while status != 'OFF':               #6

    if status == '1':               #3
        create_acc()                 #9
    # ____________________________________________________________________


    elif status == '2':                 #4
        user_acc = int(input('Enter your account number: '))     #18
        if user_acc not in database:               #19
            print('your account is not registered')

            user_option = int(input('1. Create an account\n2. Exit?\n Give your option:'))
            if user_option == 1:
                create_acc()


        else:                                     #20
            password = input('Enter your password: ')
            while database[user_acc]['password'] != password:
                print('Your password is wrong, please try again!')
                password = input('Enter your password: ')

        user_option = menu()    #21

        while user_option != '4':              #27
            if user_option == '1':               #23
                print('Balance :', database[user_acc]['amount'])

            elif user_option == '2':               #24
                deposit_amount = int(input('Enter amount to deposit: '))
                database[user_acc]['amount'] += deposit_amount
                print('Balance :', database[user_acc]['amount'])

            elif user_option == '3':               #25
                withdraw_amount = int(input('Enter amount to withdraw: '))
                while withdraw_amount > database[user_acc]['amount']:     #26
                    print('Your balance is not insufficient.')
                    print('Balance :', database[user_acc]['amount'])
                    withdraw_amount = int(input('Enter amount to withdraw: '))

                database[user_acc]['amount'] -= withdraw_amount
                print('Balance :', database[user_acc]['amount'])


            print('________________________')
            user_option = menu()

    else:                                     #22
        print('Invalid Option! You must be choice option 1 or 2.')

    print('-------------------------------------------------------------')

    status = home()

print(database)          #23

with open('blank_database.csv','w',newline='') as file:       #28
    database_csv = csv.writer(file)
    database_csv.writerow(['Account No', 'Name', 'Password', 'Balance Amount'])
    for acc in database:
        database_csv.writerow([acc,database[acc]['name'],database[acc]['password'],database[acc]['amount']])
