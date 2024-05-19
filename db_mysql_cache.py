import time
import mysql.connector

# Inisialisasi koneksi ke Memcached
from pymemcache.client import base
memcache_client = base.Client(('localhost', 11211))

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

# Fungsi untuk menyimpan hasil eksekusi ke file
def save_to_file(filename, data):
    with open(filename, 'a') as f:
        f.write(data + '\n')

# Fungsi untuk melakukan pengujian operasi insert dengan banyak data
def test_insert_operation():
    try:
        # Cek apakah data ada di cache
        start_time = time.time() 
        cache_key = "insert_operation"
        cached_data = memcache_client.get(cache_key)
        if cached_data:
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time
            print(f"Waktu komperasi Insert data {execution_time} seconds")
            print("Data Insert diambil dari cache")
            save_to_file('results.txt', f'Insert: {execution_time} seconds (from cache)')
            return cached_data

        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            # Query untuk operasi insert
            query = """
            INSERT INTO products (name, price, category, description) 
            VALUES ('New Product', 99, 'Test Category', 'Test Description')
            """
            start_time = time.time() # Waktu awal eksekusi
            for i in range(1000):  # Misalnya, melakukan operasi insert sebanyak 1000 kali
                cursor.execute(query)
            connection.commit()
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time

            cursor.close()
            connection.close()

            # Simpan waktu eksekusi ke dalam cache
            memcache_client.set(cache_key, execution_time)

            print(f"Waktu komperasi Insert data {execution_time} seconds")
            save_to_file('results.txt', f'Insert: {execution_time} seconds')

            # Return waktu eksekusi
            return execution_time

    except Exception as e:
        print("Error:", e)

# Fungsi untuk melakukan pengujian operasi update
def test_update_operation():
    try:
        # Cek apakah data ada di cache
        start_time = time.time() 
        cache_key = "update_operation"
        cached_data = memcache_client.get(cache_key)
        if cached_data:
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time
            print(f"Waktu komperasi Update data {execution_time} seconds")
            print("Data Update diambil dari cache")
            save_to_file('results.txt', f'Update: {execution_time} seconds (from cache)')
            return cached_data

        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            # Query untuk operasi update
            query = """
            UPDATE products SET price = 199 WHERE name = 'New Product'
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
            save_to_file('results.txt', f'Update: {execution_time} seconds')

            # Return waktu eksekusi
            return execution_time

    except Exception as e:
        print("Error:", e)

# Fungsi untuk melakukan pengujian operasi search
def test_search_operation():
    try:
        # Cek apakah data ada di cache
        start_time = time.time() 
        cache_key = "search_operation"
        cached_data = memcache_client.get(cache_key)
        if cached_data:
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time
            print(f"Waktu komperasi Search data {execution_time} seconds")
            print("Data Search diambil dari cache")
            save_to_file('results.txt', f'Search: {execution_time} seconds (from cache)')
            return cached_data

        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            # Query untuk operasi search
            query = """
            SELECT * FROM products WHERE category = 'Test Category'
            """
            start_time = time.time() # Waktu awal eksekusi
            cursor.execute(query)
            products_data = cursor.fetchall()
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time

            cursor.close()
            connection.close()

            # Simpan waktu eksekusi ke dalam cache
            memcache_client.set(cache_key, (execution_time, products_data))

            print(f"Waktu komperasi Search data {execution_time} seconds")
            save_to_file('results.txt', f'Search: {execution_time} seconds')

            # Return waktu eksekusi dan hasil pencarian
            return (execution_time, products_data)

    except Exception as e:
        print("Error:", e)

# Fungsi untuk melakukan pengujian operasi delete
def test_delete_operation():
    try:
        # Cek apakah data ada di cache
        start_time = time.time() 
        cache_key = "delete_operation"
        cached_data = memcache_client.get(cache_key)
        if cached_data:
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time
            print(f"Waktu komperasi Delete data {execution_time} seconds")
            print("Data Delete diambil dari cache")
            save_to_file('results.txt', f'Delete: {execution_time} seconds (from cache)')
            return cached_data

        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            # Query untuk operasi delete
            query = """
            DELETE FROM products WHERE name = 'New Product'
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
            save_to_file('results.txt', f'Delete: {execution_time} seconds')

            # Return waktu eksekusi
            return execution_time

    except Exception as e:
        print("Error:", e)


save_to_file('results.txt', 'Komparasi DB Relasional dengan Caching')
# Panggil fungsi untuk menjalankan pengujian operasi insert dengan banyak data
test_insert_operation()

# Panggil fungsi untuk menjalankan pengujian operasi update
test_update_operation()

# Panggil fungsi untuk menjalankan pengujian operasi search
test_search_operation()

# Panggil fungsi untuk menjalankan pengujian operasi delete
test_delete_operation()

save_to_file('results.txt', '----------------------------------------')
