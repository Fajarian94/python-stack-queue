stack=[]

def  tambah_barang(stack, barang_baru):
    stack.append(barang_baru)

    print(" (barang baru) berhasil ditambahkan ke dalam stack.")

def hapus_barang_terakhir(stack):
    if len(stack) ==0:
        print("Stack kosong, tidak ada barang yang dapat dihapus.")
    else:
        barang_terakhir = stack.pop() 
        print(f" (barang terakhir) berhasil dihapus dari stack.")
    
def tampilkan_barang_teratas(stack): 
    if len(stack) ==0:
        print("Stack kosong, tidak ada barang yang dapat ditampilkan.")
    else:
        barang_teratas = stack[-1]
        print("Barang teratas di dalam stack adalah (barang teratas).")
while True:
    print("\nGudang saat ini:", stack)
    print("Menu:") 
    print("1. Tambah Barang")
    print("2. Hapus Barang Terakhir")
    print("3. Tampilkan Barang Teratas")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan Anda (1/2/3/4):")
    if pilihan == "1":
        barang_baru = input("Masukan nama barang yang akan ditambahkan : ")
        tambah_barang(stack, barang_baru)
    elif pilihan == "2":
        hapus_barang_terakhir(stack)
    elif pilihan == "3":
        tampilkan_barang_teratas(stack)
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini")
        break
    else :
        print("Pilihan tidak valid. Silahkan masukan pilihan yang benar")