import mysql.connector
from mysql.connector import Error
import time

# Fungsi untuk melakukan komparasi operasi insert
def compare_insert_operation():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_json_e_commerce" 
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Query untuk operasi insert
            query = """
            INSERT INTO products_json (product_data) VALUES ('{"name": "New Product", "price": 99, "category": "Test Category", "description": "Test Description"}')
            """
            start_time = time.time() # Waktu awal komparasi
            for i in range(1000):  # Melakukan operasi insert sebanyak 1000 kali
                cursor.execute(query)
            connection.commit()
            end_time = time.time() # Waktu akhir komparasi
            execution_time = end_time - start_time

            print("Insert operation execution time: {} seconds".format(execution_time))

            # Simpan waktu komparasi ke dalam file
            with open('hasil/results.txt', 'a') as file:
                file.write("Insert operation execution time: {} seconds\n".format(execution_time))

            cursor.close()
            connection.close()

    except Error as e:
        print("Error:", e)

# Fungsi untuk melakukan komparasi operasi update
def compare_update_operation():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_json_e_commerce" 
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Query untuk operasi update
            query = """
            UPDATE products_json SET product_data = '{"name": "Updated Product", "price": 199, "category": "Updated Category", "description": "Updated Description"}' WHERE JSON_EXTRACT(product_data, '$.name') = 'New Product'
            """
            start_time = time.time() # Waktu awal komparasi
            for i in range(1000):  # Melakukan operasi update sebanyak 1000 kali
                cursor.execute(query)
            connection.commit()
            end_time = time.time() # Waktu akhir komparasi
            execution_time = end_time - start_time

            print("Update operation execution time: {} seconds".format(execution_time))

            # Simpan waktu komparasi ke dalam file
            with open('hasil/results.txt', 'a') as file:
                file.write("Update operation execution time: {} seconds\n".format(execution_time))

            cursor.close()
            connection.close()

    except Error as e:
        print("Error:", e)

# Fungsi untuk melakukan komparasi operasi delete
def compare_delete_operation():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_json_e_commerce" 
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Query untuk operasi delete
            query = """
            DELETE FROM products_json WHERE JSON_EXTRACT(product_data, '$.name') = 'Updated Product'
            """
            start_time = time.time() # Waktu awal komparasi
            for i in range(1000):  # Melakukan operasi delete sebanyak 1000 kali
                cursor.execute(query)
            connection.commit()
            end_time = time.time() # Waktu akhir komparasi
            execution_time = end_time - start_time

            print("Delete operation execution time: {} seconds".format(execution_time))

            # Simpan waktu komparasi ke dalam file
            with open('hasil/results.txt', 'a') as file:
                file.write("Delete operation execution time: {} seconds\n".format(execution_time))

            cursor.close()
            connection.close()

    except Error as e:
        print("Error:", e)

with open('hasil/results.txt', 'a') as file:
    file.write("Komparasi DB JSON tanpa Caching\n")

# Panggil fungsi untuk melakukan komparasi operasi insert
compare_insert_operation()

# Panggil fungsi untuk melakukan komparasi operasi update
compare_update_operation()

# Panggil fungsi untuk melakukan komparasi operasi delete
compare_delete_operation()

with open('hasil/results.txt', 'a') as file:
    file.write("----------------------------------------\n")
