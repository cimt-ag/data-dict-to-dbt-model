from pathlib import Path


def find_path(targetName: str):
    currentPath: Path = Path(__file__).parent
    projectRoot: str = "data-dict-to-dbt-model"
    excludedFolders: set[str] = {"__pycache__", "venv", ".git"}
    while True:
        for path in currentPath.rglob("*"):
            if projectRoot in path.parts:
                if excludedFolders.intersection(path.parts):
                    continue
                if path.name == targetName:
                        return path
        if currentPath == currentPath.parent:
            break
        currentPath = currentPath.parent

def format_collection(valuesCollection: tuple, indentation: int = 2):
    rowPrefix: str = "\t" * indentation + "  - "
    return "\n".join([f"{rowPrefix}{value}" for value in valuesCollection])