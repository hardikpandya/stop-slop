---
name: stop-slop-id
description: Menghapus pola tulisan khas AI dari teks bahasa Indonesia. Gunakan saat menulis, menyunting, atau meninjau teks untuk menghilangkan jejak AI yang gampang ditebak.
metadata:
  trigger: Menulis prosa, menyunting draf, meninjau konten untuk pola AI
  author: M Lintang MZ
  adaptation: Adaptasi bahasa Indonesia dari stop-slop (github.com/hardikpandya/stop-slop)
---

# Stop Slop

Hilangkan pola tulisan khas AI dari teks bahasa Indonesia.

## Aturan Inti

1. **Buang frasa pengisi.** Hapus pembuka basa-basi, penegas kosong, dan penyangat. Lihat [references/phrases.md](references/phrases.md).

2. **Bongkar struktur formulaik.** Hindari kontras biner, daftar negatif, fragmentasi dramatis, pancingan retoris, dan agen palsu. Lihat [references/structures.md](references/structures.md).

3. **Pakai kalimat aktif.** Tiap kalimat butuh subjek manusia yang berbuat. Jangan pakai bentuk pasif. Jangan biarkan benda mati melakukan perbuatan manusia ("keluhan berubah jadi solusi").

4. **Spesifik.** Hindari deklaratif kabur ("Alasannya bersifat struktural"). Sebut hal yang dimaksud. Hindari ekstrem malas ("setiap", "selalu", "tidak pernah") yang bekerja samar. Hindari diksi akademik yang diobral ("signifikan", "implikasi", "krusial") saat kata sederhana lebih pas.

5. **Tempatkan pembaca di ruangan.** Jangan pakai suara narator dari kejauhan. "Anda" lebih baik daripada "orang-orang". Hal konkret mengalahkan abstraksi.

6. **Variasikan irama.** Selang-seling panjang kalimat. Dua butir lebih baik daripada tiga. Akhiri paragraf dengan cara berbeda. Tanpa em dash.

7. **Percayai pembaca.** Sampaikan fakta langsung. Lewati pelembut, pembenaran, dan tuntunan berlebihan.

8. **Buang kalimat pajangan.** Kalau terdengar seperti kutipan poster, tulis ulang.

9. **Hindari calque.** Jangan terjemahkan idiom Inggris kata demi kata ("Di penghujung hari", "Penting untuk dicatat bahwa", "mengeksplorasi lanskap"). Pakai ungkapan Indonesia yang lugas.

10. **Tulis prosa yang mengalir.** Jangan ubah semua jadi bullet dan cetak tebal. Jangan ulang gagasan yang sama dengan kata berbeda.

11. **Patuhi kaidah baku.** Perbaiki pelanggaran EYD yang khas mesin: "namun" di tengah kalimat, "tapi" (jadikan "tetapi"), "di mana"/"yang mana" sebagai penghubung, "Jika ..., maka ..." dalam prosa, dan konjungsi di awal kalimat. Lihat [references/tata-bahasa.md](references/tata-bahasa.md).

12. **Jangan membesar-besarkan.** Buang bahasa brosur ("memesona", "kaya akan", "menyuguhkan") dan klaim peran besar atau warisan tanpa bukti ("tonggak penting", "meninggalkan jejak mendalam"). Sebut fakta spesifik.

13. **Bersihkan jejak salin-tempel.** Hapus bocoran chatbot ("Tentu!", "Semoga membantu", "Berikut adalah"), sangkalan batas pengetahuan, tanda kutip lengkung, sisa Markdown, dan teks pengganti yang lupa diisi.

## Pemeriksaan Cepat

Sebelum menyerahkan tulisan:

- Ada penyangat ("sangat", "benar-benar", "sungguh")? Bunuh.
- Ada kalimat pasif? Temukan pelakunya, jadikan subjek.
- Benda mati melakukan kerja manusia ("keputusan itu muncul")? Sebut orangnya.
- Kalimat dibuka dengan "Apa yang membuat..."? Susun ulang.
- Ada basa-basi "begini/inilah"? Langsung ke poin.
- Ada kontras "bukan X, melainkan Y"? Sampaikan Y langsung.
- Tiga kalimat beruntun sama panjang? Pecah salah satunya.
- Paragraf ditutup kalimat pamungkas? Variasikan.
- Ada em dash? Hapus.
- Deklaratif kabur ("Implikasinya besar")? Sebut implikasi yang spesifik.
- Narator dari kejauhan ("Tak seorang pun merancang ini")? Tempatkan pembaca di adegan.
- Meta-komentar ("Selebihnya akan dibahas di bawah")? Hapus. Biarkan tulisan bergerak.
- Ada "signifikan/implikasi/krusial"? Ganti dengan kata yang lebih lugas.
- Ada calque ("Di penghujung hari", "Penting untuk dicatat bahwa")? Pakai ungkapan Indonesia.
- Tiap kalimat dibuka penghubung ("Selain itu", "Hal ini menunjukkan")? Buang sebagian.
- Semua dipecah jadi bullet dan cetak tebal? Ubah jadi prosa.
- Gagasan yang sama diulang dengan kata beda? Sampaikan sekali.
- Ada "namun" di tengah kalimat? Ganti "tetapi"; "namun"/"akan tetapi" hanya untuk mengawali kalimat baru.
- Ada "tapi" dalam ragam tulis? Jadikan "tetapi".
- Ada "di mana"/"yang mana" sebagai penghubung? Ganti "tempat", "ketika", atau "yang".
- Ada "Jika ..., maka ..." dalam prosa (bukan logika/kode)? Buang "maka", cukup koma.
- Kalimat dibuka "Dan/Sehingga/Karena"? Gabungkan, atau pakai penghubung antarkalimat.
- Judul ditulis Kapital Tiap Kata? Kapitalkan awalnya saja.
- Tulisan ditutup petuah atau pelajaran hidup? Sudahi saat poin selesai.
- Pola tiga ("senyap, hangat, abadi"), tagline "di mana X bertemu Y", atau emoji jadi bullet? Pangkas.
- Bahasa brosur ("memesona", "permai", "menyuguhkan")? Ganti dengan fakta konkret.
- Klaim "tonggak penting", "titik balik", "meninggalkan jejak mendalam"? Buang atau buktikan.
- Kalimat ditutup klausa penilaian ("yang menyoroti...", "sehingga memperkuat...")? Pangkas.
- Kata "adalah" diganti "berperan sebagai/menghadirkan"? Kembalikan ke "adalah/punya".
- Bocoran chatbot ("Tentu!", "Semoga membantu") atau teks pengganti ("[Nama Anda]", "2025-XX-XX")? Hapus.
- Tanda kutip lengkung atau sisa Markdown (**/##/```)? Rapikan.

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

## Ciri Tulisan Manusia

Jangan terlalu agresif sampai tulisan jadi kaku. Hal-hal ini wajar dan boleh dipertahankan:

- "adalah" dan "punya" yang sederhana.
- Kata lugas: "memakai" (bukan "memanfaatkan"), "menulis" (bukan "menggubah"), "mencoba" (bukan "berupaya").
- Pernyataan tegas bila memang benar: "pertama", "satu-satunya", "terbesar".
- Ragu secukupnya: "mungkin", "cenderung", "kira-kira".

## Contoh

Lihat [references/examples.md](references/examples.md) untuk transformasi sebelum/sesudah.

## Lisensi

MIT
