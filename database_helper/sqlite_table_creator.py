import pandas as pd
from sqlalchemy import create_engine, text, inspect, Text
from sqlalchemy.schema import CreateTable
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
import os
from pathlib import Path

# Create a Base for the declarative models
Base = declarative_base()


class SQLiteTableCreator:
    """
    A class to manage the creation of SQLite databases and tables from CSV files.
    """

    def __init__(self, db_path, csv_dir):
        """
        Initializes the database_helper.

        Args:
            db_path (str): The path to the SQLite database file.
            csv_dir (str): The directory containing the CSV files.
        """
        self.db_path = db_path
        self.csv_dir = csv_dir
        self.engine = create_engine(f'sqlite:///{self.db_path}')
        self.metadata = Base.metadata
        self.session = None  # We won't use a session for this specific task

    def _infer_column_type(self, series):
        """
        Infers the SQLAlchemy column type based on a pandas Series.
        """
        # Check if the series contains only integers
        if pd.api.types.is_integer_dtype(series):
            return Integer
        # Check if the series contains only floats
        elif pd.api.types.is_float_dtype(series):
            return Float
        # Otherwise, default to string
        else:
            return String

    def _create_table_from_df(self, df, table_name):
        """
        Creates a SQLAlchemy Table object from a pandas DataFrame.
        """
        columns = [
            Column(col_name, self._infer_column_type(df[col_name]))
            for col_name in df.columns
        ]
        # Add an integer primary key column
        columns.insert(0, Column('id', Integer, primary_key=True))

        # Dynamically create a declarative class
        TableClass = type(table_name, (Base,), {
            '__tablename__': table_name,
            '__table_args__': {'extend_existing': True},
            **{col.name: col for col in columns}
        })

        # Get the table object from the class
        table = TableClass.__table__

        return table

    def _load_data_to_table(self, df, table_name):
        """
        Loads data from a pandas DataFrame into a specific table.
        """
        try:
            df.to_sql(table_name, self.engine, if_exists='append', index=False)
            print(f"✅ Data loaded successfully into table '{table_name}'.")
        except Exception as e:
            print(f"❌ Error loading data into table '{table_name}': {e}")

    def sql_result_to_dict (sql: Text) -> dict :
        return {}

    def test_db(self, my_database_path):
        # Delete testDB is it exits
        file_to_check = Path(my_database_path)
        if file_to_check.exists():
            file_to_check.unlink()

        # # Verify the tables were created
        # print("\n🔍 Verifying database contents...")
        # inspector = inspect(db_creator.engine)
        # tables = inspector.get_table_names()
        # print(f"Database contains the following tables: {tables}")


    def process_csv_files(self):
        """
        Main method to process all CSV files in the directory.
        """
        if not os.path.exists(self.csv_dir):
            print(f"❌ The directory '{self.csv_dir}' does not exist.")
            return

        csv_files = [f for f in os.listdir(self.csv_dir) if f.endswith('.csv')]
        if not csv_files:
            print("ℹ️ No CSV files found in the directory.")
            return

        print(f"🚀 Found {len(csv_files)} CSV files. Creating database tables...")
        print(f"")

        # Process each CSV file
        for filename in csv_files:
            table_name = os.path.splitext(filename)[0]
            file_path = os.path.join(self.csv_dir, filename)

            try:
                df = pd.read_csv(file_path)
            except Exception as e:
                print(f"❌ Error reading CSV file '{filename}': {e}")
                continue

            if df.empty:
                print(f"⚠️ Skipping empty file '{filename}'.")
                continue

            # Create the table
            table = self._create_table_from_df(df, table_name)
            self.metadata.create_all(self.engine)

            # Load the data
            self._load_data_to_table(df, table_name)


# Example Usage
if __name__ == '__main__':
    # Create a dummy directory and CSV files for demonstration
    example_dir = '~/sqlite_tables'
    # Replace with your actual home directory or adjust the path
    csv_dir_path = os.path.expanduser(example_dir)
    os.makedirs(csv_dir_path, exist_ok=True)

    # Create a sample CSV file
    with open(os.path.join(csv_dir_path, 'users.csv'), 'w') as f:
        f.write("name,age,city\n")
        f.write("Alice,30,New York\n")
        f.write("Bob,25,Los Angeles\n")

    with open(os.path.join(csv_dir_path, 'products.csv'), 'w') as f:
        f.write("product_name,price,stock\n")
        f.write("Laptop,1200.50,15\n")
        f.write("Mouse,25.99,100\n")

    # Use the class to create the database
    db_creator = SQLiteTableCreator(
        db_path='my_database.sqlite',
        csv_dir=csv_dir_path
    )
    db_creator.process_csv_files()

    # Verify the tables were created
    print("\n🔍 Verifying database contents...")
    inspector = inspect(db_creator.engine)
    tables = inspector.get_table_names()
    print(f"Database contains the following tables: {tables}")

    # You can also query the database to check the data
    with db_creator.engine.connect() as connection:
        # Query the 'users' table
        result_users = connection.execute(text("SELECT * FROM users"))
        print("\n📚 Data in 'users' table:")
        for row in result_users:
            print(row)

        # Query the 'products' table
        result_products = connection.execute(text("SELECT * FROM products"))
        print("\n📚 Data in 'products' table:")
        for row in result_products:
            print(row)