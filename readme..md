# Proyek Deteksi Koin dengan Streamlit dan OpenCV

## Tujuan Proyek

Proyek ini bertujuan untuk mendeteksi koin dalam video secara real-time menggunakan kombinasi Streamlit dan OpenCV. Dengan aplikasi ini, Anda dapat mengatur threshold deteksi dan area koin melalui sidebar Streamlit dan melihat hasil deteksi langsung dari kamera.

## Instruksi Penggunaan

1. **Persiapan Lingkungan**:
   - Pastikan Anda memiliki Python 3.6 atau lebih baru terinstal di sistem Anda.
   - Buat lingkungan virtual (opsional tetapi disarankan) dan aktifkan:
     ```bash
     python -m venv venv
     source venv/bin/activate  # Untuk macOS/Linux
     venv\Scripts\activate     # Untuk Windows
     ```

2. **Instalasi Dependensi**:
   - Instal semua paket yang diperlukan dengan menggunakan `requirements.txt`. Jika file `requirements.txt` belum ada, Anda bisa membuatnya dengan perintah berikut:
     ```bash
     pip freeze > requirements.txt
     ```
   - Instal dependensi dengan:
     ```bash
     pip install -r requirements.txt
     ```

3. **Menjalankan Aplikasi**:
   - Pastikan Anda memiliki webcam yang terhubung ke komputer Anda.
   - Jalankan aplikasi dengan perintah:
     ```bash
     streamlit run app.py
     ```
   - Akses aplikasi melalui browser di URL yang ditampilkan oleh Streamlit.

4. **Pengaturan**:
   - Gunakan slider di sidebar untuk mengatur nilai `Threshold 1` dan `Threshold 2` untuk deteksi tepi.
   - Atur nilai area minimum dan maksimum untuk berbagai denominasi koin di sidebar.

## Penjelasan Kode

- **`VideoTransformer`**: Kelas ini mengatur pemrosesan video dan deteksi koin. Anda dapat mengatur parameter threshold dan area koin di sidebar.
- **`preProcessing`**: Fungsi ini melakukan pra-pemrosesan gambar dengan Gaussian blur, deteksi tepi, dan operasi morfologi.
- **`transform`**: Fungsi utama yang memproses setiap frame video, mendeteksi koin, dan mengukur area mereka.
- **`get_logs`**: Fungsi ini mengumpulkan log deteksi yang dapat ditampilkan di aplikasi.

## Ucapan Terima Kasih

Terima kasih telah menggunakan proyek ini! Semoga aplikasi ini bermanfaat untuk Anda. Jika Anda memiliki pertanyaan atau saran, silakan hubungi saya di muhammadalvi.23339@mhs.unesa.ac.id atau buka isu di Alvi399.

© 2024 Muhammad Alvi Kirana Zulfan Nazal. Semua hak cipta dilindungi.

## Lisensi

Proyek ini dilisensikan di bawah [Lisensi MIT](https://opensource.org/licenses/MIT).
