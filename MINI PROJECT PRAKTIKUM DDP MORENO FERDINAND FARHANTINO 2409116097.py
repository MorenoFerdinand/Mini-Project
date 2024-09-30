# NAMA  : MORENO FERDINAND FARHANTINO
# NIM   : 2409116097
# KELAS : SISTEM INFORMASI C

# LOGIN SEDERHANA
while True:
    Nama = input("Masukkan Nama Anda = ")
    NIM = input("Masukkan NIM Anda = ")
    PRODI = input("Masukkan PRODI Anda = ")
    print("Selamat Datang: " + str(Nama))
    print("NIM Anda: " + str(NIM))
    print("PRODI Anda: " + str(PRODI))
    print("________________________________________")
    break

# PERULANGAN =
while True:
    JamKerja = float(input("Masukkan Data Jam Kerja = "))
    TarifKerja = float(input("Masukkan Tarif Kerja = Rp. "))

# Menghitung Gaji Dari Tarif Kerja di X Jam Kerja
    Gaji = JamKerja * TarifKerja

    if JamKerja > 160:
        Bonus = Gaji * 0.1
        GajiTotal = Gaji + Bonus
        print("Selamat Anda Mendapatkan Bonus sebesar 10%. Jadi Total Gaji Anda = " + str(GajiTotal))
    else:
        print("Maaf Anda Tidak Mendapatkan Bonus. Jadi Total Total Gaji Anda = " + str(Gaji))
    
    # PERULANGAN
    Ulang = input("Lanjutkan Transaksi Lain atau Tidak?(Y,/T): ")
    if(Ulang) == ("T"):
        print("Terima Kasih")
        break
    Ulang = input("Silahkan Melanjutkan Transaksi Lain: ")
    if(Ulang) == ("Y"):
        print("Terima Kasih")
        break