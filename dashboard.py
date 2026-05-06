from dataset_view import open_dataset_window
from search_records import search_records

from visualization import (
    severity_analysis,
    weather_analysis,
    city_analysis,
    time_analysis,
    traffic_density_analysis,
    road_type_analysis,
    casualties_analysis,
    risk_score_analysis
)

import customtkinter as ctk
import pandas as pd


# ---------------- APP SETTINGS ---------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ---------------- LOAD DATASET ---------------- #

df = pd.read_csv("dataset/indian_roads_dataset.csv")


# ---------------- DASHBOARD METRICS ---------------- #

total_accidents = len(df)

states_covered = df["state"].nunique()

avg_risk_score = round(df["risk_score"].mean(), 2)

weather_types = df["weather"].nunique()


# ---------------- MAIN WINDOW ---------------- #

dashboard = ctk.CTk()

dashboard.title("Smart Traffic Accident Analysis System")

dashboard.geometry("1550x920")

dashboard.configure(fg_color="#1a1a1a")


# ---------------- SIDEBAR ---------------- #

sidebar = ctk.CTkFrame(
    dashboard,
    width=270,
    fg_color="#111111",
    corner_radius=0
)

sidebar.pack(side="left", fill="y")


# ---------------- APP TITLE ---------------- #

logo = ctk.CTkLabel(
    sidebar,
    text="🚦 Traffic Analyzer",
    font=("Arial", 24, "bold"),
    text_color="#4da6ff"
)

logo.pack(pady=(18, 12))


# ---------------- BUTTON FRAME ---------------- #

button_frame = ctk.CTkFrame(
    sidebar,
    fg_color="transparent"
)

button_frame.pack(pady=5)


# ---------------- BUTTONS ---------------- #

buttons = [
    "🏠 Dashboard",
    "📂 View Dataset",
    "📊 Severity Analysis",
    "☁️ Weather Analysis",
    "🏙️ City Analysis",
    "⏰ Time Analysis",
    "🚦 Traffic Density",
    "🛣️ Road Type Analysis",
    "🚑 Casualties Analysis",
    "📉 Risk Score Analysis",
    "🔍 Search Records"
]


# ---------------- CREATE BUTTONS ---------------- #

for btn in buttons:

    btn_command = None

    # ---------------- FUNCTIONALITY ---------------- #

    if btn == "📂 View Dataset":
        btn_command = open_dataset_window

    elif btn == "📊 Severity Analysis":
        btn_command = severity_analysis

    elif btn == "☁️ Weather Analysis":
        btn_command = weather_analysis

    elif btn == "🏙️ City Analysis":
        btn_command = city_analysis

    elif btn == "⏰ Time Analysis":
        btn_command = time_analysis

    elif btn == "🚦 Traffic Density":
        btn_command = traffic_density_analysis

    elif btn == "🛣️ Road Type Analysis":
        btn_command = road_type_analysis

    elif btn == "🚑 Casualties Analysis":
        btn_command = casualties_analysis

    elif btn == "📉 Risk Score Analysis":
        btn_command = risk_score_analysis

    elif btn == "🔍 Search Records":
        btn_command = search_records


    # ---------------- CREATE BUTTON ---------------- #

    button = ctk.CTkButton(
        button_frame,
        text=btn,
        width=230,
        height=38,
        corner_radius=14,
        font=("Arial", 13, "bold"),
        fg_color="#2563eb",
        hover_color="#1d4ed8",
        command=btn_command
    )

    button.pack(pady=4)


# ---------------- EXIT BUTTON ---------------- #

exit_button = ctk.CTkButton(
    sidebar,
    text="❌ Exit",
    width=230,
    height=38,
    corner_radius=14,
    font=("Arial", 13, "bold"),
    fg_color="#dc2626",
    hover_color="#b91c1c",
    command=dashboard.destroy
)

exit_button.pack(side="bottom", pady=15)


# ---------------- MAIN AREA ---------------- #

main_frame = ctk.CTkFrame(
    dashboard,
    fg_color="#1a1a1a",
    corner_radius=0
)

main_frame.pack(side="right", fill="both", expand=True)


# ---------------- TITLE ---------------- #

title = ctk.CTkLabel(
    main_frame,
    text="Smart Traffic Accident Analysis Dashboard",
    font=("Arial", 28, "bold"),
    text_color="white"
)

title.pack(pady=(20, 5))


subtitle = ctk.CTkLabel(
    main_frame,
    text="Real-time Insights from Indian Road Accident Data",
    font=("Arial", 16),
    text_color="#aaaaaa"
)

subtitle.pack(pady=(0, 20))


# ---------------- CARDS FRAME ---------------- #

cards_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)

cards_frame.pack(pady=10)


# ---------------- CARD DATA ---------------- #

card_info = [

    ("🚗 Total Accidents",
     f"{total_accidents:,}",
     "#2563eb"),

    ("📍 States Covered",
     f"{states_covered}",
     "#16a34a"),

    ("⚠ Avg Risk Score",
     f"{avg_risk_score}",
     "#dc2626"),

    ("🌦 Weather Types",
     f"{weather_types}",
     "#ca8a04")
]


# ---------------- CREATE CARDS ---------------- #

for text, value, color in card_info:

    card = ctk.CTkFrame(
        cards_frame,
        width=220,
        height=120,
        corner_radius=20,
        fg_color=color
    )

    card.pack(side="left", padx=15)

    card.pack_propagate(False)

    label1 = ctk.CTkLabel(
        card,
        text=text,
        font=("Arial", 16, "bold"),
        text_color="white"
    )

    label1.pack(pady=(22, 8))

    label2 = ctk.CTkLabel(
        card,
        text=value,
        font=("Arial", 28, "bold"),
        text_color="white"
    )

    label2.pack()


# ---------------- ANALYTICS FRAME ---------------- #

analytics_frame = ctk.CTkFrame(
    main_frame,
    width=1100,
    height=390,
    corner_radius=25,
    fg_color="#262626"
)

analytics_frame.pack(pady=30)

analytics_frame.pack_propagate(False)


# ---------------- ANALYTICS TITLE ---------------- #

analytics_title = ctk.CTkLabel(
    analytics_frame,
    text="📈 Traffic Accident Insights",
    font=("Arial", 28, "bold"),
    text_color="#4da6ff"
)

analytics_title.pack(pady=(22, 12))


# ---------------- DESCRIPTION ---------------- #

desc = ctk.CTkLabel(
    analytics_frame,
    text="Analyze Indian road accident patterns using powerful visualizations.",
    font=("Arial", 16),
    text_color="#dddddd"
)

desc.pack(pady=(0, 15))


# ---------------- INSIGHT TEXT ---------------- #

analytics_text = ctk.CTkLabel(
    analytics_frame,
    text=(
        "✔ Severity Distribution Analysis\n"
        "✔ Weather Condition Impact\n"
        "✔ City-wise Accident Trends\n"
        "✔ Peak Traffic Hours\n"
        "✔ Casualty Statistics\n"
        "✔ Visibility & Risk Score Insights\n"
        "✔ Traffic Density Analysis\n"
        "✔ Road Type Distribution\n"
        "✔ Risk Score Distribution\n"
        "✔ Smart Search & Filtering"
    ),
    font=("Arial", 15),
    justify="left",
    text_color="#eeeeee"
)

analytics_text.pack()


# ---------------- FOOTER ---------------- #

footer = ctk.CTkLabel(
    main_frame,
    text="Developed using Python • CustomTkinter • Pandas • Matplotlib",
    font=("Arial", 12),
    text_color="#777777"
)

footer.pack(side="bottom", pady=10)


# ---------------- RUN APP ---------------- #

dashboard.mainloop()