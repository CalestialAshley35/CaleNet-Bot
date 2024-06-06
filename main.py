install typer: pip install typer

import typer

app = typer.Typer()

@app.command()
def deez():
    typer.echo("nuts")

@app.command()
def rungpt():
    typer.echo("go to chat.openai.com")

@app.command()
def installCake():
    typer.echo("go to cake.com")

@app.command()
def google():
    typer.echo("go to google.com")

@app.command()
def replit():
    typer.echo("go to replit.com")

@app.command()
def youtube():
    typer.echo("go to youtube.com")

if __name__ == "__main__":
    app()
