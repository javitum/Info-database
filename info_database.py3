import sqlite3

##Script to obtain data from a database
##How are the number of tables, number of columns, rows and data in each table
##, and the number of total records

##Script para obtener los datos de una base de datos
## Como son el numero de tablas, numero de columna, filas y datos de cada tabla
##, y el numero de registros totales

#request database name
database=input('Name of the database?: ')

conexion = sqlite3.connect(database)
cursorObject= conexion.cursor()
cursorObject.execute("SELECT name FROM sqlite_master WHERE type='table';")

#database tables
all_tbls = cursorObject.fetchall()
tables=len(all_tbls)
print(f'The database has {tables} tables')
datos=0

#browse the database tables
for table in all_tbls:
    cursorObject.execute(f'select * from {table[0]}')
    dates=cursorObject.fetchall()
    rows=len(dates)
    request_columns = f"PRAGMA table_info({table[0]})" 
    cursorObject.execute(request_columns)
    columns=len(cursorObject.fetchall())
    registers=rows*columns
    datos=datos+(registers)
    print (f'The tables {table[0]} has {columns} columns,  {rows} rows and {registers} registers')
    
print(f'The database {database} has {datos} dates')
