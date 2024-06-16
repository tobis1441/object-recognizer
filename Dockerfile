FROM python:3.10.14-bookworm

WORKDIR /src

COPY requirements.txt requirements.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

ENV PYTHONPATH /src

COPY src .

EXPOSE 8000

CMD ["python", "main/main.py"]
