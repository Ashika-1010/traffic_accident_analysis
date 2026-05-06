import customtkinter as ctk
import pandas as pd
from tkinter import ttk


# ---------------- SEARCH FUNCTION ---------------- #

def search_records():

    # ---------------- WINDOW ---------------- #

    window = ctk.CTkToplevel()

    window.title("Search Accident Records")

    window.geometry("1400x750")

    window.configure(fg_color="#1a1a1a")


    # ---------------- LOAD DATASET ---------------- #

    df = pd.read_csv("dataset/indian_roads_dataset.csv")


    # ---------------- TITLE ---------------- #

    title = ctk.CTkLabel(
        window,
        text="🔍 Search Accident Records",
        font=("Arial", 30, "bold"),
        text_color="white"
    )

    title.pack(pady=20)


    # ---------------- SEARCH FRAME ---------------- #

    search_frame = ctk.CTkFrame(
        window,
        fg_color="transparent"
    )

    search_frame.pack(pady=10)


    # Search Entry
    search_entry = ctk.CTkEntry(
        search_frame,
        width=300,
        height=40,
        placeholder_text="Enter City Name..."
    )

    search_entry.pack(side="left", padx=10)


    # ---------------- TABLE FRAME ---------------- #

    table_frame = ctk.CTkFrame(
        window,
        fg_color="#262626",
        corner_radius=20
    )

    table_frame.pack(fill="both", expand=True, padx=20, pady=20)


    # ---------------- TREEVIEW STYLE ---------------- #

    style = ttk.Style()

    style.theme_use("default")


    style.configure(
        "Treeview",
        background="#2b2b2b",
        foreground="white",
        rowheight=28,
        fieldbackground="#2b2b2b",
        borderwidth=0,
        font=("Arial", 10)
    )


    style.map(
        "Treeview",
        background=[("selected", "#2563eb")]
    )


    style.configure(
        "Treeview.Heading",
        background="#1f538d",
        foreground="white",
        relief="flat",
        font=("Arial", 11, "bold")
    )


    # ---------------- TREEVIEW ---------------- #

    tree = ttk.Treeview(table_frame)

    tree.pack(side="left", fill="both", expand=True)


    # ---------------- SCROLLBARS ---------------- #

    scrollbar_y = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )

    scrollbar_y.pack(side="right", fill="y")


    scrollbar_x = ttk.Scrollbar(
        window,
        orient="horizontal",
        command=tree.xview
    )

    scrollbar_x.pack(fill="x")


    tree.configure(
        yscrollcommand=scrollbar_y.set,
        xscrollcommand=scrollbar_x.set
    )


    # ---------------- COLUMNS ---------------- #

    tree["columns"] = list(df.columns)

    tree["show"] = "headings"


    for col in df.columns:

        tree.heading(col, text=col)

        tree.column(col, width=130, anchor="center")


    # ---------------- DISPLAY FUNCTION ---------------- #

    def display_data(dataframe):

        # Clear Existing Data
        tree.delete(*tree.get_children())

        # Insert New Data
        for index, row in dataframe.iterrows():

            if index % 2 == 0:
                tag = "evenrow"
            else:
                tag = "oddrow"

            tree.insert(
                "",
                "end",
                values=list(row),
                tags=(tag,)
            )


    # ---------------- ROW COLORS ---------------- #

    tree.tag_configure(
        "evenrow",
        background="#2b2b2b"
    )

    tree.tag_configure(
        "oddrow",
        background="#242424"
    )


    # ---------------- SEARCH BUTTON FUNCTION ---------------- #

    def perform_search():

        city = search_entry.get().lower()

        filtered_df = df[
            df["city"].str.lower().str.contains(city)
        ]

        display_data(filtered_df.head(300))


    # ---------------- SEARCH BUTTON ---------------- #

    search_button = ctk.CTkButton(
        search_frame,
        text="Search",
        width=120,
        height=40,
        font=("Arial", 14, "bold"),
        fg_color="#2563eb",
        hover_color="#1d4ed8",
        command=perform_search
    )

    search_button.pack(side="left", padx=10)


    # ---------------- SHOW INITIAL DATA ---------------- #

    display_data(df.head(100))