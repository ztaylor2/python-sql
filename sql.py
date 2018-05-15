"""Demonstrating the use of SQL in python with SQL alchemy."""

import sqlalchemy as sa
import pandas as pd


if __name__ == '__main__':
    engine = sa.create_engine('sqlite:///flight.db')
    connection = engine.connect()

    print(pd.read_sql('readings', connection))

    # an example of updating the table
    sql = """
        UPDATE readings
        SET pressure = 1021, humidity = 42
        WHERE flight = 'hab1' and humidity = 41
    """
    connection.execute(sql)
    pd.read_sql('readings', connection)

    # an example of deleting data from the table
    sql = """
        DELETE FROM readings
        WHERE flight = 'hab1' and pressure = 1020
    """
    connection.execute(sql)
    pd.read_sql('readings', connection)