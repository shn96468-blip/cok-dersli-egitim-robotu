# --- SOHBET VE ÇEVİRİ MANTIKLARI (GÜNCELLENMİŞ) ---
def sohbet_ve_cevir(kullanici_mesaji):
    mesaj_lower = kullanici_mesaji.lower().strip()
    
    # Basit Sözlük (Çeviri Simülasyonu İçin)
    basit_sozluk = {
        "merhaba": "Hello", "selam": "Hi", "teşekkürler": "Thanks", "sağol": "Thanks",
        "elma": "Apple", "armut": "Pear", "kedi": "Cat", "köpek": "Dog",
        "apple": "Elma", "pear": "Armut", "cat": "Kedi", "dog": "Köpek",
        "again": "Tekrar / Yine",
        "teach": "Öğretmek", "study": "Çalışmak", "kitap": "Book", "kalem": "Pen"
    }

    # 1. Hazır Cevaplar (Sohbet)
    if "merhaba" in mesaj_lower or "selam" in mesaj_lower:
        cevap = "Merhaba! Ben yapay zeka destekli eğitim robotuyum. Nasıl yardımcı olabilirim?"
    elif "adın ne" in mesaj_lower or "kimsin" in mesaj_lower:
        cevap = "Ben Yusuf Efe Şahin tarafından geliştirilen Çok Dersli Eğitim Robotuyum."
    elif "teşekkür" in mesaj_lower or "sağol" in mesaj_lower:
        cevap = "Rica ederim, her zaman buradayım!"
        
    # 2. Basit Çeviri Simülasyonu
    elif "çevir" in mesaj_lower or "translate" in mesaj_lower or any(kelime in mesaj_lower for kelime in basit_sozluk):
        
        # Kelimeyi bulmaya çalış
        cevirilecek_kelime = ""
        for kelime_tr, kelime_eng in basit_sozluk.items():
            if kelime_tr in mesaj_lower and kelime_tr != mesaj_lower: # Cümlenin içinde arama
                cevirilecek_kelime = kelime_tr
                break
            if kelime_eng.lower() in mesaj_lower and kelime_eng.lower() != mesaj_lower:
                cevirilecek_kelime = kelime_eng.lower()
                break
            
        # Tam kelime eşleşmesi kontrolü (Sadece 'again' yazarsa)
        if mesaj_lower in basit_sozluk:
             cevirilecek_kelime = mesaj_lower

        if cevirilecek_kelime:
            # Çeviri yap
            if cevirilecek_kelime in basit_sozluk: # İngilizce ise Türkçe karşılığını bul
                 cevap = f"Kelime: {cevirilecek_kelime.title()}. Türkçe Çevirisi: **{basit_sozluk[cevirilecek_kelime]}**."
            elif cevirilecek_kelime in [v.lower() for v in basit_sozluk.values()]: # Türkçe ise İngilizce karşılığını bul
                # Değeri (İngilizce) anahtar (Türkçe) üzerinden bulmak için ters arama yapılır
                tr_karsilik = next(k for k, v in basit_sozluk.items() if v.lower() == cevirilecek_kelime)
                cevap = f"Kelime: {cevirilecek_kelime.title()}. İngilizce Çevirisi: **{tr_karsilik}**."
            else:
                 cevap = f"'{kullanici_mesaji}' ifadesi için çeviri simülasyonu yapıldı. Daha fazla kelime eklenmelidir."
        else:
             cevap = f"'{kullanici_mesaji}' ifadesi için çeviri simülasyonu yapıldı. Gerçek bir dil modeli ile anlık çeviri yapabilirim."

    # 3. Genel Cevaplar (Eğitim)
    else:
        cevap = f"Anladım, '{kullanici_mesaji}' hakkında bilgi istiyorsunuz. Lütfen yukarıdaki menüden dersinizi ve işlem modunu seçerek detaylı bilgi almayı deneyin."
        
    st.session_state.chat_history.append({"user": kullanici_mesaji, "robot": cevap})
    return cevap
