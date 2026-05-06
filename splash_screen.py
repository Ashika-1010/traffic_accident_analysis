import customtkinter as ctk


# ---------------- SPLASH SCREEN ---------------- #

class SplashScreen(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.geometry("700x400")

        self.title("Loading...")

        self.configure(fg_color="#1a1a1a")

        self.overrideredirect(True)


        # ---------------- CENTER WINDOW ---------------- #

        screen_width = self.winfo_screenwidth()

        screen_height = self.winfo_screenheight()

        x = int((screen_width / 2) - (700 / 2))

        y = int((screen_height / 2) - (400 / 2))

        self.geometry(f"700x400+{x}+{y}")


        # ---------------- TITLE ---------------- #

        title = ctk.CTkLabel(
            self,
            text="🚦 Smart Traffic Accident\nAnalysis System",
            font=("Arial", 34, "bold"),
            text_color="#4da6ff"
        )

        title.pack(pady=(90, 20))


        # ---------------- SUBTITLE ---------------- #

        subtitle = ctk.CTkLabel(
            self,
            text="Loading Dashboard...",
            font=("Arial", 18),
            text_color="#cccccc"
        )

        subtitle.pack(pady=10)


        # ---------------- PROGRESS BAR ---------------- #

        self.progress = ctk.CTkProgressBar(
            self,
            width=400,
            height=20,
            progress_color="#2563eb"
        )

        self.progress.pack(pady=30)

        self.progress.set(0)


        # ---------------- START LOADING ---------------- #

        self.loading_value = 0

        self.after(100, self.load)


    # ---------------- LOADING FUNCTION ---------------- #

    def load(self):

        if self.loading_value < 1:

            self.loading_value += 0.02

            self.progress.set(self.loading_value)

            self.after(50, self.load)

        else:

            self.destroy()

            import dashboard