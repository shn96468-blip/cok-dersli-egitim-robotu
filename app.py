# SADECE ÖĞRENCİ MODUNDA İSE GÖSTER
if not st.session_state['admin_mode']:

    # --- MOD VE DERS SEÇİMİ (KARTLAR ŞEKLİNDE) ---
    st.header("📚 Ders Seçimi")

    # Kartları Streamlit sütunları ile oluşturma
    col_tr, col_eng, col_mat, col_sohbet = st.columns(4)

    # DERSLERİN TANIMLARI
    DERSLER = [
        {"isim": "Türkçe", "simgesi": "🇹🇷", "kolon": col_tr},
        {"isim": "İngilizce", "simgesi": "🇬🇧", "kolon": col_eng},
        {"isim": "Matematik", "simgesi": "📐", "kolon": col_mat},
        {"isim": "Sohbet ve Çeviri", "simgesi": "💬", "kolon": col_sohbet},
    ]

    # Seçim mekanizması için bir session state değişkeni
    if 'secilen_ders' not in st.session_state:
        st.session_state['secilen_ders'] = None

    # Kartları çizme döngüsü
    for ders in DERSLER:
        with ders["kolon"]:
            if st.button(f"{ders['simgesi']} {ders['isim']}", key=f"btn_{ders['isim']}", use_container_width=True):
                st.session_state['secilen_ders'] = ders['isim']
                st.rerun() 

    st.markdown("---")
    
    secilen_ders = st.session_state['secilen_ders'] # Artık seçili ders buradan geliyor

    if secilen_ders:
        st.subheader(f"✅ Seçili Ders: {secilen_ders}")
        
        # --- Sohbet modu seçilirse farklı bir arayüz göster ---
        if secilen_ders == "Sohbet ve Çeviri":
            # Sohbet kodu buraya devam edecek
            # ...
            # ...
