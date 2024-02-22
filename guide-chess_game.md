

```bash
# create a virtual environment
python3 -m venv .venv

# activate the virtual environment
source .venv/bin/activate

# install the requirements
pip install -r requirements.txt
```

```bash
```


```bash
mkdir data
mkdir models
mkdir controllers
mkdir views
touch __init__.py
touch __main__.py
touch models/__init__.py
touch controllers/__init__.py
touch views/__init__.py
```

```bash
# controllers folder
touch controllers/app.py
touch controllers/player.py
touch controllers/tournament.py
```

```bash
# main.py

from controllers.app import App

from colorama import init

init(autoreset=True)


def main():
    """Start the application via the AppController class."""
    app = AppController()
    # app.run()
    app.start()

if __name__ == "__main__":
    main()
```


```bash
# config.py

# root directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# data directory
DATA_DIR = os.path.join(ROOT_DIR, "data")
# models directory
MODELS_DIR = os.path.join(ROOT_DIR, "models")
# controllers directory
CONTROLLERS_DIR = os.path.join(ROOT_DIR, "controllers")
# views directory
VIEWS_DIR = os.path.join(ROOT_DIR, "views")
```

```bash





```

```bash

