import json
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*****",
  database="sample",
  buffered = True,
)

dbse = mydb.cursor()
dbse.execute('Drop table json_data')
dbse.execute('Create table json_data(COL_ID text, COL_INT_VALUE int, COL_BOOL_VALUE boolean, COL_FLOAT_VALUE float, COL_STRING_VALUE text)')

test_json = json.loads(json.dumps(
[{
    "COL_ID": "id1",
    "COL_INT_VALUE": 7,
    "COL_BOOL_VALUE": True,
    "COL_FLOAT_VALUE": 3.14159,
    "COL_STRING_VALUE": "Python"
    },
    {
    "COL_ID": "id2",
    "COL_INT_VALUE": 10,
    "COL_BOOL_VALUE": False,
    "COL_FLOAT_VALUE": 2.71828,
    "COL_STRING_VALUE": "MySQL"
    },]
    )
)

values = [list(x.values()) for x in test_json]
# print(values)


columns = [list(x.keys()) for x in test_json][0]

values_str = ""

for i, record in enumerate(values):

    val_list = []
   
    for v, val in enumerate(record):
        if type(val) == str:
            val = "'{}'".format(val.replace("'", "''"))
        val_list += [ str(val) ]

    values_str += "(" + ', '.join( val_list ) + "),\n"

values_str = values_str[:-2] + ";"

table_name = "json_data"
sql_string = "INSERT INTO %s (%s)\nVALUES\n%s" % (
    table_name,
    ', '.join(columns),
    values_str
)

dbse.execute(sql_string)

dbse.execute("""Select COL_ID, COL_INT_VALUE, COL_BOOL_VALUE, COL_FLOAT_VALUE, COL_STRING_VALUE from json_data""")
res = dbse.fetchall()

for r in res:
    print('ID:', r[0])
    print('Integer:', r[1])
    print('Boolean:', r[2])
    print('Float:', r[0])
    print('String:', r[0])
    print()