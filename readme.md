# Panduan Pengembangan Proyek

## Branch

Nama branch menggunakan gaya snake-case:
```
* feature/home-page
* deploy
```

Gunakan awalan pada nama branch sesuai dengan kondisi pekerjaan `<awalan>/<TIKET-JIRA>/<nama-branch>` seperti:
```
// fitur
feature/namaProduct/user-dashboard
// perbaikan
fix/namaProduct/login-error
// refaktor
ref/namaProduct/database-queries
// dokumentasi
docs/namaProduct/api-endpoints
// performa
perf/namaProduct/image-optimization
// gaya
style/namaProduct/responsive-design
dll..
```

## Commit

Baris pertama harus berisi tipe commit, *opsional* scope, dan subjek commit.
Isi pesan berisi deskripsi perubahan yang lebih panjang. Ini digunakan untuk informasi yang tidak muat dalam baris subjek pesan commit. Perhatikan bahwa setiap baris pesan commit tidak boleh lebih dari 72 karakter.
Footer bersifat opsional, dan berisi informasi tambahan untuk commit (misalnya masalah yang diperbaiki, perubahan yang merusak).

Kami menggunakan tipe commit conventional-changelog berikut:
```
feat:     Fitur baru
fix:      Perbaikan bug
docs:     Perubahan hanya pada dokumentasi
style:    Perubahan yang tidak mempengaruhi makna kode (spasi, pemformatan, titik koma yang hilang, dll)
refactor: Perubahan kode yang tidak memperbaiki bug atau menambah fitur
perf:     Perubahan kode yang meningkatkan performa
test:     Menambahkan test yang hilang atau memperbaiki test yang ada
build:    Perubahan yang mempengaruhi sistem build atau dependensi eksternal (contoh scope: gulp, broccoli, npm, gradle, mvn, dll)
ci:       Perubahan pada file konfigurasi CI dan skrip (contoh scope: travis, circle-Ci, jenkins)
chore:    Perubahan lain yang tidak memodifikasi file src atau test
revert:   Mengembalikan commit sebelumnya
```

Format untuk menulis commit adalah sebagai berikut: `<tipe>: <TIKET-JIRA> <deskripsi commit>`

Contoh:
```
git commit -m "fix: PRODUCT-123 menangani error validasi input"
```

---
### Kredit
[Habibi](c) 2023