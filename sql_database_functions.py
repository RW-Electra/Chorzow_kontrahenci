import pandas as pd
import pyodbc
import time
connection_failed = False
name_error = False


def set_connection():
    conn = pyodbc.connect(
        "Driver={iSeries Access ODBC Driver};"
        "System=192.168.13.160;"
        "DATABASE=S78D3A20;"
        "UID=WOSZCZEKK;"
        "PWD=izoblok146;"
    )
    return conn


def close_connection(conn):
    if conn is not None:
        conn.close()


def Update_data_in_database(BuyersID_connection_Dictionary, library_name, table_name):
    global connection_failed
    global name_error
    try:
        connection = set_connection()
        connection_failed = False
    except:
        connection_failed = True
        return True

    table_name_string = library_name + "." + table_name
    request_string = f"DELETE FROM {table_name_string}"

    records = 0
    val_string = ''
    for BuyerID in BuyersID_connection_Dictionary:
        for Connection_ID in BuyersID_connection_Dictionary[BuyerID]:
            records += 1
            val_string += f"('{records}','{BuyerID}','{Connection_ID}'),"

    try:
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(request_string)
        connection.autocommit = False
        name_error = False
    except:
        name_error = True
        connection.close()
        return True

    request_string = f"INSERT INTO {table_name_string} " \
                     f"(ID,BUYERID, DOPASOWANIE)" \
                     f" VALUES {val_string[:-1]}"
    try:
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(request_string)
        connection.autocommit = False
        name_error = False
    except:
        name_error = True
        return True
    connection.close()
    return False




def get_errors():
    return connection_failed, name_error




