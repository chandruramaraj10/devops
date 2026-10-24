# Monkey Flask Web App

A small Flask application with a responsive monkey-themed background and a
`/health` endpoint.

## Run locally

```bash
git clone https://github.com/chandruramaraj10/devops.git
cd devops
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open <http://localhost:8000> in a browser.

Check the health endpoint in another terminal:

```bash
curl http://localhost:8000/health
```

You can customize the displayed name and environment with variables:

```bash
APP_NAME="My Monkey App" APP_ENV="local" python app.py
```
