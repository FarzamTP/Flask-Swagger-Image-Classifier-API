FROM python:3.8-rc-slim

COPY app.py /app/app.py
COPY settings.py /app/settings.py
COPY predict.py /app/predict.py
COPY routes /app/routes
COPY models /app/models
COPY static /app/static
COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

WORKDIR /app
RUN chmod 755 .

EXPOSE 5000

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]