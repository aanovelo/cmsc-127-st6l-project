#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Connect to the MySQL database."""


import mysql.connector

dsn = {
    "user": "maria",
    "password": "P@ssw0rd",
    "host": "127.0.0.1",
    "port": "3306",
    "raise_on_warnings": True,
}


def main():
    """Run example code."""
    cnx = mysql.connector.connect(**dsn)
    cursor = cnx.cursor()

    print("The database cursor object is:")
    print(cnx)

    cursor.close()
    cnx.close()


if __name__ == "__main__":
    print(__doc__)
    main()
