# Data makanan: nama makanan : kalori , protein (per 100g)
data_makanan = {
    "nasi": (130, 2.7),
    "ayam": (240, 27),
    "ubi": (110, 2),
    "telur": (155, 13),
    "tahu": (76, 8),
    "tempe": (193, 20),
    "apel": (52, 0.3),
    "pisang": (89, 1.1),
}

# List konsumsi (masih kosong)
konsumsi = []

#Mulai Program
while True:

    print("===============================================")
    print("++++++++++++++++++Perintah+++++++++++++++++++++")
    print("Tambah  : Tambah makanan yang di konsumsi ")
    print("List    : Lihat makanan yang sudah ditambahkan ")
    print("Hapus   : Hapus makanan dari list ")
    print("Selesai : Akhiri dan lihat total")
    print("===============================================")

    perintah = input("Masukkan perintah: ")
    #Kondisi Slesai
    if perintah == "Selesai":
        break

    #Perintah Hapus
    elif perintah == "Hapus":
        i = 1
        if i < len(konsumsi):
            for i in range(len(konsumsi)):
                nama, berat = konsumsi[i]
                print(f"{i + 1} {nama}: {berat} gram")
            
            nomor = int(input("Masukkan nomor makanan yang ingin dihapus: ")) - 1
            if 0 <= nomor < len(konsumsi):
                terhapus = konsumsi.pop(nomor)
                print(f"{terhapus[0]} sebanyak {terhapus[1]} gram telah dihapus.")
            else:
                print("Nomor tidak valid")
        else:
            Print("Belum ada makanan yang diinput")
        continue

    #Perintah Tambah Makanan
    elif perintah == "Tambah":
        print("=================================================")
        print("Daftar Makanan Beserta Kalori & Protein")
        for makanan in data_makanan:
            kalori, protein = data_makanan[makanan]
            print(f"- {makanan}: {kalori} kalori, {protein}g protein")

        while True:    
            makanan = input("Masukkan nama makanan (Ketik 'Selesai' untuk berhenti): ")
            if makanan == "Selesai" :
                break
            if makanan in data_makanan :    
                berat = float(input("Masukkan berat makanan dalam gram (contoh: 100): "))
                if berat > 0:
                    konsumsi.append((makanan, berat))
                    print(f"{makanan} sebanyak {berat} gram berhasil ditambahkan.")
                else:
                    print("Maaf, Berat harus lebih dari 0 gram")
                continue
            else :
                print("Maaf, Makanan tidak ditemukan dalam daftar progam")
        continue       

        #Perintah List Makanan
    elif perintah == "List":
        print("Daftar makanan yang dikonsumsi:")
        for nama, berat in konsumsi:
            print(f"- {nama} sebanyak {berat} gram")
    
    else:
        print("Perintah tidak Valid")
        continue

#Hitung total kalori dan protein
total_kalori = 0
total_protein = 0

for nama, berat in konsumsi:
    kalori_per_100g, protein_per_100g = data_makanan[nama]
    kalori = kalori_per_100g * berat / 100
    protein = protein_per_100g * berat / 100
    total_kalori += kalori
    total_protein += protein

# TOTAL
print(" ======================")
print(" Total Asupan Hari Ini ")
print(" ======================")
print("================================")
print(f"Kalori : {total_kalori} Kalori")
print(f"Protein: {total_protein} Gram")

