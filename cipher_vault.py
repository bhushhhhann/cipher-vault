import json

key=123
pin=6969

def helper(passwords):
    
    with open("password_manager.txt","w") as file:
        json.dump(passwords,file,indent=4)

def load_passwords():
    
    try:
        with open("password_manager.txt","r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []

def list_all_saved_websites(passwords):
    
    for index,value in enumerate(passwords,start=1):
        print(f"{index}. Website : {value['website']} , Username : {value['username']} , Password : {value['password']}")

def add_new_password(passwords):
    
    website= input("Enter new Website : ")
    username= input("Enter new Username : ")
    password= pass_to_cipher(input("Enter new Password : "))
    passwords.append({"website":website,"username":username,"password":password})
    helper(passwords)

def update_password(passwords):
    
    list_all_saved_websites(passwords)
    
    while True:
        choice=int(input("Enter choice for updating Password  :"))
        if 1 <= choice <= len(passwords):
            oldPass=pass_to_cipher(input("Enter Old Password : "))
            if(passwords[choice-1]["password"]==oldPass):
                newPass=pass_to_cipher(input("Enter new Password : "))
                passwords[choice-1]["password"]=newPass
                break
            else :
                print("Enter Correct Old Password ! ")
        else :
            print("Enter valid Choice ! ")
        
    helper(passwords)

def delete_password(passwords):
    
    list_all_saved_websites(passwords)
    
    while True:
        choice=int(input("Enter choice for Deleting Password : "))
        if 1 <= choice <= len(passwords):
            del passwords[choice-1]
            break
        else:
            print("Enter valid Choice ! ")
            
    helper(passwords)

def Access_password(passwords):
    
    while True :
        p = int(input("Enter correct Pin : "))
        if p == pin:
            list_all_saved_websites(passwords)
            
            while True:
                choice=int(input("Enter choice for Accessing Password : "))
                if 1 <= choice <= len(passwords):
                    password=cipher_to_pass(passwords[choice-1]["password"],p)
                    print(f"Password for {passwords[choice-1]['username']} is {password} ")
                    return
                else :
                    print("Enter valid Choice ! ")       
        else :
            print("Enter a valid Pin ! ")

def pass_to_cipher(password):
    arr=[]
    for ch in password:
        arr.append(ord(ch) ^ key)
    return arr

def cipher_to_pass(cipher,p):
    if p == pin:
        arr=[]
        for i in cipher:
            arr.append(chr(i ^ key))
            
        return ("".join(arr))
    else:
        print("Incorrect PIN!")
        return None

def main():
    
    passwords = load_passwords()
    while True:
        print("\n Cipher Vault | Select a Valid Option")
        print("1. List All Saved Website Passwords")
        print("2. Add a New Password")
        print("3. Update an Existing Password")
        print("4. Delete a Password")
        print("5. Access (View) a Password")
        print("6. Exit the Program")
        print("\n")
        ip=str(input("Enter your Choice : "))
        
        match ip:
            case '1':
                list_all_saved_websites(passwords)
            case '2':
                add_new_password(passwords)
            case '3':
                update_password(passwords)
            case '4':
                delete_password(passwords)
            case '5':
                Access_password(passwords)
            case '6':
                break
            case _:
                print("Please Enter Valid Choice ! ")


if __name__ == "__main__":
    main()