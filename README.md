# Stop Slop

Skill untuk menghapus jejak AI dari tulisan bahasa Indonesia.

## Apa Ini

Tulisan AI punya pola: frasa yang gampang ditebak, struktur seragam, irama yang itu-itu saja. Skill ini mengajari Claude (atau LLM mana pun) menangkap dan membuang pola itu dari teks bahasa Indonesia.

## Struktur Skill

```
stop-slop-id/
├── SKILL.md              # Instruksi inti
├── references/
│   ├── phrases.md        # Frasa yang harus dibuang
│   ├── structures.md     # Pola struktur yang dihindari
│   ├── examples.md       # Transformasi sebelum/sesudah
│   └── tata-bahasa.md    # Kaidah EYD/PUEBI yang sering dilanggar
├── README.md
└── LICENSE
```

## Mulai Cepat

**Claude Code:** Tambahkan folder ini sebagai skill.

**Claude Projects:** Unggah `SKILL.md` dan berkas referensi ke pengetahuan proyek.

**Instruksi khusus:** Salin aturan inti dari `SKILL.md`.

**Panggilan API:** Sertakan `SKILL.md` di system prompt. Berkas referensi dimuat saat dibutuhkan.

## Apa yang Ditangkap

**Frasa terlarang**: Pembuka basa-basi, penegas kosong, jargon korporat, diksi akademik yang diobral, bahasa promosi, bocoran chatbot, semua penyangat, deklaratif kabur, meta-komentar. Lihat `references/phrases.md`.

**Klise struktural**: Kontras biner, daftar negatif, pola tiga, pembesaran makna, analisis tempelan, fragmentasi dramatis, pancingan retoris, tagline klise, penutup berpetuah, agen palsu, calque, kata penghubung yang dipaksakan, pola format bertele-tele, jejak salin-tempel, kalimat pasif. Lihat `references/structures.md`.

**Aturan tingkat kalimat**: Tanpa pembuka "Apa yang membuat...", tanpa em dash, tanpa fragmentasi tersendat, tanpa ekstrem malas, wajib kalimat aktif.

**Kaidah baku**: Pelanggaran EYD yang khas mesin, seperti "namun" di tengah kalimat, "tapi" alih-alih "tetapi", "di mana"/"yang mana" sebagai penghubung, "Jika ..., maka ..." dalam prosa, serta "yang" dan konjungsi di awal kalimat. Lihat `references/tata-bahasa.md`.

## Penilaian

Beri nilai 1-10 untuk tiap dimensi:

| Dimensi | Pertanyaan |
|---------|-----------|
| Kelugasan | Menyatakan langsung atau cuma mengumumkan? |
| Irama | Bervariasi atau seperti metronom? |
| Kepercayaan | Menghargai kecerdasan pembaca? |
| Keaslian | Terdengar seperti tulisan manusia? |
| Kepadatan | Ada yang masih bisa dipangkas? |

Di bawah 35/50: revisi.

## Penulis

[M Lintang MZ](https://github.com/mlintangmz2765)

Adaptasi bahasa Indonesia dari [stop-slop](https://github.com/hardikpandya/stop-slop) oleh Hardik Pandya.

## Lisensi

MIT. Pakai bebas, sebarkan luas.
