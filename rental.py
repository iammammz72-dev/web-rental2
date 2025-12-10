# Sistem Rental / Sewa Barang Sederhana

barang = ["Kamera", "Tripod", "Laptop", "Proyektor"]
barang_disewa = []

def tampilkan_menu():
    print("\n=== SISTEM RENTAL BARANG ===")
    print("1. Lihat daftar barang")
    print("2. Sewa barang")
    print("3. Kembalikan barang")
    print("4. Lihat barang yang sedang disewa")
    print("5. Keluar")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        print("\nDaftar Barang:")
        for i, b in enumerate(barang):
            print(f"{i+1}. {b}")

    elif pilihan == "2":
        print("\nBarang yang tersedia:")
        for i, b in enumerate(barang):
            print(f"{i+1}. {b}")

        pilih = int(input("Pilih nomor barang yang disewa: ")) - 1
        
        if 0 <= pilih < len(barang):
            disewa = barang.pop(pilih)
            barang_disewa.append(disewa)
            print(f"Anda menyewa: {disewa}")
        else:
            print("Pilihan tidak valid!")

    elif pilihan == "3":
        print("\nBarang yang disewa saat ini:")
        for i, b in enumerate(barang_disewa):
            print(f"{i+1}. {b}")

        pilih = int(input("Pilih nomor barang yang dikembalikan: ")) - 1

        if 0 <= pilih < len(barang_disewa):
            kembali = barang_disewa.pop(pilih)
            barang.append(kembali)
            print(f"Anda mengembalikan: {kembali}")
        else:
            print("Pilihan tidak valid!")

    elif pilihan == "4":
        print("\nBarang yang sedang disewa:")
        if len(barang_disewa) == 0:
            print("Tidak ada barang yang disewa.")
        else:
            for b in barang_disewa:
                print("- " + b)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan sistem rental!")
        break

    else:
        print("Menu tidak dikenal!")
