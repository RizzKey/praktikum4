
  
nilai = []
perulangan = True

while perulangan:
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    nilaiTugas = int(input("Masukkan Nilai Tugas: "))
    nilaiUts = int(input("Masukkan Nilai UTS: "))
    nilaiUas = int(input("Masukkan Nilai UTS: "))
    nilaiAkhir = (nilaiTugas * 30/100) + (nilaiUts * 35/100) + (nilaiUas * 35/100)

    nilai.append([nama, nim, nilaiTugas, nilaiUts, nilaiUas, int(nilaiAkhir)])
    if (input("Tambah data (y/t)? ") == 't'):
        perulangan = False

print("\n                      DAFTAR NILAI MAHASISWA                    ")
print("==================================================================")
print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
print("==================================================================")
i = 0
for item in nilai:
    i += 1
    print("| {no:2d} | {nama:12s} | {nim:9s} | {nilaiTugas:5d} | {nilaiUts:5d} | {nilaiUas:5d} | {nilaiAkhir:6.2f} |"
          .format(no=i, nama=item[0], nim=item[1], nilaiTugas=item[2], nilaiUts=item[3], nilaiUas=item[4], nilaiAkhir=item[5]))
print("==================================================================")
