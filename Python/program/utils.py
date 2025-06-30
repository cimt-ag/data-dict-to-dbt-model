from pathlib import Path


def find_path(targetName: str):
    currentPath: Path = Path(__file__).parent
    projectRoot = "data-dict-to-dbt-model"
    excludedFolders = {"__pycache__", "venv", ".git"}
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