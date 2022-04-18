# Stock Profit Calculator

DSAI 2018 HW1 corrector

## Environment - 1: pipenv
### Prerequisite
- Python 3.6
- [pipenv](http://pipenv.org)

#### Install Dependency
```sh
pipenv install
```

#### Start Virtual Environment
```sh
pipenv shell
```

### Usage
```sh
python profit_calculator.py [-h] stock action
```

- stock: Input stock file
- action: Input action file

### Testing

#### Instal Testing Dependency
```sh
pipenv install --dev
```

#### Run Test
```sh
pytest
```

## Environment - 2: conda
### Prerequisite
- [conda](https://docs.conda.io/en/latest/index.html)

### Build Eev.
create an python 3.6 env.
```sh 
conda create -n StockProfitCalculator-py36 python=3.6.4
```
To activate Env. in linux:
```sh 
conda activate StockProfitCalculator-py36
```

To activate Env. in windows:
```sh 
activate StockProfitCalculator-py36
```

### Install Dependency
```
pip install -r requirements.txt
```

### Usage
```sh
python profit_calculator.py [-h] stock action
```
- stock: Input stock file
- action: Input action file

E.g.
```sh
python profit_calculator.py ./tests/testing_data.csv ./tests/output.csv
```

## AUTHORS
[Lee-W](https://github.com/Lee-W/)