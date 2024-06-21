import tkinter as tk
from tkinter import messagebox

# Function to open the Register window
def open_register_window():
    register_window = tk.Toplevel(screen)
    register_window.title("Register")
    register_window.geometry("300x300")
    register_window.configure(bg='#f0f0f0')

    # Add Register form fields
    tk.Label(register_window, text="Username", bg='#f0f0f0').pack(pady=5)
    username_entry = tk.Entry(register_window)
    username_entry.pack(pady=5)

    tk.Label(register_window, text="Email", bg='#f0f0f0').pack(pady=5)
    email_entry = tk.Entry(register_window)
    email_entry.pack(pady=5)

    tk.Label(register_window, text="Password", bg='#f0f0f0').pack(pady=5)
    password_entry = tk.Entry(register_window, show='*')
    password_entry.pack(pady=5)

    tk.Label(register_window, text="Confirm Password", bg='#f0f0f0').pack(pady=5)
    confirm_password_entry = tk.Entry(register_window, show='*')
    confirm_password_entry.pack(pady=5)

    # Add a Submit button
    submit_button = tk.Button(register_window, text="Register", command=lambda: submit_register_form(username_entry, email_entry, password_entry, confirm_password_entry))
    submit_button.pack(pady=20)

# Function to open the Login window
def open_login_window():
    login_window = tk.Toplevel(screen)
    login_window.title("Login")
    login_window.geometry("300x200")
    login_window.configure(bg='#f0f0f0')

    # Add Login form fields
    tk.Label(login_window, text="Email", bg='#f0f0f0').pack(pady=5)
    email_entry = tk.Entry(login_window)
    email_entry.pack(pady=5)

    tk.Label(login_window, text="Password", bg='#f0f0f0').pack(pady=5)
    password_entry = tk.Entry(login_window, show='*')
    password_entry.pack(pady=5)

    # Add a Login button
    login_button = tk.Button(login_window, text="Login", command=lambda: submit_login_form(email_entry, password_entry))
    login_button.pack(pady=20)

# Function to handle Register form submission
def submit_register_form(username_entry, email_entry, password_entry, confirm_password_entry):
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not username or not email or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    # Here, you could add the logic to handle registration (e.g., save data to a database)
    messagebox.showinfo("Success", f"User {username} registered successfully!")
    username_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)

# Function to handle Login form submission
def submit_login_form(email_entry, password_entry):
    email = email_entry.get()
    password = password_entry.get()

    if not email or not password:
        messagebox.showerror("Error", "Both fields are required!")
        return

    # Here, you could add the logic to handle login (e.g., verify credentials)
    messagebox.showinfo("Success", f"User logged in with email {email}!")
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create main application window
screen = tk.Tk()

# Set window background color
screen['bg'] = '#27aae1'

# Set window title
screen.title('tops-admin')

# Set window icon
logo_path = 'images/logo.ico'
screen.iconbitmap(logo_path)

# Set window size
screen.geometry('400x400')

# Create a frame to hold the buttons
frame = tk.Frame(screen, bg='lightblue')
frame.place(relx=0.5, rely=0.5, anchor='center')

# Create "Register" and "Login" buttons
register_button = tk.Button(frame, text="Register", width=20, height=5, command=open_register_window)
login_button = tk.Button(frame, text="Login", width=20, height=5, command=open_login_window)

# Pack the buttons into the frame
register_button.pack(pady=(0, 10))  # Adds padding only below the button
login_button.pack(pady=(10, 0))     # Adds padding only above the button

screen.mainloop()
