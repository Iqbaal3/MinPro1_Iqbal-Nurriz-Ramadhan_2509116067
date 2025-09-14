# MinPro1_Iqbal-Nurriz-Ramadhan_2509116067
Iqbal Nurriz Ramadhan_2509116067

Mini Project yang saya buat disini adalah Program "Pelacak Asupan Kalori & Protein Harian"
Sesuai dengan namanya program ini bertujuan menghitung jumlah Kalori & Protein yang telah di konsumsi. 
Program ini bermanfaat untuk orang orang yang sedang melakukan Bulking ataupun Cutting (Diet)
Cara kerjanya yaitu pengguna Memilih diantara 4 perintah yang di sediakan pada Menu Utama yaitu Tambah, List, Hapus, Selesai.

1. Fitur tambah
   Untuk Menambah Makanan yang di konsumsi
2. Fitur List
   Berfungsi melihat daftar/list makanan yang di konsumsi
3. Fitur Hapus
   Yaitu agar pengguna dapat menghapus makanan yang telah di tambahkan pada daftar/list
4. Fitur Selesai
   Menyelesaikan program serta menampilkan Total Asupan Kalori & Protein.

Program ini memuat sistem Create, Read, dan Delete. Yang dimana pengguna dapat menginput maupun menghapus data/list yang telah ada.

Berikut FlowChart dari Program "Pelacak Asupan Kalori& Protein Harian" :



Penjelasan Alur:

1. Alur di (Mulai)
2. Data_makanan merupakan Dictionary yang memuat data nama makanan yang berpasangan dengan data kalori, dan protein. (menggunakan dictionary karena memudahkan untuk perhitungan nantinya)
3. Konsumsi Merupakan Sebuah List kosong yang dapat di tambah maupun di hapus
4. Program akan menampilkan menu utama yang berisi Keterangan untuk tiap perintah yaitu: tambah, List, Hapus, Dan Selesai.
5. Pengguna di minta untuk menginput Perintah
6. Jika Perintah adalah/bernilai  "Selesai" maka akan masuk ke perhitungan :
a. mendeklarasikan sebuah variabel untuk Total Kalori = 0 dan Total Protein = 0
b. lalu akan masuk ke program loop, yang dimana program akan mendeteksi apakah terdapat variabel nama, berat dalam list konsumsi.
c. jika iya maka untuk tiap-tiap pasangan data (nama) di data_makanan akan diberi variabel Kalori per 100g dan Protein per 100g. program akan menghitung kalori dengan Kalori = Kalori per 100 g * berat / 100. dan menghitung protein dengan Protein = kalori per 100 g * berat / 100. lalu menjumlahkan Kalori dengan Total Kalori += Kalori dan Total Protein += Kalori. digunakannya += agar saat proses loop nilai dari Variabel Total Kalori ataupun Protein tidak kemabli ke 0.
d. Jika tidak maka program akan langsung menampilkan Total Asupan kalori & protein. dan program (Selesai)
7. Jika Perintah adalah/bernilai "Hapus" maka akan masuk ke tampilan menu hapus yaitu : 
a. program mendeklarasikan bahwa variabel i(untuk penomoran) = 0
b. Jika i lebih dari jumlah anggota yang ada di list konsumsi maka akan lanjut, namun jika tidak maka akan menampilkan bahwa belum ada makanan yang di konsumsi dan kembali ke Menu utama karena adanya looping while di awal. 
c. saat Lanjut program melakukan loop untuk i yang berada pada rentang 0 hingga (jumlah anggota konsumsi) maka akan print/menampilkan tiap i+1 dengan nama, dan berat hingga sejumlah dengan anggota konsumsi dan program akan stop melakukan looping.
d. program meminta inputan dari pengguna yang nilainya di simpan di variabel Nomor dan dikurangi 1 agar sama/sesuai dengan indeks pada list dan memudahkan user.
e. lalu jika 0 <= Nomor < jumlah anggota Konsumsi maka akan menghapus salah satu anggota konsumsi yang sesuai dengan nilai Nomor menggunakan fungsi/fitur pop. misal pengguna menginput 1 maka Nomor = 1-1 = 0, lalu konsumsi.pop(0). dan menyimpan anggota konsumsi yang terhapus ke dalam list/variabel Terhapus
f. setelah itu program akan menampilkan/print teks berupa konfirmasi bahwa anggota konsumsi yang Terhapus telah dihapus menggunakan Terhapus[0] sebanyak terhapus[1] gram telah dihapus.
g. setelah itu program akan kembali ke menu utama karena adanya looping while.
8. Jika perintah bernilai "Tambah" maka program akan masuk ke tampilan menu tambah
a. loop untuk tiap variabel makanan di data_makanan, akan di deklarasikan pasangannya menjadi sebuah variabel baru yaitu kalori dan protein
b. lalu menampilkan/print makanan, kalori & protein.
c. jika sistem telah print seluruh makanan, maka loop akan terputus dan lanjut.
d. pengguna menginput makanan
e. jika makanan bernilai "Selesai" maka akan kembali ke menu utama.
f. jika makanan nilainya ada di data_makanan makan akan lanjut ke menginput berat.
g. jika berat yang di input kurang dari 0 maka akan menampilkan tulisan bahwa berat harus di atas 0 gram. lalu kembali ke penginputan nilai karena ada fungsi loop while di dalam menu tambah
h. jika berat lebih dari 0 maka lanjut dan menambahkan makanan yg di input ke list konsumsi dengan fungsi append
i. lalu program mengkonfirmasi jika makanan dan berat telah di tambahkan.
10. Jika Perintah adalah/bernilai "List", maka akan masuk ke perulangan.
a. untuk setiap nama, berat yang ada di makanan akan di tampilkan hingga tidak ada lagi. dan loop akan berhenti lalu lanjut ke Menu Utama karena ada loop While.




