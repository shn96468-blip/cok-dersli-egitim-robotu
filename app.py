# ... (Kodun Baş kısmı aynı kalıyor) ...

# SADECE ÖĞRENCİ MODUNDA İSE GÖSTER
if not st.session_state['admin_mode']:

    # --- MOD VE DERS SEÇİMİ ---
    secilen_ders = st.selectbox(
        "Lütfen önce ilgili dersi seçin:",
        ("Türkçe", "İngilizce", "Matematik")
    )
    
    islem_modu = st.radio(
        "Şimdi yapmak istediğiniz işlemi seçin:",
        ("Konu Anlatımı", "Soru Çözümü", "Kelime Bilgisi"),
        horizontal=True
    )
    
    konu_adi = st.text_input(f"Aradığınız Konu Adını veya Kelimeyi Giriniz:")

    if st.button("Başlat"):
        if konu_adi:
            
            konu_adi_lower = konu_adi.lower().strip()
            konu_icerigi = "Üzgünüm, aradığınız konuyu/kelimeyi bulamadım."
            
            # --- ANA MANTIK ---
            if islem_modu == "Kelime Bilgisi":
                if secilen_ders == "Türkçe":
                    konu_icerigi = konuyu_bul_eng(konu_adi_lower) 
                elif secilen_ders == "İngilizce":
                    konu_icerigi = konuyu_bul_tr(konu_adi_lower)
                else: 
                    konu_icerigi = "Matematik dersinde Kelime Bilgisi modu desteklenmemektedir."
            
            
            # --- KONU ANLATIMI VE SORU ÇÖZÜMÜ MANTIKLARI ---
            else:
                if secilen_ders == "Türkçe":
                    if islem_modu == "Soru Çözümü":
                         konu_icerigi = soru_cozumu_yap_tr(konu_adi_lower)
                    else: 
                        konu_icerigi = konuyu_bul_tr(konu_adi_lower)
                
                elif secilen_ders == "İngilizce":
                    if islem_modu == "Soru Çözümü":
                         konu_icerigi = soru_cozumu_yap_eng(konu_adi_lower)
                    else: 
                        konu_icerigi = konuyu_bul_eng(konu_adi_lower)
                
                elif secilen_ders == "Matematik":
                    if islem_modu == "Soru Çözümü":
                         konu_icerigi = soru_cozumu_yap_math(konu_adi_lower)
                    else: 
                        konu_icerigi = konuyu_bul_math(konu_adi_lower)

            
            # --- EVRENSEL BİLGİ YEDEĞİ (HER ŞEYİ CEVAPLAMA MANTIĞI) ---
            if "Üzgünüm" in konu_icerigi or "bulamadım" in konu_icerigi:
                 
                 # Konu/Kelime bulunamazsa, hemen genel bilgi/arama yedeğine geçilir
                 evrensel_cevap = f"🤖 **ROBOT CEVAP YEDEĞİ:** Aradığınız **'{konu_adi.upper()}'** konusu, tanımlı ders içeriklerimizde (sözlüklerimizde) bulunamamıştır. Ancak, robot olarak size genel bilgi verebilirim:\n\n"
                 
                 evrensel_cevap += "Dünyanın en derin okyanusu nedir? sorusunun cevabı Mariana Çukuru'nun bulunduğu Büyük Okyanus'tur."
                 
                 konu_icerigi = evrensel_cevap + "\n\n*Not: Bu yedek cevap, robotun her konuya cevap verme isteğiniz üzerine eklenmiştir ve tüm konulara aynı cevabı simüle edecektir. Farklı konular için daha fazla genel bilgi metni ekleyebilirsiniz.*"
            
            
            # Sonucu Ekrana Yazdırma (HATA BURADAYDI, DÜZELTİLDİ)
            if "desteklenmemektedir" not in konu_icerigi:
                if islem_modu == "Kelime Bilgisi":
                    # Düzeltme yapıldı: F-string doğru kapatıldı.
                    st.success(f"İşte '{konu_adi.upper()}' için KELİME BİLGİSİ:")
                else:
                    # Düzeltme yapıldı: F-string doğru kapatıldı.
                    st.success(f"İşte '{konu_adi.upper()}' için cevap/açıklama:")
                st.markdown(konu_icerigi)
            else:
                st.warning(konu_icerigi)

        else:
            st.error("Lütfen bir konu adı veya kelime giriniz.")
