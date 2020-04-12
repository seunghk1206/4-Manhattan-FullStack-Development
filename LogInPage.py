from tkinter import *
import os #operating system
def register_user(): # regiser 버튼 

    username_info = username.get() # username 의 값을 가져옴
    password_info = password.get()

    if len(password_info) >= 8:
        file = open(username_info, "w") #[username_info].txt - > youngho.txt, file의 권한 = w -> Write
        file.write(username_info)
        file.write("\n") #new line
        file.write(password_info)
        file.close()

        username_entry.delete(0,END)
        password_entry.delete(0,END)

        Label(screen1, text = "Registration Successful", fg = "green", font = ("Calibri", 13)).pack()
    else:
        password_entry.delete(0,END)
        Label(screen1, text = "The password has to be more than 8 digits!", fg = "red", font = ("Calibri", 13)).pack()

def login_user():
    
    username_info = username_verify.get() # username 의 값을 가져옴
    password_info = password_verify.get()

    list_of_files = os.listdir()
    if username_info in list_of_files:
        file = open(username_info, 'r')
        verify = file.read().splitlines()#처음에 정렬되지 않은 리스트를 스페이스 다 없에고 ENTER 한거 다 없에서 하나의 값으로 나열
        if password_info in verify:
            print('logged in')
            print('loading game')
            import ManhattanPractice
        else:
            print('password is not correct')
    else:
        print("username not found")
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

def register():
    global screen1
    screen1 = Toplevel(screen) #screen으로 인한 새로운 페이지
    screen1.title("Register")
    screen1.geometry("300x250")
    screen1.title("Mahattan Project Login Page")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter your info below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen) #screen으로 인한 새로운 페이지
    screen2.title("login")
    screen2.geometry("300x350")
    screen2.title("Mahattan Project Login Page")
    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text = "").pack()
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Button(screen2, text = "login", width = 10, height = 1, command = login_user).pack()

def login_page():
    global screen
    screen = Tk()
    screen.geometry("300x350")
    screen.title("Mahattan Project Login Page")
    Label(text = "Manhattan Project Login Page", bg = "grey", width = 300, height = 2, font = ("calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", width = 30, height = 2, command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", width = 30, height = 2, command = register).pack()

    screen.mainloop()

login_page()