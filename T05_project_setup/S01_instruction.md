# Installing `git`

- Download and install from https://git-scm.com/
- Set your username and email

```bash
git config --global user.name "firstname lastname";
git config --global user.email "email@example.com"
```

- Check by `git config --list`

# Creating a new project

- Create a new folder (e.g. `project`)
  - `mkdir project`
  - `cd project`
- `uv init --python 3.12`
- `uv add jupyterlab ipykernel pandas scikit-learn matplotlib seaborn openpyxl ruff notebook`

> When you create a project using `uv`, your dependency versions are automatically locked and fixed in the `uv.lock` file. This ensures that every environment created from your project will use the exact same package versions, leading to consistent and reproducible results across different machines and collaborators.

# Organizing a new project

- Delete `main.py`
- Create `src` and `run` folders and add source codes.
- Create a blank `__init__.py` file.
  - This file marks the directory as a Python package.
- Your project directory should look like this.

```
📁 src
    📁 ml_runner
        📄 __init__.py
        📄 v1.py
    📁 run
        📄 data.xlsx
        📄 S04_workflow_real_fit.ipynb
        📄 S05_workflow_real_analyze.ipynb
📄 .gitignore
📄 .python-version
📄 pyproject.toml
📄 README.md
📄 uv.lock
```

- Install the project in [editable mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).
  - `uv pip install -e .`

# Create a new Github repository

- Create a new git repository in `GitHub`.
  - Copy a git url `https://...`
- Initializing a git repository in your project (if your project is not already a git repository)
  - `git init`
- Point your local git repository to the GitHub repository
  - `git remote add origin https://...`
  - Check your remotes with `git remote -v`
- Staging your changes
  - `git add .`
- Commit your changes
  - `git commit -m "Update ..."`
- Push your changes
  - `git push --set-upstream origin master`

### Other git commands

- Fetch and merge changes from the remote
  - `git pull`
- Show the status of files in the working directory
  - `git status`
- View commit
  - `git log`

## Reinitializing an existing GitHub repository

- Clone an existing repository
  - `git clone https://...`
- Installing packages
  - `uv sync`
  - `uv pip install -e .`
