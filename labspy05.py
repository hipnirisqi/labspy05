data = {}

print ("╔═════════════════════════════════════════════════════════════════════════╗")
print ("╠════════════════════ PROGRAM INPUT DATA MAHASISWA ═══════════════════════╣")
print ("╠═══════════╦════════════╦════════════╦═════════════╦══════════╦══════════╣")
print ("║(T)ambah   ║   (U)bah   ║ (H)apus    ║  (C)ari     ║  (L)ist  ║(K)eluar  ║")
print ("╚═══════════╩════════════╩════════════╩═════════════╩══════════╩══════════╝")

while True:

    c = input("\nPilih Opsi: ")

# KELUAR PROGRAM
    if c.lower() == 'q':
        break

# PRINT DATA
    elif c.lower() == 'l':
        print ("\n╔═════════════════════════════════════════════════════════════════════════╗")
        print ("╠═════════════════════════ DAFTAR DATA MAHASISWA ═════════════════════════╣")
        print ("╠════╦═════════════════╦══════════════════╦═══════╦═══════╦═══════╦═══════╣")
        print ("║ NO ║      NAMA       ║       NIM        ║ TUGAS ║  UTS  ║  UAS  ║ AKHIR ║")
        print ("╠════╬═════════════════╬══════════════════╬═══════╬═══════╬═══════╬═══════╣")
        no = 1
        for tabel in data.values():
            print ("║{0:3} ║ {1:15} ║ {2:16} ║ {3:5} ║ {4:5} ║ {5:5} ║ {6:5} ║"
              .format(no, tabel[0],tabel[1], tabel[2],tabel[3], tabel[4], tabel[5]))
            no += 1
        print ("╚════╩═════════════════╩══════════════════╩═══════╩═══════╩═══════╩═══════╝")
        print ("\n    (T)ambah       (U)bah      (H)apus     (C)ari      (L)ist     (K)eluar   ")


# MENAMBAH DATA
    elif c.lower() == 't':
        print ("\n════Masukan Data Mahasiswa════")

        while (True):
            nama = input("NAMA : ")
            if nama == '':
                print ('Nama tidak boleh kosong')
            else:
                break
        while (True):
            try:
                nim  = int(input("NIM  : "))
                if nim == '':
                    print ('Masukan Nim Anda')
            except ValueError:
                print ('Masukan Nim Anda')
            else:
                break
        while (True):
            try:
                tugas  = int(input("TUGAS  : "))
                if tugas == '':
                    print ('Masukan Nilai TUGAS')
            except ValueError:
                print ('Masukan Nilai TUGAS')
            else:
                break
        while (True):
            try:
                uts  = int(input("UTS  : "))
                if uts == '':
                    print ('Masukan Nilai UTS')
            except ValueError:
                print ('Masukan Nilai UTS')
            else:
                break
        while (True):
            try:
                uas  = int(input("UAS  : "))
                if uas == '':
                    p('Masukan Nilai UAS')
            except ValueError:
                print ('Masukan Nilai UAS')
            else:
                break
        akhir = round((float(tugas) * 0.3)+(float(uts) * 0.35)+(float(uas) * 0.35),2)
        data[nama] = [nama,nim,tugas,uts,uas,akhir]

        print ("\n    (T)ambah       (U)bah      (H)apus     (C)ari      (L)ist     (K)eluar   ")


# UBAH DATA
    elif c.lower() == 'u':
        nama = input("Masukan nama untuk ubah data : ")

        if nama in data.keys():
            del data[nama]
            print ("\n═══Masukan Pembaruan Data═══")

            while (True):
                nama = input("NAMA  : ")
                if nama == '':
                    print ('Nama tidak boleh kosong')
                else:
                    break
            while (True):
                try:
                    nim = int(input("NIM   : "))
                    if nim == '':
                        print ('Masukan Nilai Nim')
                except ValueEarror:
                    print ('Masukan Nilai Nim')
                else:
                    break
            while (True):
                try:
                    tugas = int(input("TUGAS    : "))
                    if tugas == '':
                        print ('Masukan Nilai TUGAS')
                except ValueError:
                    print ('Masukan Nilai TUGAS')
                else:
                    break
            while (True):
                try:
                    uts = int(input("UTS   : "))
                    if uts == '':
                        print ('Masukan Nilai UTS')
                except ValueError:
                    print ('Masukan Nilai UTS')
                else:
                    break
            while (True):
                try:
                    uas = int(input("UAS   : "))
                    if uas == '':
                        print ('Masukan Nilai UAS')
                except ValueError:
                    print ('Masukan Nilai UAS')
                else:
                    break
            akhir = round((float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35), 2)
            data[nama] = [nama, nim, tugas, uts, uas, akhir]

        else:
            print (" ________________________")
            print ("| Data {} tidak ditemukan |".format(nama))
            print (" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print ("\n    (T)ambah       (U)bah      (H)apus     (C)ari      (L)ist     (K)eluar   ")



# MENCARI DATA
    elif c.lower() == 'c':
        nama = input("Masukan nama yang di cari : ")
        if nama in data.keys():

            print ("\n╔═════════════════╦══════════════════╦═══════╦═══════╦═══════╦═══════╗")
            print ("║      NAMA       ║       NIM        ║ TUGAS ║  UTS  ║  UAS  ║ AKHIR ║")
            print ("╠═════════════════╬══════════════════╬═══════╬═══════╬═══════╬═══════╣")
            print ("║ {0:15} ║ {1:16} ║ {2:5} ║ {3:5} ║ {4:5} ║ {5:5} ║".format(nama, data[nama][1],data[nama][2], data[nama][3],data[nama][4], data[nama][5]))
            print ("╚═════════════════╩══════════════════╩═══════╩═══════╩═══════╩═══════╝")
        else:
            print (" ________________________")
            print ("| Data {} tidak ditemukan |".format(nama))
            print (" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

        print ("\n  (T)ambah       (U)bah      (H)apus     (C)ari      (L)ist     (K)eluar      ")

# HAPUS DATA
    elif c.lower() == 'h':
        nama = input("Masukan nama untuk menghapus data : ")
        if nama in data.keys():
            del data[nama]
            print ("Data {} dihapus".format(nama))
        else:
            print (" ________________________")
            print ("| Data {} tidak ditemukan |".format(nama))
            print (" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

        print ("\n    (T)ambah       (U)bah      (H)apus     (C)ari      (L)ist     (K)eluar ")


    else:
        print (" __________________________")
        print ("| Pilih opsi yang tersedia |")
        print (" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print ("    (T)ambah       (U)bah      (H)apus     (C)ari      (L)ist     (K)eluar   ")

 
