import pyrebase 

firebaseConfig = {
  'apiKey': "AIzaSyAq9PXaK2yBv5WJPCxN2ftYsIS6xmEJMTQ",
  'authDomain': "glassboilerplate.firebaseapp.com",
  'projectId': "glassboilerplate",
  'storageBucket': "glassboilerplate.firebasestorage.app",
  'messagingSenderId': "1059418877993",
  'appId': "1:1059418877993:web:39af816079c772b8822c38"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def login(): 
    print("Log in...")
    email= input("Enter email: ")
    password = input("Enter password: ")
    try: 
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
    except: 
        print("Invalid email or password")
    return 

def signup(): 
    print("Sign up...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try: 
        user = auth.create_user_with_email_and_password(email, password)
    except:
        print("Email already exists")
    return

ans = input("Are you a new user?[y/n]") 

if ans == 'n':
    login()
elif ans == 'y':
    signup()