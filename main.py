import customtkinter as ctk

# App Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main Window
app = ctk.CTk()

app.title("Smart Traffic Accident Analysis System")

app.geometry("1200x700")

# Title
title = ctk.CTkLabel(
    app,
    text="🚦 Smart Traffic Accident Analysis System",
    font=("Arial", 30, "bold")
)

title.pack(pady=40)

# Subtitle
subtitle = ctk.CTkLabel(
    app,
    text="Indian Road Accident Analytics Dashboard",
    font=("Arial", 18)
)

subtitle.pack(pady=10)

# Run App
app.mainloop()