import time
import json
import os

superuser={'user': 'admin', 'password': 'admin'}

# Create Member
def create_member():
    member={}
    print('Enter details:-')
    fname = input("Full name::")
    age=int(input("Age::"))
    gender=input("Gender::")
    phone = int(input("Phone number::"))
    email = input("Email id::")
    BMI = float(input("BMI::"))
    dur = int(input("Membership duration(1,3,6 or 12)::"))
    with open('regimen.json') as json_file:
        data = json.load(json_file)
    
    if BMI < 18.5:
        reg=data['1']
    elif BMI < 18.5:
        reg=data['2']
    elif BMI < 18.5:
        reg=data['3']
    else:
        reg=data['4']
        
    res=input('Regimen auto assigned. Do you wanna change it(yes or no)::')
    if res == 'yes':
        view_regimen()
        n = input('Enter regimen no to assign::')
        reg=data[n]
    
    filesize = os.path.getsize("member.json")
    if filesize == 0:
        l=0
    else:    
        with open('member.json') as fo:
            member = json.load(fo)
            l=len(member)

    member[l+1]={'Full name':fname,'Age':age,'Gender':gender,'Mobile':phone,'Email':email,'BMI':BMI,'Regimen':reg,'Duration':dur}
    with open("member.json","w") as fi:
        json.dump(member,fi)
    print("Member added successfully :)")

# View Member
def view_member():
    temp = int(input('Enter moblie no of member::'))
    with open('member.json') as fo:
        data = json.load(fo)

    flag=-1
    for i in range(1,len(data)+1):
        if data[str(i)]['Mobile'] == temp:
            index=i
            flag=1
            break

    if flag==1:
        print('*******************************')
        print('Name:',data[str(index)]['Full name'])
        print('Age:',data[str(index)]['Age'])
        print('Gender:',data[str(index)]['Gender'])
        print('Mobile',data[str(index)]['Mobile'])
        print('Email',data[str(index)]['Email'])
        print('BMI',data[str(index)]['BMI'])
        print('Membership months:',data[str(index)]['Duration'])
        print('Regimen:-')
        print('Mon:',data[str(index)]['Regimen']['Mon'])
        print('Tue:',data[str(index)]['Regimen']['Tue'])
        print('Wed:',data[str(index)]['Regimen']['Wed'])
        print('Thu:',data[str(index)]['Regimen']['Thu'])
        print('Fri:',data[str(index)]['Regimen']['Fri'])
        print('Sat:',data[str(index)]['Regimen']['Sat'])
        print('Sun:',data[str(index)]['Regimen']['Sun'])
        print('*******************************')
    else:
        print('Member not found')
    time.sleep(2)

# Delete Member
def delete_member():
    temp = int(input('Enter moblie no of member::'))
    with open('member.json') as fo:
        data = json.load(fo)

    flag=-1
    for i in range(1,len(data)+1):
        if data[str(i)]['Mobile'] == temp:
            index=i
            flag=1
            break

    if flag==1:
        for i in range (int(index),len(data)):
            data[str(i)]=data[str(i+1)]
        print("Member removed successfully :)")

        print("Updating file now...")
        time.sleep(2)
        del data[str(len(data))]
        with open("member.json","w") as fi:
            json.dump(data,fi)
        print("File update successful")
    else:
        print('Member not found')
        time.sleep(2)
    

# Update Member
def update_member():
    temp = int(input('Enter moblie no of member::'))
    with open('member.json') as fo:
        data = json.load(fo)

    flag=-1
    for i in range(1,len(data)+1):
        if data[str(i)]['Mobile'] == temp:
            index=i
            flag=1
            break

    if flag==1:
        res = input('Membership (extend or invoke)::')
        if res == 'extend':
            temp1 = int(input('Enter the months to be added::'))
            data[str(index)]['Duration']+=temp1
            print('Membership extended :)')
        elif res == 'invoke':
            data[str(index)]['Duration']=0
            print('Membership invoked :)')
        else:
            print("Invalid input!!!")
            update_member()
            
        with open("member.json","w") as fi:
            json.dump(data,fi)
        
    else:
        print('Member not found')
    time.sleep(2)


# Create Regime
def create_regimen():
    print('Enter routine:-')
    mon = input("Mon::")
    tue = input("Tue::")
    wed = input("Wed::")
    thu = input("Thu::")
    fri = input("Fri::")
    sat = input("Sat::")
    sun = input("Sun::")
    
    with open('regimen.json') as fo:
        data = json.load(fo)

    data[len(data)+1]={'Mon': mon, 'Tue': tue, 'Wed': wed,'Thu': thu, 'Fri': fri, 'Sat': sat, 'Sun': sun}
    with open("regimen.json","w") as fi:
        json.dump(data,fi)
    print("Regimen added successfully :)")
    time.sleep(2)


# View Regime
def view_regimen(): 
    with open('regimen.json') as fo:
        data = json.load(fo)

        for i in range(1,len(data)+1):
            print(i,data[str(i)])
    time.sleep(2)
    

# Delete Regime
def delete_regimen():
    view_regimen()
    with open('regimen.json') as fo:
        data = json.load(fo)
    res = input("Enter regimen no to delete::")
    if int(res)>0 and int(res)<5:
        print('This is a default regimen. Deletion not allowed.')
        return
    else:
        x = data.keys()
        if res in x:
            for i in range (int(res),len(data)):
                data[str(i)]=data[str(i+1)]
            print("Regimen removed successfully :)")

            print("Updating file now...")
            time.sleep(2)
            del data[str(len(data))]
            with open("regimen.json","w") as fi:
                json.dump(data,fi)
            print("File update successful")

        else:
            print('Regimen no not fount!!!')
    time.sleep(2)
    
# Update Regime
def update_regimen():
    view_regimen()
    with open('regimen.json') as fo:
        data = json.load(fo)
    res = input("Enter regimen no to update::")
    if int(res)>0 and int(res)<5:
        print('This is a default regimen. Updation not allowed.')
        return
    else:
        x = data.keys()
        if res in x:
            print('Enter routine:-')
            mon = input("Mon::")
            tue = input("Tue::")
            wed = input("Wed::")
            thu = input("Thu::")
            fri = input("Fri::")
            sat = input("Sat::")
            sun = input("Sun::")
            data[res]={'Mon': mon, 'Tue': tue, 'Wed': wed,'Thu': thu, 'Fri': fri, 'Sat': sat, 'Sun': sun}
            with open("regimen.json","w") as fi:
                json.dump(data,fi)
            print('Regimen update successful :)')
            
        else:
            print('Regimen no not fount!!!')
    time.sleep(2)


# Superuser Panel
def member_panel(mno):
    with open('member.json') as fo:
        data = json.load(fo)

    flag=-1
    for i in range(1,len(data)+1):
        if data[str(i)]['Mobile'] == mno:
            index=i
            flag=1
            break

    if flag==1:
        print("\nChoose Your Option")
        print("1. My regimen")
        print("2. My profile")
        print("3. Go back")
        print("4. Exit")
        choice = int(input("Enter your choice(1-4)::"))
        if choice == 1:
            print('*******************************')
            print('Mon:',data[str(index)]['Regimen']['Mon'])
            print('Tue:',data[str(index)]['Regimen']['Tue'])
            print('Wed:',data[str(index)]['Regimen']['Wed'])
            print('Thu:',data[str(index)]['Regimen']['Thu'])
            print('Fri:',data[str(index)]['Regimen']['Fri'])
            print('Sat:',data[str(index)]['Regimen']['Sat'])
            print('Sun:',data[str(index)]['Regimen']['Sun'])
            print('*******************************')
        elif choice == 2:
            print('*******************************')
            print('Name:',data[str(index)]['Full name'])
            print('Age:',data[str(index)]['Age'])
            print('Gender:',data[str(index)]['Gender'])
            print('Mobile',data[str(index)]['Mobile'])
            print('Email',data[str(index)]['Email'])
            print('BMI',data[str(index)]['BMI'])
            print('Membership months:',data[str(index)]['Duration'])
            print('*******************************')
        elif choice == 3:
            main()
        elif choice == 4:
            print("Now terminating the program...")
            time.sleep(2)
            quit()
        else:
            print("Invalid input!!!")
        time.sleep(2)
        member_panel(mno)
    else:
        print('Member not found')



# Superuser Panel
def superuser_panel():
    print("\nChoose Your Option")
    print("1. Create Member")
    print("2. View Member")
    print("3. Delete Member")
    print("4. Update Member")
    print("5. Create Regimen")
    print("6. View Regimen")
    print("7. Delete Regimen")
    print("8. Update Regimen")
    print("9. Go back")
    print("10. Exit")
    choice = int(input("Enter your choice(1-10)::"))

    if choice == 1:
        create_member()
    elif choice == 2:
        view_member()
    elif choice == 3:
        delete_member()
    elif choice == 4:
        update_member()
    elif choice == 5:
        create_regimen()
    elif choice == 6:
        view_regimen()
    elif choice == 7:
        delete_regimen()
    elif choice == 8:
        update_regimen()
    elif choice == 9:
        main()
    elif choice == 10:
        print("Now terminating the program...")
        time.sleep(2)
        quit()

    else:
        print("Invalid input!!!")
    time.sleep(2)
    superuser_panel()


# Check Id aand password validity for Admin
def superuser_check():
    uname = input("Enter your username::")
    pwd = input("Enter your password::")
    flag = -1
    
    if superuser['user'] == uname and superuser['password'] == pwd:
        flag = 1
        
    if flag == -1:
        print("Wrong credentials!!!")
        superuser_check()
    return flag


# Main function
def main():
    usertype = input("Who are you (super user or member) or exit::")

    # Admin type
    if usertype == 'super user':
        flag = int(superuser_check())
        if flag == 1:
            print("Login Successful...")
            superuser_panel()

    elif usertype == 'member':
        temp = int(input('Enter your mobile no::'))
        member_panel(temp)

    elif usertype == 'exit':
        print("Now terminating the program...")
        time.sleep(2)
        quit()

    else:
        print("Invalid input!!!\nPlease try again...")
    time.sleep(2)
    main()


# Start of Food Ordering App
print("*****WECLOME TO GYM MEMBERSHIP APP*****")
main()