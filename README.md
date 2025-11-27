Nama : Febryvia Deya Nur Havidtar Murti Aqsa

NIM : 312510194

Kelas : TI.25.A.2

Mata Kuliah : Pengantar Pemrograman

Pertemuan : 11


##PRAKTIKUM 6

1. Melatih penggunaan lambda function

2. Memahami cara kerja fungsi matematika dasar dalam bentuk lambda

3. Melatih membaca dan menjelaskan kode

4. Mengasah logika program melalui fungsi sederhana


##Latihan 1

Mengubah fungsi menggunakan lambda

Fungsi a = lamba = x: x**2

Tujuan: Menghitung kuadrat dari x

Input: Menerima satu argumen string

Proses: Mengalikan x dengan dirinya sendiri (x**2)

a =  lambda x: x**2 : Menghitung kuadrat dari x

b = lambda x,y: math.sqrt(x**2 + y**2) :  Menghitung (hipotenusa) teorema pythagoras

c = lambda *args: sum(args) / len(args) : Menghitung rata-rata dari banyak angka

d = lambda s: "".join(set(s)) : Menghapus huruf-huruf yang duplikat, mengambil sebuah string, dan mengembalikan string baru dalam urutan tidak di tentukan

Output yang dihasilkan 

print(a(7)) : proses menghitung 7² #Hasil ouput 49

print(a(-3)) : proses menghitung (-3)² #Hasil output 9

print(a(2.5)) : proses menghitung (2.5)² #Hasil output 6.25

print("hello python") : Mencetak string secara langsung

Hasilnya :

<img width="1441" height="527" alt="Screenshot 2025-11-27 170317" src="https://github.com/user-attachments/assets/c86f3609-9edc-4547-bf87-42bb47cc7b9a" />


##Praktikum

Program Daftar Nilai Mahasiswa

1. Tambah data mahasiswa

2. Tampilkan semua data

3. Hapus data berdasarkan nama

4. Ubah data berdasarkan nama

5. Keluar program


Fungsi utama yang harus dibuat:

tambah () : Menambah data (Meminta input Nama dan Nilai mahasiswa baru, lalu memnyimpannya ke dalam struktur data utama)

tampilkan () : Menampilkan data (Menampilkan seluruh daftar nama dan  nilai mahasiswa yang tersimpan)

hapus (nama) : Menghapus data (Menerima input nama dan mencari data mahasiswa yang sesuai)

ubah (nama) : Mengubah data (Menerima  input nama dan mencari data mahasiswa)

#Fungsi tambah()

1. Meminta pengguna memasukkan Nama mahasiswa

2. Meminta pengguna memasukkan Nilai mahasiswa.

3. Buat dictionary baru: {"nama": Nama, "nilai": Nilai}.

4. Tambahkan dictionary ini ke data_mahasiswa

5. Tampilkan ("Data berhasil ditambahkan") 

#Fungsi tampilkan()

1. Cek apakah data_mahasiswa kosong

2. Jika tidak kosong, lakukan perulangan (loop) melalui list dan cetak nama serta nilai dari setiap mahasiswa

3. Tampilkan ("Daftar Nilai Mahasiswa")

#Fungsi hapus(nama)

1. Lakukan perulangan melalui data_mahasiswa.

2. Meminta cek apakah mahasiswa['nama'] sama dengan nama yang dicari.

3. Jika sama, hapus elemen tersebut dari list (gunakan del atau metode pop()).

4. Setelah ditemukan dan dihapus, segera hentikan perulangan (gunakan break).

#Fungsi ubah(nama)

1. Lakukan perulangan melalui data_mahasiswa.

2. Meminta cek apakah mahasiswa['nama'] sama dengan nama yang dicari.

3. Jika sama, minta input Nilai Baru.

4. Perbarui mahasiswa['nilai'] = Nilai_Baru.

5. Hentikan perulangan (break)

##Struktur Kode
- `data_mahasiswa`: List of dictionaries untuk menyimpan data.
- Fungsi `tambah()`, `tampilkan()`, `hapus(nama)`, `ubah(nama)`: Implementasi fitur utama.
- `main()`: Fungsi utama dengan loop menu

Langkah algoritma

1. Mulai

2. Tampilkan menu
  
3. Pilih menu (1-5)

4. Jika memilih 1 akan menambahkan data

5. Input nama dan nilai

6. Simpan dan kembali ke menu

7. Jika memilih 2 akan menampilkan data

9. Tampilkan seluruh data

10. Kembali ke menu

11. Jika memilih 3 akan hapus data

12. Input nama

13. Hapus Data jika nama ada

14. Tampilkan status hapus dan kembali ke menu

15. Jika memilih 4 maka ubah data

16. Input nama

17. Ubah nama dan nilai

18. Tampilkan status ubah dan kembalil ke menu

19. Jika memilih 5 akan keluar dari program

20. Selesai

#Flowchart :

```
                   +-------------------+
                   |       START       |
                   +---------+---------+
                             |
                             v
                   +-------------------+
                   |   Tampilkan Menu  |
                   +-------------------+
                             |
                             v
                   +-------------------+
                   |  Pilih Menu (1-5) |
                   +---------+---------+
                             |
     ---------------------------------------------------------
     |           |             |                |            |
     v           v             v                v            v
+---------+  +---------+   +---------+     +---------+   +---------+
|   1     |  |    2    |   |    3    |     |    4    |   |    5    |
+---------+  +---------+   +---------+     +---------+   +---------+
|Tambah   |  |Tampilkan|   |Hapus    |     |Ubah     |   | Keluar  |
|Data     |  |Data     |   |Data     |     |Data     |   |Program  |
+----+----+  +----+----+   +----+----+     +----+----+   +----+----+
     |           |             |                |             |
     v           v             v                v             v
+---------+  +---------+   +---------+     +---------+   +---------+
|Input    |  |Tampilkan|   |Input    |     |Input    |   |  END    |
|Nama &   |  |Seluruh  |   |Nama     |     |Nama     |   +---------+
|Nilai    |  |Data     |   +----+----+     +----+----+
+----+----+  +----+----+        |               |
     |           |              v               v
     v           |       +-------------+   +-------------+
+---------+      |       |Hapus Data   |   |Ubah Nama &  |
|Simpan   |      |       |Jika Nama Ada|   |Nilai        |
|Data     |      |       +------+------+   +-------------+
+----+----+      |              |                 |
     |           |              v                 v
     v           v      +-------------+   +-------------+
+---------+  +---------+|Tampilkan    |   |Tampilkan    |
|Kembali  |  |Kembali  | |Status Hapus|   |Status Ubah  |
|ke Menu  |  |ke Menu  | +-------------+ +-------------+
+---------+  +---------+        |                 |
                                -------------------
                                          |
                                          v
                                 +-------------------+
                                 |   Kembali ke Menu |
                                 +-------------------+
```

Hasilnya:

<img width="1613" height="887" alt="Screenshot 2025-11-27 172624" src="https://github.com/user-attachments/assets/932b2865-0578-443a-94a8-5862538daa00" />

<img width="1424" height="886" alt="Screenshot 2025-11-27 172640" src="https://github.com/user-attachments/assets/7e5d531b-4eb4-4f17-97f8-9ae17df45157" />


 Commit dan push URL:

<img width="1423" height="976" alt="Screenshot 2025-11-27 174427" src="https://github.com/user-attachments/assets/ef9a2c07-f597-407d-b2e3-bb1a5de9bdf1" />

