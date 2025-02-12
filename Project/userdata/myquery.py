import mysql.connector

def connection():
    return mysql.connector.connect(
        host='database-1.cgp0ki4geqwi.us-east-1.rds.amazonaws.com',
        user='admin',
        password='Abantika04*',
        database='my_db'
    )



def userdatainsertion(n, e, pn):

    con = connection()
    cursor = con.cursor()
    qry = 'INSERT INTO my_table (`name`, `email`, `number`) VALUES (%s, %s, %s)'
    values = (n, e, pn) 

    cursor.execute(qry, values)
    con.commit()

    print("Data inserted successfully.")
    cursor.close() 
    con.close()


def userdatafetch():
    con  = connection()
    cursor = con.cursor()
    qry = "SELECT * FROM my_table"
    cursor.execute(qry)
    data  = cursor.fetchall()
    cursor.close()
    con.close()
    return data


def deleteUser(id):
    con = connection()  
    cursor = con.cursor()
    qry = "DELETE FROM my_table WHERE id = %s"
    values = (id,) 
    cursor.execute(qry, values)
    con.commit()


def userdataupdate(n,e , pn , id):
    try:
        con = connection()  
        cursor = con.cursor()
        qry = "UPDATE my_table SET name = %s, email = %s , number = %s WHERE id = %s"
        values = (n, e , pn ,id) 
        
        cursor.execute(qry, values)
        con.commit() 
        
        if cursor.rowcount > 0:
            print("Data updated successfully.")
        else:
            print("No records updated. Check if the ID exists.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close() 
        if con:
            con.close()


def get_user_by_id(user_id):
    con = connection() 
    cursor = con.cursor() 
    # Modify based on your DB interaction method
    query = "SELECT * FROM my_table WHERE id = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchone() 