import typer

app = typer.Typer()


@app.command()
def run():
    """Run the service."""
    print("DEMO: Running Airctl...")


@app.command()
def status():
    """Show status."""
    print("DEMO: Airctl status: OK")


if __name__ == "__main__":
    app()
