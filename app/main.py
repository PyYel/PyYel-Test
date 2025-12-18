from pylcloud.database import DatabaseRelationalPostgreSQL


app_db = DatabaseRelationalPostgreSQL()
app_db.list_databases(display=True)