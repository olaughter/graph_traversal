import csv
import sqlite3
import os

from main import route

FIXTURE_TABLE_NAME = "network_connectivity"
FIXTURE_SOURCE = "fixture.csv"

def create_table_sql():
    return f"create table if not exists {FIXTURE_TABLE_NAME} (a INTEGER, b INTEGER)"

def truncate_table_sql():
    return f"delete from {FIXTURE_TABLE_NAME}"

def insert_fixture_sql():
    with open(FIXTURE_SOURCE, "r") as f:
        csv_reader = csv.reader(f)
        
        values = ", ".join([f"({row[0]}, {row[1]})" for row in csv_reader])
        sql = f"insert into {FIXTURE_TABLE_NAME} values {values}"

    return sql
    
def setup():
    os.environ["NETWORK_DATABASE"] = "test.db"

    conn = sqlite3.connect(os.environ["NETWORK_DATABASE"])
    conn.execute(create_table_sql())
    conn.execute(truncate_table_sql())
    conn.execute(insert_fixture_sql())
    conn.commit()

def test_route():
    setup()

    test_cases = [
        ([1,4], [1,6,4]),
        ([3,5], [3,4,5]),
        ([1,6], [1,6]),
        ([1,4], [1,6,4]),
        ([1,5], [1,6,4,5]),
        ([2,6], [2,6]),
        ([3,1], [3,2,1]),
    ]

    for [start, target], answer in test_cases:
        assert route(start, target) == answer