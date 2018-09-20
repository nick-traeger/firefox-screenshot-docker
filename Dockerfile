FROM ubuntu

ENV DEBIAN_FRONTEND noninteractive
ENV FLASK_APP main.py

RUN apt-get update && apt-get -y install --no-install-recommends -qq python3 python3-pip python3-setuptools firefox && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--workers", "5", "--bind", "0.0.0.0:8000", "wsgi:app"]
