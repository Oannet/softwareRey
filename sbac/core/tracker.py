import os
import json
from rich import print

def add_file(filename, repo_path=".sbac"):
    index_path = os.path.join(repo_path, "index.json")

    if not os.path.isfile(filename):
        print(f"[bold red]Error:[/bold red] El archivo '{filename}' no existe.")
        return

    try:
        with open(index_path, "r", encoding="utf-8") as f:
            index = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        index = {"tracked_files": []}

    if filename in index["tracked_files"]:
        print(f"[bold yellow]Advertencia:[/bold yellow] El archivo '{filename}' ya está siendo rastreado.")
        return

    index["tracked_files"].append(filename)

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=4)

    print(f"[bold green]Archivo '{filename}' añadido al seguimiento.[/bold green]")
    
def show_status(repo_path=".sbac"):
    index_path = os.path.join(repo_path, "index.json")

    if not os.path.exists(index_path):
        print("[bold red]Error:[/bold red] No se encontró el índice de archivos.")
        return

    with open(index_path, "r", encoding="utf-8") as f:
        index = json.load(f)

    tracked = index.get("tracked_files", [])
    
    if not tracked:
        print("[bold yellow]No hay archivos rastreados actualmente.[/bold yellow]")
        return

    print("[bold cyan]Archivos actualmente rastreados:[/bold cyan]")
    for file in tracked:
        print(f"  • {file}")

