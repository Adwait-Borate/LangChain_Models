import langchain
from importlib.metadata import version, PackageNotFoundError

try:
    print(langchain.__version__)
except Exception:
    try:
        print(version("langchain"))
    except PackageNotFoundError:
        print("langchain version not found")