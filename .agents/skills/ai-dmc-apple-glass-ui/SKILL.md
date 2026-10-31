---
name: ai-dmc-apple-glass-ui
description: Pakai skill ini setiap kali membuat atau mengubah UI frontend AI-DMC (Next.js). Arah desain Apple light + glass: latar abu flat, satu warna aksen, glass hanya untuk elemen kecil yang mengambang.
---

# Panduan Desain UI AI-DMC: Apple Light + Glass

Skill ini jadi acuan tunggal tampilan aplikasi AI-DMC. Diturunkan dari gaya "Apple light + glass capsules" yang sudah disetujui di proyek tim sebelumnya, lalu disesuaikan untuk aplikasi web dan identitas CoE AIIS.

Kalau ragu, pilih yang **lebih sepi**. Aplikasi ini dipakai dosen untuk kerja, bukan untuk dipamerkan.

---

## 1. Prinsip Utama

1. **Tenang dan bersih.** Latar abu Apple flat, banyak ruang kosong, tanpa dekorasi.
2. **Satu warna aksen.** Biru AIIS untuk semua yang bisa diklik. Warna lain hanya untuk status.
3. **Glass punya fungsi.** Dipakai untuk elemen yang mengambang di atas konten (navbar, modal, panel unggah, toast). Kartu konten utama tetap putih solid.
4. **Satu laman, satu tugas utama.** Tombol utama cuma satu per layar.
5. **Dosen tidak mengisi formulir dari nol.** UI menampilkan hasil AI yang sudah terisi, tugas dosen hanya Setujui atau Koreksi.

---

## 2. Design Tokens

Tempel di `frontend/app/globals.css`:

```css
:root {
  /* Latar dan permukaan */
  --bg: #F5F5F7;              /* latar halaman, flat */
  --surface: #FFFFFF;         /* kartu konten */
  --surface-muted: #FAFAFC;   /* baris tabel selang-seling, area sekunder */
  --border: #E5E5EA;          /* garis pemisah tipis */

  /* Teks */
  --ink: #1D1D1F;             /* teks utama */
  --ink-2: #55555A;           /* teks sekunder */
  --ink-3: #86868B;           /* label, keterangan */
  --ink-4: #A1A1A6;           /* placeholder, teks nonaktif */

  /* Aksen tunggal: biru AIIS */
  --accent: #0B7AA0;          /* tombol, link, fokus (kontras 4,8:1 di putih) */
  --accent-hover: #096A8B;
  --accent-soft: #E6F4FA;     /* latar terpilih, highlight lembut */
  --accent-brand: #2AABD2;    /* biru AIIS asli, khusus ikon / ilustrasi, BUKAN teks */

  /* Status (hanya untuk pill status kecil) */
  --st-proses-bg: #F2F2F7;    --st-proses-fg: #55555A;
  --st-verif-bg: #FFF4E5;     --st-verif-fg: #9A5B00;
  --st-ok-bg: #E8F6EE;        --st-ok-fg: #1E7A46;
  --st-tolak-bg: #FDECEC;     --st-tolak-fg: #B3141B;

  /* Merah Telkom: logo dan aksi destruktif saja */
  --telkom-red: #E1252B;

  /* Glass */
  --glass-bg: rgba(255, 255, 255, 0.72);
  --glass-border: rgba(255, 255, 255, 0.9);
  --glass-line: rgba(185, 205, 235, 0.6);   /* garis luar tipis biru keabuan */
  --glass-blur: 20px;

  /* Bentuk dan bayangan */
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 18px;
  --radius-pill: 999px;
  --shadow-card: 0 1px 2px rgba(0,0,0,0.04), 0 4px 16px rgba(0,0,0,0.04);
  --shadow-float: 0 8px 32px rgba(0,0,0,0.08);
}
```

**Kenapa biru, bukan merah Telkom, sebagai aksen?** Di aplikasi, merah dibaca sebagai "bahaya / hapus". Kalau semua tombol merah, tombol Tolak jadi tidak terbedakan. Jadi merah Telkom hanya muncul di logo dan aksi destruktif. Hierarki brand CoE tetap terjaga lewat logo di navbar.

---

## 3. Tipografi

1. **Satu keluarga huruf: Inter** (paling dekat dengan SF Pro Apple, dan sesuai dokumen rancangan). Load lewat `next/font/google`.
2. Skala:

| Peran | Ukuran / Tebal | Contoh pemakaian |
|---|---|---|
| Judul laman | 32px / 700, tracking -0.02em | "Kotak Verifikasi" |
| Judul bagian | 20px / 600 | "Menunggu konfirmasi" |
| Judul kartu | 16px / 600 | Nama dokumen |
| Body | 15px / 400, line-height 1.5 | Isi umum |
| Label / meta | 13px / 500, warna `--ink-3` | "Diunggah 2 jam lalu" |
| Pill / badge | 12px / 600 | Status |

3. Teks tidak pernah di bawah 12px.
4. Judul laman berupa kata benda singkat, bukan kalimat promosi.
5. Angka (skor, jumlah) pakai `font-variant-numeric: tabular-nums`.

---

## 4. Glass: Kapan Boleh, Kapan Tidak

### Boleh
1. **Navbar** sticky di atas.
2. **Modal / sheet** (misalnya form koreksi).
3. **Panel antrean unggah** yang mengambang di pojok bawah.
4. **Toast** notifikasi.
5. **Toolbar filter** yang menempel saat scroll.

### Tidak boleh
1. Kartu dokumen, tabel, atau kartu verifikasi (pakai `--surface` putih solid).
2. Latar seluruh halaman.
3. Glass di atas glass.

### Resep CSS

```css
.glass {
  background: var(--glass-bg);
  backdrop-filter: saturate(180%) blur(var(--glass-blur));
  -webkit-backdrop-filter: saturate(180%) blur(var(--glass-blur));
  border: 1px solid var(--glass-line);
  box-shadow: inset 0 1px 0 var(--glass-border), var(--shadow-float);
}

/* Fallback kalau browser tidak mendukung blur, atau user minta transparansi dikurangi */
@supports not (backdrop-filter: blur(1px)) {
  .glass { background: rgba(255, 255, 255, 0.96); }
}
@media (prefers-reduced-transparency: reduce) {
  .glass { background: rgba(255, 255, 255, 0.98); backdrop-filter: none; }
}
```

Bayangan selalu netral (hitam transparan). **Tidak ada bayangan atau glow berwarna.**

---

## 5. Komponen

### 5.1 Navbar
- Glass, tinggi 56px, sticky.
- Kiri: logo Telkom University + AIIS, lalu teks "AI-DMC" 15px/600.
- Tengah: menu Unggah, Verifikasi (dengan angka badge), Arsip. Menu aktif warna `--accent`, lainnya `--ink-2`.
- Kanan: nama dosen + avatar inisial.
- Di HP: menu pindah ke tab bar bawah (glass juga), 3 ikon + label.

### 5.2 Tombol

| Jenis | Tampilan | Contoh |
|---|---|---|
| Utama | Latar `--accent`, teks putih, radius pill, tinggi 40px | Setujui, Unggah |
| Sekunder | Latar `--accent-soft`, teks `--accent` | Koreksi |
| Teks | Tanpa latar, teks `--accent` | Lihat detail |
| Destruktif | Teks `--telkom-red`, tanpa latar; jadi solid merah hanya di dialog konfirmasi | Tolak |

Hover: gelap sedikit. Fokus keyboard: ring 3px `--accent-soft` + outline 2px `--accent`. Jangan pernah hilangkan outline fokus.

### 5.3 Area Unggah (Dropzone)
- Kartu putih besar, radius `--radius-lg`, garis putus-putus `--border` 1.5px.
- Ikon dokumen sederhana (garis, bukan ilustrasi warna-warni), teks "Seret berkas ke sini atau pilih berkas", keterangan kecil "PDF, DOCX, JPG, PNG".
- Saat berkas diseret di atasnya: garis jadi `--accent`, latar `--accent-soft`.
- Di HP: tombol tambahan "Pindai dengan kamera".

### 5.4 Panel Antrean Unggah
- Glass, mengambang di kanan bawah (HP: sheet dari bawah).
- Tiap berkas satu baris: nama berkas, status teks ("Membaca teks", "Mengklasifikasi", "Selesai"), progress bar tipis 3px warna `--accent`.
- Duplikat: baris dengan teks "Sudah pernah diunggah" warna `--ink-3`, bukan merah.

### 5.5 Pill Status
Radius pill, 12px/600, padding 4px 10px, pakai pasangan warna `--st-*`:
- Diproses (abu), Menunggu verifikasi (oranye lembut), Terverifikasi (hijau lembut), Ditolak (merah lembut), Gagal (merah lembut + ikon).

### 5.6 Indikator Keyakinan AI
- Tampilkan sebagai teks: "Keyakinan AI 91%", di sebelahnya bar tipis 4px.
- Bar `--accent` kalau ≥ 85%, `--st-verif-fg` kalau di bawah.
- Di bawah 85%: tambahkan kalimat kecil "AI kurang yakin, mohon dicek."
- Jangan pakai gauge bulat atau speedometer.

### 5.7 Kartu Verifikasi (komponen terpenting)
Layout dua kolom di desktop, bertumpuk di HP:
1. **Kiri:** pratinjau dokumen (thumbnail halaman pertama), klik untuk perbesar.
2. **Kanan:**
   - Nama berkas (16px/600) + pill status.
   - Indikator keyakinan.
   - Klasifikasi: Kategori › Subkategori › Jenis, ditulis sebagai satu baris breadcrumb.
   - Metadata dalam daftar label-nilai (label `--ink-3` 13px, nilai `--ink` 15px). Field kosong ditulis "Tidak ditemukan" warna `--ink-4`, bukan dikosongkan.
   - Tombol: **Setujui** (utama), Koreksi (sekunder), Tolak (destruktif teks). Urutan dari kanan: Setujui paling kanan.

### 5.8 Form Koreksi
- Muncul sebagai sheet/modal glass.
- Semua field sudah terisi hasil AI. Field yang diubah dosen diberi titik kecil `--accent` di sampingnya.
- Kategori, subkategori, jenis pakai dropdown dari endpoint `/taxonomy`.
- Input: latar putih, border `--border`, radius `--radius-sm`, tinggi 40px, fokus border `--accent`.

### 5.9 Daftar Arsip
- Toolbar filter (glass, sticky): segmented control kategori (Semua, PND, PNL, PKM, PUB, PNJ, ADM) + dropdown status + tahun.
- Isi: tabel di dalam kartu putih. Kolom: Nama dokumen, Jenis, Tanggal terbit, Status. Baris tinggi 52px, garis pemisah `--border`, hover `--surface-muted`.
- Di HP: tabel berubah jadi daftar kartu.

### 5.10 Empty State
- Ikon garis sederhana abu, satu kalimat, satu tombol.
- Contoh: "Belum ada dokumen yang perlu dicek." Tanpa ilustrasi kartun.

### 5.11 Toast
- Glass, muncul di atas tengah, hilang 3 detik.
- Contoh: "Dokumen disetujui dan masuk arsip." Sertakan tombol "Urungkan" untuk aksi Setujui/Tolak.

---

## 6. Layout Laman

| Laman | Isi utama |
|---|---|
| Login | Kartu putih di tengah lebar 380px, logo di atas, 2 input, 1 tombol. Latar `--bg` polos. |
| Unggah | Judul laman, dropzone besar, di bawahnya "Unggahan terakhir" (5 item). Panel antrean mengambang. |
| Kotak Verifikasi | Judul + jumlah ("4 dokumen menunggu"), daftar kartu verifikasi bertumpuk. |
| Arsip Saya | Judul, toolbar filter, tabel. |

Grid:
1. Lebar konten maksimum 1080px, di tengah.
2. Padding samping 24px desktop, 16px HP.
3. Jarak antar elemen kelipatan 4px (8, 12, 16, 24, 32, 48).
4. Tidak ada scroll horizontal di HP.

---

## 7. Gerak (Motion)
1. Durasi 150 sampai 250ms, easing `cubic-bezier(0.25, 0.1, 0.25, 1)`.
2. Yang boleh bergerak: hover tombol, munculnya modal/sheet (fade + naik 8px), toast, progress bar.
3. Hormati `prefers-reduced-motion`: matikan animasi non-esensial.
4. Tidak ada animasi berulang (pulse, shimmer berlebihan). Skeleton loading boleh, abu `--surface-muted` statis atau shimmer sangat halus.

---

## 8. Ikon
- Satu set saja: **Lucide** (`lucide-react`), stroke 1.75, ukuran 18 atau 20px.
- Warna ikon ikut teks di sebelahnya. Ikon bukan dekorasi, selalu ada label teksnya.

---

## 9. Larangan (biar tidak kelihatan "AI banget")

1. Gradien aurora, mesh gradient, blob, atau glow berwarna di latar.
2. Lebih dari satu warna aksen (misalnya biru + ungu + oranye sekaligus).
3. Glass di semua tempat, terutama kartu konten.
4. Deretan kartu identik dengan ikon di lingkaran warna-warni.
5. Emoji di UI.
6. Teks promosi ("Revolusi pengelolaan dokumen!"). Pakai bahasa kerja yang lugas.
7. Em-dash di copy.
8. Font lebih dari satu keluarga.
9. Ilustrasi kartun atau maskot.
10. Shadow tebal atau shadow berwarna.

---

## 10. Copywriting UI
1. Bahasa Indonesia baku tapi santai, kalimat pendek.
2. Tombol pakai kata kerja: Unggah, Setujui, Koreksi, Tolak, Simpan.
3. Istilah konsisten di semua laman: "Kotak Verifikasi", "Arsip Saya", "Keyakinan AI". Jangan ganti-ganti sinonim.
4. Pesan error menjelaskan apa yang harus dilakukan: "Format berkas tidak didukung. Gunakan PDF, DOCX, JPG, atau PNG."

---

## 11. Checklist Sebelum PR UI
1. Hanya pakai token dari Bagian 2, tidak ada warna hex baru di komponen.
2. Glass hanya di elemen yang tercantum di Bagian 4.
3. Kontras teks minimal 4,5:1 (cek pakai DevTools).
4. Dicek di lebar 375px (HP) dan 1280px (desktop), tidak ada yang terpotong atau scroll horizontal.
5. Bisa dipakai pakai keyboard saja (Tab, Enter, Esc), outline fokus terlihat.
6. Tidak melanggar satu pun larangan di Bagian 9.
7. Screenshot desktop + HP dilampirkan di PR.
