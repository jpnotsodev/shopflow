import sys
import os
from pathlib import Path

from duckdb import InternalError

from staging.stage_data import duckdb_conn


cursor = duckdb_conn.cursor()

if not Path(sys.argv[1]).is_file():
    print(cursor.sql(sys.argv[1]))
else:
    if not os.path.exists(sys.argv[1]):
        # check if the file exists, raise an error if it doesn't
        raise FileNotFoundError(f"{repr(sys.argv[1])} does not exists.")
    with open(sys.argv[1], "r") as sql:
        try:
            cursor.execute(sql.read())
        except InternalError as e:
            raise e