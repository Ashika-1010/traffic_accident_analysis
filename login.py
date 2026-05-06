import customtkinter as ctk
from tkinter import messagebox


# ---------------- APP SETTINGS ---------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ---------------- LOGIN FUNCTION ---------------- #

def login():

    username = username_entry.get()
    password = password_entry.get()

    # Hardcoded credentials
    if username == "admin" and password == "1234":

        messagebox.showinfo("Login Successful", "Welcome to Smart Traffic Analysis System")

        app.destroy()

        # Open dashboard
        import splash_screen

        splash_screen.SplashScreen().mainloop()

    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")


# ---------------- MAIN WINDOW ---------------- #

app = ctk.CTk()

app.title("Login")

app.geometry("1200x700")


# ---------------- MAIN FRAME ---------------- #

main_frame = ctk.CTkFrame(
    app,
    width=500,
    height=500,
    corner_radius=20
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")


# ---------------- TITLE ---------------- #

title = ctk.CTkLabel(
    main_frame,
    text="🚦 Smart Traffic Accident Analysis",
    font=("Arial", 28, "bold")
)

title.pack(pady=(40, 10))


subtitle = ctk.CTkLabel(
    main_frame,
    text="Login to Continue",
    font=("Arial", 18)
)

subtitle.pack(pady=(0, 30))


# ---------------- USERNAME ---------------- #

username_entry = ctk.CTkEntry(
    main_frame,
    width=300,
    height=45,
    placeholder_text="Enter Username"
)

username_entry.pack(pady=15)


# ---------------- PASSWORD ---------------- #

password_entry = ctk.CTkEntry(
    main_frame,
    width=300,
    height=45,
    placeholder_text="Enter Password",
    show="*"
)

password_entry.pack(pady=15)


# ---------------- LOGIN BUTTON ---------------- #

login_button = ctk.CTkButton(
    main_frame,
    text="Login",
    width=300,
    height=45,
    font=("Arial", 18, "bold"),
    command=login
)

login_button.pack(pady=30)


# ---------------- LOGIN INFO ---------------- #

info = ctk.CTkLabel(
    main_frame,
    text="Username: admin    Password: 1234",
    font=("Arial", 14)
)

info.pack(pady=10)


# ---------------- RUN APP ---------------- #

app.mainloop()