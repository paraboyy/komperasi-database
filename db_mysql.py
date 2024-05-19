import time
import mysql.connector

# Fungsi untuk mendapatkan koneksi ke database MySQL
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_e_commerce" 
        )
        return connection
    except mysql.connector.Error as err:
        print("Error:", err)

# Fungsi untuk menyimpan hasil eksekusi ke dalam file
def save_to_file(filename, data):
    with open(filename, 'a') as f:
        f.write(data + '\n')

# Fungsi umum untuk menjalankan operasi SQL
def execute_sql_operation(operation_name, query, values=None):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            start_time = time.time() # Waktu awal eksekusi
            if values:
                cursor.executemany(query, values)
            else:
                cursor.execute(query)
            connection.commit()
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time

            print(f"Waktu komperasi {operation_name} data {execution_time} seconds")
            save_to_file('hasil/results.txt', f'{operation_name}: {execution_time} seconds')

            cursor.close()
            connection.close()
    except Exception as e:
        print("Error:", e)

# Fungsi untuk melakukan pengujian operasi insert dengan banyak data
def test_insert_operation():
    query = "INSERT INTO products (name, price, category, description) VALUES (%s, %s, %s, %s)"
    values = [('New Product', 99, 'Test Category', 'Test Description') for _ in range(1000)]
    execute_sql_operation("Insert", query, values)

# Fungsi untuk melakukan pengujian operasi update
def test_update_operation():
    query = "UPDATE products SET price = 199 WHERE price = 2000"
    execute_sql_operation("Update", query)

# Fungsi untuk melakukan pengujian operasi search
def test_search_operation():
    query = "SELECT * FROM products WHERE category = 'Test Category'"
    execute_sql_operation("Search", query)

# Fungsi untuk melakukan pengujian operasi delete
def test_delete_operation():
    query = "DELETE FROM products WHERE name = 'New Product'"
    execute_sql_operation("Delete", query)

save_to_file('hasil/results.txt', 'Komparasi DB Relasional tanpa Caching')
# Panggil fungsi untuk menjalankan pengujian operasi insert dengan banyak data
test_insert_operation()

# Panggil fungsi untuk menjalankan pengujian operasi update
test_update_operation()

# Panggil fungsi untuk menjalankan pengujian operasi search
test_search_operation()

# Panggil fungsi untuk menjalankan pengujian operasi delete
test_delete_operation()
save_to_file('hasil/results.txt', '----------------------------------------')
