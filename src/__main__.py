import typer

from src.capture.main import capture_cam

app = typer.Typer()


@app.command()
def run():
    """Run the service."""
    # Check MediaPipe installation
    try:
        import mediapipe as mp

        print("MediaPipe is installed. Version:", mp.__version__)
    except ImportError:
        print("MediaPipe is not installed. Please install it to run the service.")
        return
    # Check MediaPipe Holistic model
    try:
        mp_holistic = mp.solutions.holistic
        print("MediaPipe Holistic model is available.")
    except AttributeError:
        # Download Model if not available
        print("MediaPipe Holistic model is not available. Downloading...")
        mp_holistic = mp.solutions.holistic
    print("Waiting for capturing ")
    capture_cam()


@app.command()
def status():
    """Show status."""
    print("DEMO: Airctl status: OK")


if __name__ == "__main__":
    app()
