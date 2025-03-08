# aithenos-self-study

Aithenos AI Production

## Description

## To Do List

## Install and run

### Set up

#### Set up env

Using python 3.10.16

```bash
conda create -n self-study python==3.10.16 -y

conda activate self-study
```

#### Set up pre-commit to format code

    - Install:
    ```bash
    pip install pre-commit
    ```

    - Add pre-commit to git hook:
    ```bash
    pre-commit install
    ```

    - Run pre-commit for formating code (only staged files in git):
    ```bash
    pre-commit run
    ```

    - Run pre-commit for formating code with all files:
    ```bash
    pre-commit run --all-files

## Code Structure

backend/ (Main code in here)

exp/ (Testing in here)
