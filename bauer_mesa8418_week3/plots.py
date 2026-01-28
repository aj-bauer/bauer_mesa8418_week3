from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer
import pandas as pd
import altair as alt

from config import FIGURES_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    output_path: Path = FIGURES_DIR / "plot.png",
    # -----------------------------------------
):
    logger.info("Generating plot from data...")
    
    # Import data
    df = pd.read_csv(input_path)

    # Generate % Pop below Poverty level
    df["percent_below_pov"] = df["income_b17001_002e"] / df["population_b03002_001e"] * 100

    # Generate bar graph
    chart = alt.Chart(df, title="Boston Neighborhood Poverty Levels").mark_bar().encode(
        x = alt.X('name:N').title(None),
        y = alt.Y('percent_below_pov:Q').title("% Population Below Poverty Level"),
        color = alt.Color('percent_below_pov').scale(scheme="purples").legend(None)
    ).properties(
        width = 600,
        height = 400,
        padding=20
    ).configure_axisBottom(
        labelAngle = -45,
        labelFontSize = 12
    ).configure_axisLeft(
        titleFontSize = 16,
        labelFontSize = 12,
        titlePadding = 15
    ).configure_title(
        fontSize = 20,
        offset = 20
    )

    # Save chart
    chart.save(output_path)

    logger.success("Plot generation complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
