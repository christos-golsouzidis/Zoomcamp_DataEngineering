
import pandas as pd
from sqlalchemy import create_engine
import argparse


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    database = params.database
    table = params.table
    csv = params.csv

    df = pd.read_csv(csv)

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    engine.connect()

    df.head(0).to_sql(name=table, con=engine, if_exists='replace')

    df.to_sql(name=table, con=engine, if_exists='append')
    print('Job completed successfully.')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")
    parser.add_argument('--user', help='user to postgres')
    parser.add_argument('--password', help='password to postgres')
    parser.add_argument('--host', help='host to postgres')
    parser.add_argument('--port', help='port to postgres')
    parser.add_argument('--database', help='database to postgres')
    parser.add_argument('--table', help='table name of the db')
    parser.add_argument('--csv', help='csv path')

    args = parser.parse_args()

    main(args)

