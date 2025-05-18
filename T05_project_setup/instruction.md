- `uv init --python 3.12`
- Delete `main.py`
- Create `src` folder
- `uv add jupyterlab ipykernel pandas scikit-learn matplotlib seaborn openpyxl ruff notebook`
- Create `__init__.py` files as follows

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
