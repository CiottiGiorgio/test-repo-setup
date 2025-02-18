import click

@click.command()
@click.argument("name")
def greeting(name):
    print(f"hello {name}")
