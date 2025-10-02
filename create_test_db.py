from pathlib import Path

from icecream import ic
from sqlalchemy import inspect, text

from apps.tvm_time_value_of_money.time_value_of_money import TimeValueOfMoney
from database_helper.sqlite_table_creator import SQLiteTableCreator
from database_helper.database_common import create_sqlite_session, cursor_to_list_of_dict

if __name__ == '__main__':

    my_database_path = './sqlite_db/my_database.sqlite'

    # Delete testDB is it exits
    file_to_check = Path(my_database_path)
    if file_to_check.exists():
        file_to_check.unlink()

    # Use the class to create the database
    db_creator = SQLiteTableCreator(
        db_path=my_database_path,
        csv_dir="./sqlite_tables"
    )
    db_creator.process_csv_files()


    print("👋 Hi World")

    with create_sqlite_session(my_database_path) as session:
        ic(session)
        cursor = session.execute("select * from investments")
        rows = cursor_to_list_of_dict(cursor)
        ic(rows)

    # Verify the tables were created
    print("\n🔍 Verifying database contents...")
    inspector = inspect(db_creator.engine)
    tables = inspector.get_table_names()
    print(f"Database contains the following tables: {tables}")




