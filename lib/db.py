import psycopg2
# Database methdos for connecting, inserting, fethching, and deleting.

# This method connects us to our database
def connectToDatabase():
    return psycopg2.connect(
            host = "ec2-34-234-240-121.compute-1.amazonaws.com",
            database = "d3pvstjgsdbmjp",
            user = "rmbmdpagnloizn",
            password = "c371c84f18d0b18a39d271bce2a695c6f4a2dbe4974d036cac1a86a2f5f4d076",
            port = "5432",
        );

# This method commits values to a table in our database
def commitToDatabase(values):
    # Create connection and cursor
    conn = connectToDatabase();
    c = conn.cursor();

    # Insert command

    sql_command = "INSERT INTO temp VALUES" + str(values)
    
    #execute command
    c.execute(sql_command)

    # Commit changes and close connection
    conn.commit();
    conn.close();

# This function returns all records in database
def getAllDbValues():
    conn = connectToDatabase();

    #create a cursor
    c = conn.cursor()

    #retreive records from database
    c.execute("SELECT * FROM temp")
    records = c.fetchall()

    return records;