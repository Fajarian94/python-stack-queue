stack = []

def tambah_buku(stack,buku) :
    stack.append(buku)
    print(f'{buku} Buku baru telah ditambahkan!')

def menghapus_buku(stack) :
    if len(stack)== 0:
        print('Stack kosong! tidak dapat menghapus buku')
    else:
        buku_terakhir = stack.pop() 
        print(f" {buku_terakhir} berhasil dihapus dari stack.")
    
def tampilkan_buku_teratas(stack): 
    if len(stack) ==0:
        print("Stack kosong, tidak ada buku yang dapat ditampilkan.")
    else:
        buku_teratas = stack[-1]
        print(f"Barang teratas di dalam stack adalah {buku_teratas}")
while True :
    print("\nstack saat ini:", stack)
    print("Menu:") 
    print("1. Tambah Buku")
    print("2. Hapus Buku Terakhir")
    print("3. Tampilkan Buku Teratas")
    print("4. Keluar")

    pilihan = input('Masukan Pilihan Anda maseh (1/2/3/4) : ')

    if pilihan == "1" :
        buku = input ('Masukan Judul Buku dan pengarangnya (contoh : (Nama Buku - Nama Pengarang )) yang akan di tambahkan : ')
        tambah_buku (stack, buku)
    elif pilihan == "2" :
        menghapus_buku(stack)
    elif pilihan == "3" :
        tampilkan_buku_teratas(stack)
    elif pilihan == "4" :
        print("Terimakasih, Sampai Jumpa. ")
        break
    else :
        print(" Pilihan Tidak Valid. Silahkan masukan pilihan yang benar")
         
