"""Demonstrating the use of SQL in python with SQL alchemy."""

import sqlalchemy as sa
import pandas as pd


if __name__ == '__main__':
    engine = sa.create_engine('sqlite:///flight.db')
    connection = engine.connect()

    print(pd.read_sql('readings', connection))
