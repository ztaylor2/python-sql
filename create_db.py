"""A script to create the database."""

import sqlalchemy as sa

if __name__ == '__main__':
    engine = sa.create_engine('sqlite:///flight.db')

    connection = engine.connect()

    sql = """
    CREATE TABLE readings (
        flight    VARCHAR(10) NOT NULL,
        ts        TIMESTAMP NOT NULL,
        temp      NUMERIC(3,1) NOT NULL,
        pressure  NUMERIC(4,0) NOT NULL,
        humidity  NUMERIC(3,0) NOT NULL,
        accel_x   REAL DEFAULT 0 NOT NULL,
        accel_y   REAL DEFAULT 0 NOT NULL,
        accel_z   REAL DEFAULT 0 NOT NULL,

        CONSTRAINT readings_pk PRIMARY KEY (flight, ts),
        CONSTRAINT temp_ck CHECK (temp BETWEEN -70 AND 70),
        CONSTRAINT pres_ck CHECK (pressure BETWEEN 0 AND 2000),
        CONSTRAINT hum_ck CHECK (humidity BETWEEN 0 AND 100)
    )
    """
    connection.execute(sql)

    sql = """
        INSERT INTO readings(flight, ts, temp, pressure, humidity)
        VALUES ('hab1', '2015-01-01 09:00:00', 25.5, 1020, 40)
    """
    connection.execute(sql)

    sql = """
        INSERT INTO readings(flight, ts, temp, pressure, humidity)
        VALUES
          ('hab1', '2015-01-01 09:01:00', 25.5, 1019, 40),
          ('hab1', '2015-01-01 09:02:00', 25.5, 1019, 41)
    """
    connection.execute(sql)

    sql = """
        INSERT INTO readings(flight, ts, temp, pressure, humidity)
        VALUES ('hab1', '2015-01-01 09:03:00', 25.5, -1000, 40)
    """
    try:
        connection.execute(sql)
    except Exception as e:
        print(e)

