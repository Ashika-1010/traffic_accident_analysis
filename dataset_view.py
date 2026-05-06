import customtkinter as ctk
import pandas as pd
from tkinter import ttk


# ---------------- FUNCTION ---------------- #

def open_dataset_window():

    # ---------------- WINDOW ---------------- #

    window = ctk.CTkToplevel()

    window.title("Dataset Viewer")

    window.geometry("1450x750")

    window.configure(fg_color="#1a1a1a")


    # ---------------- LOAD DATASET ---------------- #

    df = pd.read_csv("dataset/indian_roads_dataset.csv")


    # ---------------- TITLE ---------------- #

    title = ctk.CTkLabel(
        window,
        text="📂 Indian Road Accident Dataset",
        font=("Arial", 30, "bold"),
        text_color="white"
    )

    title.pack(pady=(20, 10))


    # ---------------- STATS FRAME ---------------- #

    stats_frame = ctk.CTkFrame(
        window,
        fg_color="#262626",
        corner_radius=20,
        height=80
    )

    stats_frame.pack(fill="x", padx=20, pady=10)


    total_records = len(df)
    total_states = df["state"].nunique()
    avg_risk = round(df["risk_score"].mean(), 2)


    stats_text = (
        f"📊 Total Records: {total_records}      "
        f"📍 States: {total_states}      "
        f"⚠ Avg Risk Score: {avg_risk}"
    )


    stats_label = ctk.CTkLabel(
        stats_frame,
        text=stats_text,
        font=("Arial", 18, "bold")
    )

    stats_label.pack(pady=20)


    # ---------------- SEARCH FRAME ---------------- #

    search_frame = ctk.CTkFrame(
        window,
        fg_color="transparent"
    )

    search_frame.pack(fill="x", padx=20, pady=10)


    search_entry = ctk.CTkEntry(
        search_frame,
        width=300,
        height=40,
        placeholder_text="Search by City..."
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
        rowheight=30,
        fieldbackground="#2b2b2b",
        bordercolor="#343638",
        borderwidth=0,
        font=("Arial", 11)
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
        font=("Arial", 12, "bold")
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


    # ---------------- HEADINGS ---------------- #

    for col in df.columns:

        tree.heading(col, text=col)

        tree.column(col, width=140, anchor="center")


    # ---------------- INSERT DATA ---------------- #

    for index, row in df.head(300).iterrows():

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