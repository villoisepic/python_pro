meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lolucon",
            "SHEESH": "sedikit ketidak setujuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "AGGRO": "menbuat orang marah"
            }
word = input("Ketikan kata yang tidak di mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print("kata di temukan :)")
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("kata tidak di temukan :(")
