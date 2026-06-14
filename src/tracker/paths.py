from os import getenv
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

HAND_MODEL_URL = getenv("MODEL_URL")
PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_DIR = PROJECT_ROOT / "assets" / "models"
MODEL_PATH = MODEL_DIR / "hand_landmarker.task"


class ModelPath:

    @classmethod
    def get_model_path(cls):
        return MODEL_PATH

    @classmethod
    def get_model_url(cls):
        return HAND_MODEL_URL

    def __repr__(self):
        return MODEL_PATH
