# AI-DMC · Application Engineer

Aplikasi pengelolaan dokumen CoE AIIS. Checkout ini mengerjakan bagian **Orang 2**: database, API, frontend, adapter pipeline, audit dan dokumentasi. Pipeline OCR/LLM dan taksonomi resmi tetap milik Orang 1.

**Mode awal adalah mock**, ditampilkan sebagai simulasi pada aplikasi. Berkas tidak benar-benar diklasifikasi AI dalam mode ini.

## Menjalankan dengan Docker Compose

Prasyarat: Docker Desktop dengan Compose. Dari root proyek:

```powershell
Copy-Item .env.example .env
# Edit .env: ganti JWT_SECRET, POSTGRES_PASSWORD dan SEED_PASSWORD.
# Jika password database berubah, sesuaikan DATABASE_URL juga.
docker compose up --build -d
docker compose exec backend python -m app.seed
```

Frontend: [localhost:3000](http://localhost:3000). Backend: [localhost:8000/health](http://localhost:8000/health), dokumentasi API: [localhost:8000/docs](http://localhost:8000/docs).

Semua akun demo memakai password SEED_PASSWORD dari environment. Nama akun dan cara setup tanpa Docker dijelaskan dalam [README backend](backend/README.md). Akun seed hanya untuk development. Detail frontend tersedia dalam [README frontend](frontend/README.md).

Port layanan diikat ke localhost untuk pengembangan. Deployment ke jaringan kampus memerlukan konfigurasi host, HTTPS, origin, rahasia baru, backup dan akses server yang disepakati tim. Perubahan NEXT_PUBLIC_API_URL memerlukan build ulang frontend.

## Dokumen dan batas pekerjaan

- [Rancangan yang disetujui](docs/superpowers/specs/2026-10-31-application-engineer-design.md).
- [Rencana implementasi](docs/superpowers/plans/2026-10-31-application-engineer.md).
- [Wireframe desktop dan HP](docs/wireframe/README.md).
- [Panduan dosen](docs/PANDUAN_DOSEN.md).
- [Handoff dan status verifikasi](docs/HANDOFF.md).

Skema memakai **5 tabel** sesuai klarifikasi pengguna: users, documents, dokumen_dosen, koreksi, audit_log.

## Data lokal

Jangan commit data dosen atau dokumen asli. data/, storage/, .env, database lokal, dependency dan hasil pengujian lokal sudah di-ignore. Gunakan dokumen sintetis untuk demo.

## Pemeriksaan

Jalankan pengujian backend dan production build frontend sesuai README masing-masing. Docker tidak tersedia pada lingkungan implementasi awal; keberhasilan test lokal tidak menggantikan pengujian migrasi PostgreSQL atau Compose. Hasil aktual dicatat dalam docs/HANDOFF.md.
