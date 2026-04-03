import pandas as pd
from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from salarlens_predictor.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR / "SalaryLens-Predictor-de-Retorno-Laboral-con-Machine-Learning/data/raw/job_salary_prediction_dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    
):
    logger.info(f"Leyendo datos desde {input_path}...")

    # 1.- Verificar si el archivo existe antes de intentar leerlo
    if not input_path.exist():
        logger.error(f"Error, no se encontro el archivo en: {input_path}")
        return

    # 2.- Lectura del archivo
    df = pd.read_csv(input_path)

    # 3.- Mostrar informacion basica en los logs
    logger.info(f"Dataset cargado exitosamente. Filas: {df.shape}, columnas: {df.shape[1]}")




if __name__ == "__main__":
    app()
