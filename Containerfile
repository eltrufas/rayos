FROM ubuntu:jammy

RUN apt-get update && apt-get install -y libgeos-dev proj-bin libproj-dev python3-virtualenv

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY server3.py /app/

CMD ["panel", "serve", "server3.py"]

