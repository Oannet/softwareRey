import click
from sbac.core.repo import init_repo
from sbac.core.tracker import add_file  # <- si usas función en vez de clase

@click.group()
def cli():
    pass

@cli.command()
def init():
    """Inicializa un nuevo repositorio SBAC."""
    init_repo()

@cli.command()
@click.argument('archivo')
def add(archivo):
    """Añade un archivo al seguimiento."""
    add_file(archivo)

@cli.command()
def status():
    """Muestra el estado actual de archivos rastreados."""
    from sbac.core.tracker import show_status
    show_status()

