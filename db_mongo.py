import time
from pymongo import MongoClient

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

# Fungsi untuk melakukan pengujian operasi dengan 1000 data
def test_operation(operation_name, operation_function):
    try:
        db = connect_to_database()
        if db is not None:
            start_time = time.time() # Waktu awal eksekusi
            operation_function(db)
            end_time = time.time() # Waktu akhir eksekusi
            execution_time = end_time - start_time

            print(f"Waktu komperasi {operation_name} data {execution_time} seconds")
            save_to_file('hasil/results.txt', f'{operation_name}: {execution_time} seconds')
        else:
            print("Error: Gagal terhubung ke database")
    except Exception as e:
        print("Error:", e)

# Fungsi untuk operasi insert
def insert_operation(db):
    products = []
    for i in range(1000):
        products.append({
            "name": "New Product",
            "price": 99,
            "category": "Test Category",
            "description": "Test Description"
        })
    db.products.insert_many(products)

# Fungsi untuk operasi update
def update_operation(db):
    products = []
    for i in range(1000):
        products.append({
            "name": "New Product",
            "price": 199,
            "category": "Test Category",
            "description": "Test Description"
        })
    for product in products:
        db.products.update_many(
            {"name": product["name"]},
            {"$set": {"price": product["price"]}}
        )
        
# Fungsi untuk operasi delete
def delete_operation(db):
    products = []
    for i in range(1000):
        products.append({
            "name": "New Product",
            "price": 199,
            "category": "Test Category",
            "description": "Test Description"
        })
    for product in products:
        db.products.delete_many({"name": product["name"]})

save_to_file('hasil/results.txt', 'Komparasi Mongo DB tanpa Caching')
# Panggil fungsi untuk menjalankan pengujian operasi insert dengan banyak data
test_operation("Insert", insert_operation)

# Panggil fungsi untuk menjalankan pengujian operasi update
test_operation("Update", update_operation)

# Panggil fungsi untuk menjalankan pengujian operasi delete
test_operation("Delete", delete_operation)

save_to_file('hasil/results.txt', '----------------------------------------')
