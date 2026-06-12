import typer

from .capture.main import capture_cam

app = typer.Typer()


@app.command()
def run():
    """Run the service."""
    print("Waiting for capturing ")
    capture_cam()


@app.command()
def status():
    """Show status."""
    print("DEMO: Airctl status: OK")


if __name__ == "__main__":
    app()
