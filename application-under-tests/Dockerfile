FROM python:3.12-alpine3.19 as dev

RUN mkdir /work/
WORKDIR /work/

COPY requirements.txt /work/requirements.txt
RUN pip install -r requirements.txt

FROM python:3.12-alpine3.19 as prod

RUN mkdir /app/
WORKDIR /app/

COPY --from=dev /work/ /app/
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
CMD flask run -h 0.0.0 -p 5000