# How the War in Ukraine is Affecting the Predictability of the Energy Stock Market

## Important Links 
- Text Analysis Meeting Notes: https://docs.google.com/document/d/17tsZcXi3bGT1AHkA875-W_ctOUX1SKOqzRgez_HEE8o/edit?usp=sharing
- Data Mining Meeting Notes: https://docs.google.com/document/d/1oHuGH65mphbCqiuvs5ZZg02AVA5wi621hZin_TLWPjs/edit?usp=sharing
- Financial Analysis Meeting Notes: https://docs.google.com/document/d/1P3FgKjTBLSxvM30N8pjrqgq6xezCF_0Dkddx9roiV9M/edit?usp=sharing


## GitHub tips
Submitting a pull request
https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request


## Data Collection:

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


## Financial Analysis

TTI Library https://trading-technical-indicators.readthedocs.io/en/latest/index.html

Possible list of models
Moving Average (MA)
Exponential Moving Average (EMA)
Stochastic Oscillator
Moving Average Convergence Divergence (MACD)
Bollinger Bands
Relative Strength Index (RSI)
Fibonacci Retracement
Ichimoku Cloud
Standard Deviation
Average Directional Index
Average Directional Movement Index (ADX)
Regression
On Balance Volume (OBV)







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


