import os
from pathlib import Path
import logging
from itertools import chain
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="HOTEL_RESERVATIONS"

# Group files by responsibility
#A. Source code
#B. Infrastructure
#C. Config
#D. Other type

#✅ A. Source Code Files
Source_File =[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "main.py"
    "app.py"
]

# ✅ B. Infrastructure / Packaging Files
INFRA_FILES = [
    "requirements.txt",
    "Dockerfile",
    "setup.py",
]

#✅ C. Configuration Files
CONFIG_FILES = [
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
]

#✅ D. Other Files
OTHER_FILES = [
    ".github/workflows/.gitkeep",
    "research/research.ipynb",
    "templates/index.html",
]


#ALL_FILES = SOURCE_FILES + INFRA_FILES + CONFIG_FILES + OTHER_FILES
ALL_FILES = list(chain(Source_File,INFRA_FILES,CONFIG_FILES,OTHER_FILES))  #using  from itertools import chain

def write_minimal_content(path: Path) -> None:
    """
    Write minimal valid content for critical files.
    Non-critical files are created as empty placeholders.

    This function is only called when the file does NOT already exist
    (so it won't overwrite your work).
    """
    if path.name == "Dockerfile":
        path.write_text(
            "FROM python:3.11-slim\n"
            "WORKDIR /app\n"
            "COPY requirements.txt .\n"
            "RUN pip install --no-cache-dir -r requirements.txt\n"
            "COPY . .\n"
            'CMD ["python", "app.py"]\n'
        )

    elif path.name == "requirements.txt":
        path.write_text(
            "# Add project dependencies here\n"
            "# Example:\n"
            "# numpy\n"
            "# pandas\n"
        )

    elif path.name == "setup.py":
        path.write_text(
            "from setuptools import setup, find_packages\n\n"
            "setup(\n"
            f'    name="{project_name}",\n'
            "    version='0.0.1',\n"
            "    packages=find_packages(where='src'),\n"
            "    package_dir={'': 'src'},\n"
            ")\n"
        )

    elif path.suffix == ".py":
        # Optional: tiny placeholder for python files (safe + valid)
        if path.name == "app.py":
            path.write_text(
                "def main():\n"
                "    print('App is running...')\n\n"
                "if __name__ == '__main__':\n"
                "    main()\n"
            )
        else:
            path.touch()

    elif path.suffix == ".yaml":
        # Optional: minimal yaml placeholder (valid yaml)
        path.write_text("# YAML config\n")

    elif path.suffix == ".html":
        path.write_text(
            "<!doctype html>\n"
            "<html>\n"
            "<head><meta charset='utf-8'><title>App</title></head>\n"
            "<body><h1>Hello</h1></body>\n"
            "</html>\n"
        )

    else:
        path.touch()


def create_project_structure(files: list[str]) -> None:
    try:   
        for filepath in files:
            path=Path(filepath)

            # NOTE:
            # path.parent = directory of the file
            # parents=True  → create all missing parent folders
            # exist_ok=True → do NOT fail if folder already exists

            # path.parent.mkdir(parents=True, exist_ok=True)
            parent_dir = path.parent
            if not parent_dir.exists():
                parent_dir.mkdir(parents=True, exist_ok=True)
                logging.info(f"Created directory: {parent_dir}")
            else:
                parent_dir.mkdir(parents=True, exist_ok=True)

            # Create file only if it doesn't exist
            if not path.exists():
                write_minimal_content(path)
                logging.info(f"Created file: {path}")
            else:
                logging.info(f"{path.name} already exists")
           
    except OSError as e: 
        logging.error(f"File system error occurred: {e}")
        raise
            

if __name__ == "__main__":
    create_project_structure(ALL_FILES)
    logging.info("✅ Project structure created successfully.")
