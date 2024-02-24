import json
import os
from datetime import datetime
from pathlib import Path

import pytz

import alembic.config
from src.orm.config import session_generator
from src.orm.models.visits import Visits


def read_init_data():
    init_data_file_path = Path.cwd() / "database" / "init-data.json"
    with init_data_file_path.open() as f:
        return json.load(f)


def parse_visit_info(visit: dict):
    visit["scheduled_at"] = datetime.strptime(
        visit["scheduled_at"], "%Y-%m-%d %H:%M:%S",
    ).astimezone(tz=pytz.UTC)


if __name__ == "__main__":
    sqlite_db_filename = os.getenv("SQLITE_DB_FILENAME", "")
    if not sqlite_db_filename:
        msg = "SQLITE_DB_FILENAME environment variable is not set"
        raise Exception(msg)  # noqa: TRY002

    db_file_path = Path.cwd() / "database" / sqlite_db_filename
    init_data_file_path = Path.cwd() / "database" / "init-data.sql"

    # Delete existing database file
    Path.unlink(db_file_path, missing_ok=True)

    # create file with touch with read and write permissions
    db_file_path.touch(mode=0o755, exist_ok=True)

    # Creates tables and models
    alembic_args = [
        "--raiseerr",
        "upgrade",
        "head",
    ]
    alembic.config.main(argv=alembic_args)

    # Inserts initial data into the db
    visits = read_init_data()

    with session_generator() as session:
        for visit_info in visits:
            parse_visit_info(visit_info)
            visit = Visits(**visit_info)
            session.add(visit)
        session.commit()
