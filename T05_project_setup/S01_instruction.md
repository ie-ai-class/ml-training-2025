# Install `git`

- Download and install from https://git-scm.com/
- Set your username and email

```bash
git config --global user.name "firstname lastname";
git config --global user.email "email@example.com"
```

# Create a project structure

- `uv init --python 3.12`
- `uv add jupyterlab ipykernel pandas scikit-learn matplotlib seaborn openpyxl ruff notebook`
- Delete `main.py`
- Create `src` and `run` folders with the following files
  - `__init__.py` is a blank file.
- `uv pip install -e .`

```
📁 src
    📁 ml_runner
        📄 __init__.py
        📄 v1.py
    📁 run
        📄 S04_workflow_real_fit.ipynb
        📄 S05_workflow_real_analyze.ipynb
📄 .gitignore
📄 .python-version
📄 pyproject.toml
📄 README.md
📄 uv.lock
```
