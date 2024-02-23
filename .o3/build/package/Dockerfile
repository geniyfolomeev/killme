ARG BASE_IMAGE_REPO

FROM ${BASE_IMAGE_REPO}/docker/python:3.10

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --index-url https://artifactory.s.o3.ru/artifactory/api/pypi/pypi-remote/simple \
    --no-cache-dir \
    -r requirements.txt

ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

EXPOSE 80 84
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

COPY ./app/ /usr/src/app

ARG GIT_COMMIT_SHA
ENV SENTRY_RELEASE=$GIT_COMMIT_SHA
