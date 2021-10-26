FROM python:3.6.12

LABEL version="0.2.0"
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