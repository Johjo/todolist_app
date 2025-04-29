# Utilise une image officielle Python
FROM python:3.13-bookworm

# Installe poetry
RUN pip install --no-cache-dir poetry

# Crée un dossier pour ton app
WORKDIR /app

# Copie seulement le fichier de dépendances pour installer plus vite
COPY pyproject.toml poetry.lock* /app/

# Installe les dépendances sans créer un venv interne
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copie le reste de ton projet
COPY . /app

ENV PYTHONPATH=/app/src

# Définit la commande pour démarrer ton app

CMD poetry run python main_demo.py
