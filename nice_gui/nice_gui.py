from nicegui import ui
from database_helper.database_common import create_sqlite_session, cursor_to_list_of_dict

my_database_path = '../sqlite_db/my_database.sqlite'

with create_sqlite_session(my_database_path) as session:
    rows = cursor_to_list_of_dict(session.execute("select * from investments"))

# Enrich rows
rows = [row |
        {"FV Calc" : row["PV"] if bool(row["PV"]) else None }
        for row in rows
        ]


columns = [
    {'name': 'investment_number', 'label': 'investment_number', 'field': 'name', 'required': True, 'align': 'left'},
    {'name': 'Description', 'label': 'Description', 'field': 'age', 'sortable': True},
]

ui.table(rows=rows, row_key='name')

ui.run()