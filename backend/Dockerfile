FROM python:3.13.4-slim-bullseye

# host.docker.internal -> localhost
# curl -X POST -d '{"message":"Hello world!"}' -H "Content-Type: application/json" http://localhost:8080/api/chats/
RUN apt-get update && apt-get install -y curl

# create venv
RUN python -m venv /opt/venv/
ENV PATH=/opt/venv/bin:$PATH


WORKDIR /app

# copy local file to contanier destination
COPY requirements.txt /tmp/requirements.txt
# run within container while building
RUN pip install -r /tmp/requirements.txt

COPY ./src /app

CMD ["python", "-m", "http.server", "8000"]