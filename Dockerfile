FROM    python:3.10-buster AS base
ENV     PYTHONUNBUFFERED=true \
        PORT=8080
WORKDIR /src
RUN     apt update && \
        curl -sSL https://install.python-poetry.org | python -

FROM    base
ENV     PATH=/root/.local/bin:${PATH}
ADD     . ./
RUN     poetry config virtualenvs.create false && \
        poetry install --no-dev
WORKDIR /src/service
CMD     uvicorn --host 0.0.0.0 --port $PORT --workers 4 main:app
