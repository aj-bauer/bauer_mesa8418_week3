from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer
import pandas as pd

from config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    logger.info("Processing dataset...")

    # Read data
    df = pd.read_csv(input_path)

    # Drop shape_wlt column, which contains no data
    df = df.drop(columns="shape_wkt")

    # Drop harbor islands, which is missing data as well
    df = df[df["name"] != "Harbor Islands"]

    # Write data to output path  
    df.to_csv(output_path, index=False)
    
    logger.success("Processing dataset complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
