install typer: pip install typer

import typer

app = typer.Typer()

@app.command()
def version():
    typer.echo("the latest version is 0.0.1")

@app.command()
def Rungpt():
    typer.echo("go to chat.openai.com")

@app.command()
def Content_Store():
    typer.echo("Replit = python main.py replit, google = python main.py google, youtube = python main.py youtube")

@app.command()
def google():
    typer.echo("go to google.com")

@app.command()
def replit():
    typer.echo("go to replit.com")

@app.command()
def youtube():
    typer.echo("go to youtube.com")

@app.command()
def about():
    typer.echo("CaleNet Bot is Developed by Calestial Ashley")
    
@app.command()
def language():
    typer.echo("Currently Have English And Using English")

if __name__ == "__main__":
    app()
