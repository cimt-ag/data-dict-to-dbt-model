from pathlib import Path


def find_path(modelsFolder: str):
    currentPath: Path = Path(__file__).parent
    excludedFolders = {"__pycache__", "venv", ".git"}
    while True:
        for path in currentPath.rglob("*"):
            if not path.is_dir() or excludedFolders.intersection(path.parts):
                continue
            if path.name == modelsFolder:
                    return path
        if currentPath == currentPath.parent:
            break
        currentPath = currentPath.parent