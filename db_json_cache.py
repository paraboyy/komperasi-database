import mysql.connector
import time
from pymemcache.client import base

# Inisialisasi koneksi ke Memcached
memcache_client = base.Client(('localhost', 11211))

# Fungsi untuk mendapatkan koneksi ke database MySQL
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_json_e_commerce" 
        )
        return connection
    except mysql.connector.Error as err:
        print("Error:", err)

# Fungsi untuk menyimpan hasil eksekusi ke file
def save_to_file(filename, data):
    with open(filename, 'a') as f:
        f.write(data + '\n')

# Fungsi untuk melakukan pengujian operasi insert
def compare_insert_operation():
    try:
        # Cek apakah data ada di cache
        cache_key = "insert_operation_json"
        cached_data = memcache_client.get(cache_key)
        if cached_data:
            print("Data Insert diambil dari cache")
            save_to_file('hasil/results.txt', f'Insert: {cached_data} seconds (from cache)')
            return cached_data

        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            # Query untuk operasi insert
            query = """
            INSERT INTO products_json (product_data) VALUES (%s)
            """
            values = [("""{"name": "New Product", "price": 99, "category": "Test Category", "description": "Test Description"}""",) for _ in range(1000)]
            
            start_time = time.time() # Waktu awal eksekusi
            cursor.executemany(query, values)
            connection.commit()
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time

            cursor.close()
            connection.close()

            # Simpan waktu eksekusi ke dalam cache
            memcache_client.set(cache_key, execution_time)

            print(f"Waktu komperasi Insert data {execution_time} seconds")
            save_to_file('hasil/results.txt', f'Insert: {execution_time} seconds')

            # Return waktu eksekusi
            return execution_time

    except Exception as e:
        print("Error:", e)

# Fungsi untuk melakukan pengujian operasi update
def compare_update_operation():
    try:
        # Cek apakah data ada di cache
        cache_key = "update_operation_json"
        cached_data = memcache_client.get(cache_key)
        if cached_data:
            print("Data Update diambil dari cache")
            save_to_file('hasil/results.txt', f'Update: {cached_data} seconds (from cache)')
            return cached_data

        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            # Query untuk operasi update
            query = """
            UPDATE products_json SET product_data = '{"name": "Updated Product", "price": 199, "category": "Updated Category", "description": "Updated Description"}' WHERE JSON_EXTRACT(product_data, '$.name') = 'New Product'
            """
            start_time = time.time() # Waktu awal eksekusi
            cursor.execute(query)
            connection.commit()
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time

            cursor.close()
            connection.close()

            # Simpan waktu eksekusi ke dalam cache
            memcache_client.set(cache_key, execution_time)

            print(f"Waktu komperasi Update data {execution_time} seconds")
            save_to_file('hasil/results.txt', f'Update: {execution_time} seconds')

            # Return waktu eksekusi
            return execution_time

    except Exception as e:
        print("Error:", e)

# Fungsi untuk melakukan pengujian operasi delete
def compare_delete_operation():
    try:
        # Cek apakah data ada di cache
        cache_key = "delete_operation_json"
        cached_data = memcache_client.get(cache_key)
        if cached_data:
            print("Data Delete diambil dari cache")
            save_to_file('hasil/results.txt', f'Delete: {cached_data} seconds (from cache)')
            return cached_data

        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            # Query untuk operasi delete
            query = """
            DELETE FROM products_json WHERE JSON_EXTRACT(product_data, '$.name') = 'Updated Product'
            """
            start_time = time.time() # Waktu awal eksekusi
            cursor.execute(query)
            connection.commit()
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time

            cursor.close()
            connection.close()

            # Simpan waktu eksekusi ke dalam cache
            memcache_client.set(cache_key, execution_time)

            print(f"Waktu komperasi Delete data {execution_time} seconds")
            save_to_file('hasil/results.txt', f'Delete: {execution_time} seconds')

            # Return waktu eksekusi
            return execution_time

    except Exception as e:
        print("Error:", e)

save_to_file('hasil/results.txt', 'Komparasi DB JSON dengan Caching')
# Panggil fungsi untuk melakukan komparasi operasi insert
compare_insert_operation()

# Panggil fungsi untuk melakukan komparasi operasi update
compare_update_operation()

# Panggil fungsi untuk melakukan komparasi operasi delete
compare_delete_operation()

save_to_file('hasil/results.txt', '----------------------------------------')
