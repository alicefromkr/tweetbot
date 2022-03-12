FROM python:3.7-alpine

COPY bots/config.py /bots/
COPY bots/LikeRetweet.py /bots/
COPY requirements.txt /tmp
RUN python -m pip install --upgrade pip
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "LikeRetweet.py"]