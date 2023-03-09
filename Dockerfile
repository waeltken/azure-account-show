FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY ./Pipfile ./Pipfile.lock ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pipenv && \
		pipenv install --system --deploy --ignore-pipfile
COPY . .
CMD ["python", "main.py"]