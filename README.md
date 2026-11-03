
# GitHub Actions CI Practice Project

A tiny Python calculator project to practice Git, GitHub, pytest, and GitHub Actions.

## 1. Run it on your computer

Open a terminal in this project folder and run:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt**
```bat
.venv\Scripts\activate.bat
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install the test dependency and run tests:

```bash
pip install -r requirements.txt
pytest -v
```

Expected result: **3 passed**.

## 2. Push the project to GitHub

Create a new empty GitHub repository. Then, from this project folder, run:

```bash
git init
git add .
git commit -m "Add calculator and CI workflow"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the URL with your own repository URL.

## 3. Watch GitHub Actions

1. Open your GitHub repository.
2. Select the **Actions** tab.
3. Open **Python CI Practice**.
4. Click the workflow run to see each step.
5. Expand a step to inspect its logs.

The workflow starts on a push to `main` and on pull requests targeting `main`.
GitHub provides a temporary Ubuntu runner, checks out your code, sets up Python,
installs pytest, and runs the tests.

## 4. Practice a failed test

Open `tests/test_app.py` and temporarily change:

```python
assert add(2, 3) == 5
```

to:

```python
assert add(2, 3) == 99
```

Run `pytest -v` locally. It should fail.

Commit and push the change:

```bash
git add .
git commit -m "Practice a failing test"
git push
```

Go to **Actions** and observe that the workflow is marked failed. Fix the expected
value back to `5`, commit, and push again. The workflow should pass.

## Important

This starter project practices **CI (build/setup and automated testing)**.
It does not deploy to a live server. First understand the test workflow; deployment
can be added as a separate next exercise.
