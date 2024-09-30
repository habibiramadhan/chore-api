# Dokumentasi API

## URL Dasar
http://localhost:8000

## Autentikasi
Semua endpoint dalam API ini memerlukan autentikasi melalui token JWT. Anda dapat memperoleh token dengan melakukan login dengan kredensial yang valid.

### Mendapatkan Token
**POST** /auth/token

**Body Permintaan** (form-data):
```plaintext
username=testuser&password=testpassword
```

**Contoh `curl`:**
```bash
curl -X POST http://localhost:8000/auth/token \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=testuser&password=testpassword"
```

**Respons**:
```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

## Endpoint

1. Daftar Pengguna
**POST** `/auth/register`

**Deskripsi**: Mendaftar pengguna baru. Jika nama pengguna sudah digunakan, akan mengembalikan error 400.

**Body Permintaan**:
```json
{
  "username": "string",
  "password": "string"
}
```

**Contoh `curl`:**
```bash
curl -X POST http://localhost:8000/auth/register \
-H "Content-Type: application/json" \
-d '{ "username": "testuser", "password": "testpassword" }'
```

**Respons**:
```json
{
  "username": "testuser",
  "is_active": true
}
```

2. Ambil Pengguna Saat Ini
**GET** `/auth/me`

**Deskripsi**: Mengambil informasi pengguna yang sedang terautentikasi.

**Header**:
```plaintext
Authorization: Bearer your_jwt_token
```

**Contoh `curl`:**
```bash
curl -X GET http://localhost:8000/auth/me \
-H "Authorization: Bearer your_jwt_token"
```

**Respons**:
```json
{
  "username": "testuser",
  "is_active": true
}
```

3. Rute Terlindungi
**GET** `/auth/protected`

**Deskripsi**: Mengakses rute terlindungi yang memerlukan autentikasi yang valid.

**Header**:
```plaintext
Authorization: Bearer your_jwt_token
```

**Contoh `curl`:**
```bash
curl -X GET http://localhost:8000/auth/protected \
-H "Authorization: Bearer your_jwt_token"
```

**Respons**:
```json
{
  "message": "You have access to this protected route"
}
```

## Respons Error
* **400 Bad Request**: Dikembalikan saat terjadi kesalahan validasi atau permintaan tidak sesuai.
   * Contoh: Pengguna mencoba mendaftar dengan nama pengguna yang sudah ada.
* **401 Unauthorized**: Dikembalikan saat token hilang, tidak valid, atau telah kedaluwarsa.
   * Contoh: Mengakses endpoint yang dilindungi tanpa token atau dengan token yang tidak valid.
* **404 Not Found**: Dikembalikan saat sumber daya yang diminta tidak ditemukan.
   * Contoh: Mengakses endpoint yang tidak ada.

