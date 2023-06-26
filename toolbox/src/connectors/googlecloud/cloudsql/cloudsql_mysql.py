from google.cloud.sql.connector import Connector
import sqlalchemy

def initializeCloudSQL(project, region, instance, user, password, db):
    """Initializes and returns a connection with Cloud SQL."""

    connector = Connector()
    conn = connector.connect(
        project + ":" + region + ":" + instance,
        "pymysql",
        user=user,
        password=password,
        db=db
    )

    return conn

def executeCloudSQL(statement):
    """Executes a query in Cloud SQL and returns the result."""

    query = sqlalchemy.text(statement)
    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )
    with pool.connect() as db_conn:
        db_conn.execute(insert_stmt, parameters={"id": "book1", "title": "Book One"})
        result = db_conn.execute(sqlalchemy.text("SELECT * from my_table")).fetchall()
        db_conn.commit()

    return result


def closeCloudSQL(connector): 
    connector.close()