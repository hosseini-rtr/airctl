import typer
from dotenv import load_dotenv

from src.capture.main import capture_cam
from src.tracker.hand_tracker import hand_tracker
from src.tracker.model_manager import ModelManager
from src.tracker.paths import ModelPath

load_dotenv()

app = typer.Typer()


@app.command()
def run():
    try:

        """Run the service."""
        print("Waiting for capturing ")
        print(ModelPath.get_model_path(), ModelPath.get_model_url())
        ModelManager.get_model()
        hand_tracker()
        # capture_cam()
    finally:
        print("finished!")


@app.command()
def status():
    """Show status."""
    print("DEMO: Airctl status: OK")


if __name__ == "__main__":
    app()
