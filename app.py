 # 3. DERS SEÇİMİ (KARTLAR ŞEKLİNDE)
    st.header("📚 Ders Seçimi")

    # DERSLERİN TANIMLARI (Tüm 6 ders + Çeviri)
    # Kart görselindeki gibi 4'erli iki satır oluşturuyoruz.
    col_din, col_fen, col_eng, col_mat = st.columns(4)
    col_tarih, col_tr, col_cevir, col_bos = st.columns(4)

    DERSLER = [  # <-- Bu satırın varlığı ŞART
        {"isim": "Din Kültürü", "simgesi": "🕌", "kolon": col_din},
        {"isim": "Fen Bilimleri", "simgesi": "🔬", "kolon": col_fen},
        {"isim": "İngilizce", "simgesi": "🇬🇧", "kolon": col_eng},
        {"isim": "Matematik", "simgesi": "📐", "kolon": col_mat},
        {"isim": "Tarih", "simgesi": "🏛️", "kolon": col_tarih},
        {"isim": "Türkçe", "simgesi": "🇹🇷", "kolon": col_tr},
        {"isim": "Anlık Çeviri", "simgesi": "🔄", "kolon": col_cevir},
    ] # <-- Bu satırın varlığı ŞART
    
    for ders in DERSLER:
        with ders["kolon"]:
            if st.button(f"{ders['simgesi']} {ders['isim']}", key=f"btn_{ders['isim']}", use_container_width=True):
                st.session_state['secilen_ders'] = ders['isim']
                st.rerun()
