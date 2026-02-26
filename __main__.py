import typer

app = typer.Typer()


@app.command()
def run():
    """Run the service."""
    print("Running airctl...")


@app.command()
def status():
    """Show status."""
    print("Airctl status: OK")


if __name__ == "__main__":
    app()
