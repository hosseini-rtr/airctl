from os import getenv
from urllib.request import urlretrieve

from src.tracker.paths import HAND_MODEL_URL, MODEL_DIR, MODEL_PATH, ModelPath


class ModelManager:
    def __init__(self, model=MODEL_PATH):
        self.model = model

    @classmethod
    def get_model(cls):
        model_url = getenv("MODEL_URL")
        if model_url:
            if MODEL_PATH.exists():
                print(f"Model already exists at {MODEL_PATH}")
                return cls().model
        MODEL_DIR.mkdir(parents=True, exist_ok=True)

        print("Downloading model...")

        urlretrieve(HAND_MODEL_URL, MODEL_PATH)

        print(f"Model saved at {MODEL_PATH}")

        return MODEL_PATH
