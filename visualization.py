import pandas as pd
import matplotlib.pyplot as plt
import os


# ---------------- CREATE EXPORT FOLDER ---------------- #

os.makedirs("exports", exist_ok=True)


# ---------------- SEVERITY ANALYSIS ---------------- #

def severity_analysis():

    # Load Dataset
    df = pd.read_csv("dataset/indian_roads_dataset.csv")

    # Count Severity Types
    severity_counts = df["accident_severity"].value_counts()

    # ---------------- BAR CHART ---------------- #

    plt.figure(figsize=(8, 6))

    colors = ["#22c55e", "#f59e0b", "#ef4444"]

    plt.bar(
        severity_counts.index,
        severity_counts.values,
        color=colors
    )

    plt.title(
        "Accident Severity Distribution",
        fontsize=18,
        fontweight="bold"
    )

    plt.xlabel("Severity Type", fontsize=14)

    plt.ylabel("Number of Accidents", fontsize=14)

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.savefig(
        "exports/severity_bar_chart.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    # ---------------- PIE CHART ---------------- #

    plt.figure(figsize=(7, 7))

    plt.pie(
        severity_counts.values,
        labels=severity_counts.index,
        autopct="%1.1f%%",
        colors=colors,
        startangle=90
    )

    plt.title(
        "Severity Percentage Distribution",
        fontsize=18,
        fontweight="bold"
    )

    plt.savefig(
        "exports/severity_pie_chart.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ---------------- WEATHER ANALYSIS ---------------- #

def weather_analysis():

    # Load Dataset
    df = pd.read_csv("dataset/indian_roads_dataset.csv")

    # Count Weather Types
    weather_counts = df["weather"].value_counts()

    # ---------------- BAR CHART ---------------- #

    fig, ax = plt.subplots(figsize=(9, 6))

    fig.patch.set_facecolor("#1e1e1e")
    ax.set_facecolor("#2b2b2b")

    colors = ["#38bdf8", "#64748b", "#2563eb"]

    bars = ax.bar(
        weather_counts.index,
        weather_counts.values,
        color=colors,
        width=0.6
    )

    ax.set_title(
        "Weather-wise Accident Distribution",
        fontsize=20,
        fontweight="bold",
        color="white",
        pad=20
    )

    ax.set_xlabel(
        "Weather Condition",
        fontsize=14,
        color="white"
    )

    ax.set_ylabel(
        "Number of Accidents",
        fontsize=14,
        color="white"
    )

    ax.tick_params(colors="white")

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.3
    )

    for spine in ax.spines.values():
        spine.set_visible(False)

    for bar in bars:

        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width()/2,
            height + 50,
            f"{height}",
            ha="center",
            color="white",
            fontsize=12,
            fontweight="bold"
        )

    plt.tight_layout()

    plt.savefig(
        "exports/weather_bar_chart.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    # ---------------- PIE CHART ---------------- #

    plt.figure(figsize=(7, 7))

    plt.pie(
        weather_counts.values,
        labels=weather_counts.index,
        autopct="%1.1f%%",
        colors=colors,
        startangle=90
    )

    plt.title(
        "Weather Condition Percentage",
        fontsize=18,
        fontweight="bold"
    )

    plt.savefig(
        "exports/weather_pie_chart.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ---------------- CITY ANALYSIS ---------------- #

def city_analysis():

    df = pd.read_csv("dataset/indian_roads_dataset.csv")

    city_counts = df["city"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 6))

    fig.patch.set_facecolor("#1e1e1e")
    ax.set_facecolor("#2b2b2b")

    bars = ax.barh(
        city_counts.index,
        city_counts.values,
        color="#3b82f6"
    )

    ax.set_title(
        "Top Accident-Prone Cities",
        fontsize=22,
        fontweight="bold",
        color="white",
        pad=20
    )

    ax.set_xlabel(
        "Number of Accidents",
        fontsize=14,
        color="white"
    )

    ax.set_ylabel(
        "Cities",
        fontsize=14,
        color="white"
    )

    ax.tick_params(colors="white")

    ax.grid(
        axis="x",
        linestyle="--",
        alpha=0.3
    )

    for spine in ax.spines.values():
        spine.set_visible(False)

    for bar in bars:

        width = bar.get_width()

        ax.text(
            width + 20,
            bar.get_y() + bar.get_height()/2,
            f"{width}",
            va="center",
            color="white",
            fontsize=11,
            fontweight="bold"
        )

    plt.tight_layout()

    plt.savefig(
        "exports/city_analysis.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ---------------- TIME ANALYSIS ---------------- #

def time_analysis():

    df = pd.read_csv("dataset/indian_roads_dataset.csv")

    hour_counts = df["hour"].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(11, 6))

    fig.patch.set_facecolor("#1e1e1e")
    ax.set_facecolor("#2b2b2b")

    ax.plot(
        hour_counts.index,
        hour_counts.values,
        color="#38bdf8",
        linewidth=3,
        marker="o",
        markersize=8
    )

    ax.fill_between(
        hour_counts.index,
        hour_counts.values,
        color="#38bdf8",
        alpha=0.2
    )

    ax.set_title(
        "Accidents by Hour of the Day",
        fontsize=22,
        fontweight="bold",
        color="white",
        pad=20
    )

    ax.set_xlabel(
        "Hour of Day",
        fontsize=14,
        color="white"
    )

    ax.set_ylabel(
        "Number of Accidents",
        fontsize=14,
        color="white"
    )

    ax.tick_params(colors="white")

    ax.grid(
        linestyle="--",
        alpha=0.3
    )

    for spine in ax.spines.values():
        spine.set_visible(False)

    peak_hour = hour_counts.idxmax()
    peak_value = hour_counts.max()

    ax.scatter(
        peak_hour,
        peak_value,
        color="#ef4444",
        s=120,
        zorder=5
    )

    ax.text(
        peak_hour,
        peak_value + 30,
        f"Peak: {peak_hour}:00",
        color="white",
        fontsize=12,
        ha="center",
        fontweight="bold"
    )

    plt.tight_layout()

    plt.savefig(
        "exports/time_analysis.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ---------------- TRAFFIC DENSITY ANALYSIS ---------------- #

def traffic_density_analysis():

    df = pd.read_csv("dataset/indian_roads_dataset.csv")

    traffic_counts = df["traffic_density"].value_counts()

    fig, ax = plt.subplots(figsize=(9, 6))

    fig.patch.set_facecolor("#1e1e1e")
    ax.set_facecolor("#2b2b2b")

    colors = ["#ef4444", "#f59e0b", "#22c55e"]

    bars = ax.bar(
        traffic_counts.index,
        traffic_counts.values,
        color=colors,
        width=0.6
    )

    ax.set_title(
        "Traffic Density vs Accident Frequency",
        fontsize=20,
        fontweight="bold",
        color="white",
        pad=20
    )

    ax.set_xlabel(
        "Traffic Density",
        fontsize=14,
        color="white"
    )

    ax.set_ylabel(
        "Number of Accidents",
        fontsize=14,
        color="white"
    )

    ax.tick_params(colors="white")

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.3
    )

    for spine in ax.spines.values():
        spine.set_visible(False)

    for bar in bars:

        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width()/2,
            height + 50,
            f"{height}",
            ha="center",
            color="white",
            fontsize=12,
            fontweight="bold"
        )

    plt.tight_layout()

    plt.savefig(
        "exports/traffic_density_analysis.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ---------------- ROAD TYPE ANALYSIS ---------------- #

def road_type_analysis():

    df = pd.read_csv("dataset/indian_roads_dataset.csv")

    road_counts = df["road_type"].value_counts()

    fig, ax = plt.subplots(figsize=(8, 8))

    fig.patch.set_facecolor("#1e1e1e")
    ax.set_facecolor("#2b2b2b")

    colors = ["#3b82f6", "#22c55e", "#f59e0b"]

    wedges, texts, autotexts = ax.pie(
        road_counts.values,
        labels=road_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=colors,
        textprops={"color": "white", "fontsize": 12}
    )

    centre_circle = plt.Circle(
        (0, 0),
        0.65,
        fc="#2b2b2b"
    )

    fig.gca().add_artist(centre_circle)

    ax.set_title(
        "Road Type Accident Distribution",
        fontsize=22,
        fontweight="bold",
        color="white",
        pad=20
    )

    plt.tight_layout()

    plt.savefig(
        "exports/road_type_analysis.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ---------------- CASUALTIES ANALYSIS ---------------- #

def casualties_analysis():

    df = pd.read_csv("dataset/indian_roads_dataset.csv")

    casualties = df["casualties"]

    fig, ax = plt.subplots(figsize=(9, 6))

    fig.patch.set_facecolor("#1e1e1e")
    ax.set_facecolor("#2b2b2b")

    ax.hist(
        casualties,
        bins=10,
        color="#ef4444",
        edgecolor="white",
        alpha=0.85
    )

    ax.set_title(
        "Casualties Distribution Analysis",
        fontsize=22,
        fontweight="bold",
        color="white",
        pad=20
    )

    ax.set_xlabel(
        "Number of Casualties",
        fontsize=14,
        color="white"
    )

    ax.set_ylabel(
        "Frequency",
        fontsize=14,
        color="white"
    )

    ax.tick_params(colors="white")

    ax.grid(
        linestyle="--",
        alpha=0.3
    )

    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()

    plt.savefig(
        "exports/casualties_analysis.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ---------------- RISK SCORE ANALYSIS ---------------- #

def risk_score_analysis():

    df = pd.read_csv("dataset/indian_roads_dataset.csv")

    risk_scores = df["risk_score"]

    avg_risk = risk_scores.mean()

    fig, ax = plt.subplots(figsize=(10, 6))

    fig.patch.set_facecolor("#1e1e1e")
    ax.set_facecolor("#2b2b2b")

    ax.hist(
        risk_scores,
        bins=15,
        color="#3b82f6",
        edgecolor="white",
        alpha=0.85
    )

    ax.axvline(
        avg_risk,
        color="#ef4444",
        linestyle="--",
        linewidth=3,
        label=f"Average Risk = {avg_risk:.2f}"
    )

    ax.set_title(
        "Risk Score Distribution",
        fontsize=22,
        fontweight="bold",
        color="white",
        pad=20
    )

    ax.set_xlabel(
        "Risk Score",
        fontsize=14,
        color="white"
    )

    ax.set_ylabel(
        "Frequency",
        fontsize=14,
        color="white"
    )

    ax.tick_params(colors="white")

    ax.grid(
        linestyle="--",
        alpha=0.3
    )

    for spine in ax.spines.values():
        spine.set_visible(False)

    legend = ax.legend()

    for text in legend.get_texts():
        text.set_color("white")

    plt.tight_layout()

    plt.savefig(
        "exports/risk_score_analysis.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()