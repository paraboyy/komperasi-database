import time
from pymongo import MongoClient
from pymemcache.client import base

# Inisialisasi koneksi ke Memcached
memcache_client = base.Client(('localhost', 11211))

# Fungsi untuk mendapatkan koneksi ke database MongoDB
def connect_to_database():
    try:
        client = MongoClient('localhost', 27017)
        return client['e_commerce']
    except Exception as e:
        print("Error:", e)

# Fungsi untuk menyimpan hasil eksekusi ke dalam file
def save_to_file(filename, data):
    with open(filename, 'a') as f:
        f.write(data + '\n')

# Fungsi untuk melakukan pengujian operasi insert dengan banyak data
def test_insert_operation():
    try:
        db = connect_to_database()
        if db is not None:
            # Query untuk operasi insert
            start_time = time.time() # Waktu awal eksekusi
            for i in range(1000):  # Misalnya, melakukan operasi insert sebanyak 1000 kali
                db.products.insert_one({
                    "name": "New Product",
                    "price": 99,
                    "category": "Test Category",
                    "description": "Test Description"
                })
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time

            print(f"Waktu komperasi Insert data {execution_time} seconds")
            save_to_file('results.txt', f'Insert: {execution_time} seconds')
        else:
            print("Error: Gagal terhubung ke database")
    except Exception as e:
        print("Error:", e)

# Fungsi untuk melakukan pengujian operasi update
def test_update_operation():
    try:
        db = connect_to_database()
        if db is not None:
            # Query untuk operasi update
            start_time = time.time() # Waktu awal eksekusi
            db.products.update_many(
                {"name": "New Product"},
                {"$set": {"price": 199}}
            )
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time

            print(f"Waktu komperasi Update data {execution_time} seconds")
            save_to_file('results.txt', f'Update: {execution_time} seconds')
        else:
            print("Error: Gagal terhubung ke database")
    except Exception as e:
        print("Error:", e)

# Fungsi untuk melakukan pengujian operasi search
def test_search_operation():
    try:
        db = connect_to_database()
        if db is not None:
            # Query untuk operasi search
            start_time = time.time() # Waktu awal eksekusi
            products_data = db.products.find({"category": "Test Category"})
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time

            print(f"Waktu komperasi Search data {execution_time} seconds")
            save_to_file('results.txt', f'Search: {execution_time} seconds')
        else:
            print("Error: Gagal terhubung ke database")
    except Exception as e:
        print("Error:", e)

# Fungsi untuk melakukan pengujian operasi delete
def test_delete_operation():
    try:
        db = connect_to_database()
        if db is not None:
            # Query untuk operasi delete
            start_time = time.time() # Waktu awal eksekusi
            db.products.delete_many({"name": "New Product"})
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time

            print(f"Waktu komperasi Delete data {execution_time} seconds")
            save_to_file('results.txt', f'Delete: {execution_time} seconds')
        else:
            print("Error: Gagal terhubung ke database")
    except Exception as e:
        print("Error:", e)

save_to_file('results.txt', 'Komparasi Mongo DB dengan Caching')
# Panggil fungsi untuk menjalankan pengujian operasi insert dengan banyak data
test_insert_operation()

# Panggil fungsi untuk menjalankan pengujian operasi update
test_update_operation()

# Panggil fungsi untuk menjalankan pengujian operasi search
test_search_operation()

# Panggil fungsi untuk menjalankan pengujian operasi delete
test_delete_operation()
save_to_file('results.txt', '----------------------------------------')
