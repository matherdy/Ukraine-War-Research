# PythonProject

# To-Do/Goal List:

### Data Collection





## Setup for developement:

- Setup a python 3.x venv (usually in `.venv`)
  - You can run `./scripts/create-venv.sh` to generate one
- `pip3 install --upgrade pip`
- Install pip-tools `pip3 install pip-tools`
- Update dev requirements: `pip-compile --output-file=requirements.dev.txt requirements.dev.in`
- Update requirements: `pip-compile --output-file=requirements.txt requirements.in`
- Install dev requirements `pip3 install -r requirements.dev.txt`
- Install requirements `pip3 install -r requirements.txt`
- `pre-commit install`

### Update versions

`pip-compile --output-file=requirements.dev.txt requirements.dev.in --upgrade`

## Run `pre-commit` locally.

`pre-commit run --all-files`





# Data Collection:

Used keywords
ukraine
ukraine+stock
ukraine+energy
ukraine+oil
kyiv+energy
kyiv+stock
kyiv+oil
war+stock
war+energy
stock+energy
green+energy
putin
putin+war
putin+energy
putin+oil
zelenskyy
zelenskyy+war
zelenskyy+energy
invasion
russia
russia+war
russia+stock
russia+invasion
NATO
