FROM python:3.5.9

LABEL version="0.1.0"
LABEL name="twtr2telega"

WORKDIR /usr/app/twtr2telega

COPY bot.py .
COPY commands.py .
COPY job.py .
COPY main.py .
COPY models.py .
COPY util.py .
COPY requirements.txt .

RUN pip install -r /usr/app/twtr2telega/requirements.txt

CMD ["python", "/usr/app/twtr2telega/main.py"]