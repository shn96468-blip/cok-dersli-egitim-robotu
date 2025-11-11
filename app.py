# MÜZİK KONTROLÜ
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎶 Müzik ve Ses Ayarları")
    
    # Yeni Müzik Seçeneği: Dinamik URL Girişi
    
    # 1. Müzik URL'leri
    MUSIC_OPTIONS = {
        "Ders Çalışma Müzik 1 (Varsayılan)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "Piyano Melodisi": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "Hafif Tekno Ritim": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
        "Özel Şarkı Linki Gir": "CUSTOM_URL", # Yeni seçenek
        "Müzik Kapalı (Ses URL'sini Kaldır)": ""
    }

    yeni_music_izin = st.sidebar.checkbox("Fon Müziğini Aç", st.session_state['music_enabled'])
    if yeni_music_izin != st.session_state['music_enabled']:
        st.session_state['music_enabled'] = yeni_music_izin
        st.rerun()

    secilen_sarki_adi = st.sidebar.selectbox(
        "Çalınacak Şarkıyı Seçin:",
        options=list(MUSIC_OPTIONS.keys())
    )
    
    # 2. Dinamik URL Girişi
    yeni_url = MUSIC_OPTIONS[secilen_sarki_adi]
    
    if secilen_sarki_adi == "Özel Şarkı Linki Gir":
        custom_url_input = st.sidebar.text_input("Şarkınızın MP3 Linkini Buraya Yapıştırın:", key="custom_music_url_input")
        if custom_url_input:
             yeni_url = custom_url_input
        else:
             st.sidebar.warning("Lütfen geçerli bir MP3 linki girin.")
             yeni_url = "" # Eğer link yoksa, URL'yi boş bırak

    if yeni_url != st.session_state['music_url']:
        st.session_state['music_url'] = yeni_url
        # Rerun'u sadece URL değiştiğinde yapalım
        if st.session_state['music_enabled']:
             st.rerun()
        
    st.sidebar.caption("Müzik açıldığında, hem yönetici hem de öğrenci modunda çalacaktır.")
    st.sidebar.markdown("---")

    st.sidebar.button("🔒 YÖNETİCİ ÇIKIŞI", on_click=admin_logout)
else:
