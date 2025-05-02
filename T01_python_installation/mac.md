# Python Installation - Mac

## 1. Install `brew`

```bash
bash bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Copy the command printed after the installation. It should look like this

```bash
echo >> /Users/[Your User Name]/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/icemacbook/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

## 2. Install `uv`

- `brew install uv`

## 3. Install Python

- `uv python install 3.12`

## 4. Create a virtual environment

- `uv venv --python 3.12`
- Activate the environment
  - `source ~/.venv/bin/activate`
- Install packages
  - `uv pip install jupyterlab ipykernel pandas scikit-learn matplotlib seaborn openpyxl ruff notebook`

# VSCode

- Install `VSCode`
- Install VSCode extensions
  - Python Extension Pack
  - Jupyter
  - Ruff
- Go to VSCode setting
  - `python.venvPath` -> `~`
  - `editor.formatOnSave` -> ✔️

# Run python file

- Create `hello.py`

```python
import pandas as pd

print("Hello World")
print(print(pd.__version__))
```

- Set "Workspace Environment"
- Run file from the play button.
- (Optionally) select formatter

# Run Jupyter notebook

- Create `hello.ipynb`
- Click `Select Kernel` at the top right.
- Click `+ Code` and type some code.
- Click play button.
- (Optionally) select formatter
