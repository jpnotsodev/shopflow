import duckdb

from pathlib import Path

duckdb_conn = duckdb.connect("staging_db.duckdb")


def stage():
    for file in Path("staging/tables").iterdir():
        with open(file, "r") as sql:
            duckdb_conn.execute(sql.read())

if __name__ == "__main__":
    stage()