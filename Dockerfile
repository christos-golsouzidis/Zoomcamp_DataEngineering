FROM python:3.9 

RUN pip install pandas sqlalchemy psycopg2-binary argparse

WORKDIR /app
COPY . .

ENTRYPOINT ["python", "green_taxi_pipeline.py"]

