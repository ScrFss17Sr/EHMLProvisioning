from hdbcli import dbapi
from Helper.CSVLoader import CSVLoader

def connectToHana():
    print("Try to connect to hana: ")
    conn = dbapi.connect(
        address="localhost",
        port=30015,
        user="EML",
        password="SvenRosenzweig1992"
    )
    print('Connected', conn.isconnected())
    return conn


def setSchema(conn, schema=""):
    sql_select_schema = 'SET Schema ' +schema + ';'
    cursor = conn.cursor()
    cursor.execute(sql_select_schema)


#Data: [{"date": "2018-01-01 00:00", "temperatrue": "1,2" }, {"date": "2018-01-02 00:00", "temperatrue": "3,1"}]
def insert(conn, schema="", table="", data=[]):
    setSchema(conn, schema)

    cursor = conn.cursor()

    sql_insert = 'INSERT INTO ' + table + '('
    sql_values = ' VALUES('

    #'VALUES ( :date, :temperature )'
    print('Last Element:  ' + list(data[0].keys())[-1])

    for key in list(data[0].keys()):
        print(key)
        if key == list(data[0].keys())[-1]:
            sql_insert += key + ')'
            sql_values += ':' + key + ')'
        else:
            sql_insert += key + ','
            sql_values += ':' + key + ','

    sql_insert += sql_values

    print('Statement: '+ sql_insert)

    for row in data:
        print(str(row))
        cursor.execute(sql_insert, row)

    cursor.close

def insertData(schema="", table="", data=[] ):
    conn = connectToHana()
    insert(conn=conn, schema=schema, table=table, data=data)

def select(schema="", table="", where=""):
    return

if __name__ == '__main__':
    conn = connectToHana()
    if(conn.isconnected()):
        print('Successfully connected to Hana')

        csv_loader = CSVLoader(fullpath='../data/train.csv', delimiter=',')
        data = csv_loader.get_all_data()


        test = list()
        for row in data:
            d = {}
            d['x'] = row[0]
            d['y'] = row[1]
            test.append(d)

        print(test)
        insert(conn=conn, schema="EML", table="EH_BI_DATA", data= test)

    print("Finished");

