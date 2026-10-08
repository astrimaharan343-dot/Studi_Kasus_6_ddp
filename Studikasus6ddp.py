import json
import os

path = r"C:\Users\DWI FEBRIANTI\OneDrive\Dokumen\Praktikum\Studikasus6ddp\inventaris.json"
if not os.path.exists(path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

while True:
    print("==================================================") 
    print("        SISTEM MANAJEMEN INVENTARIS DATA          ")
    print("==================================================")
    print("1. Lihat Stok Barang ")
    print("2. Tambah Barang Baru ")
    print("3. Keluar ")

    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == "1":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not data:
            print("Tidak ada data barang.")
        else:
            print("\n--- Stok Barang ---")
            for index, barang in enumerate(data):
                print(f"{index + 1}. Nama: {barang['nama_barang']}, Jumlah: {barang['jumlah']}")

    elif pilihan == "2":
        nama = input("Masukkan nama barang: ")
        jumlah = int(input("Masukkan jumlah barang: "))

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        data.append({"nama_barang": nama, "jumlah": jumlah})

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print("Barang berhasil ditambahkan!")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan sistem manajemen inventaris.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")