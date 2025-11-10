# app.py dosyasında, 170. satır civarındaki general_chat_kanka fonksiyonu:

def general_chat_kanka(kullanici_mesaji):
    mesaj_lower = kullanici_mesaji.lower().strip()

    # Kanka Sohbeti Mantığı
    if "merhaba" in mesaj_lower or "selam" in mesaj_lower or "kanka" in mesaj_lower:
        cevap = "Selam! Ben senin yapay zeka kankanım. Ders mi çalışalım yoksa güncel bir konudan mı konuşalım?"
    elif "nasılsın" in mesaj_lower:
        cevap = "Çok iyi çalışıyorum, teşekkür ederim! Peki sen nasılsın, dersler nasıl gidiyor?"
    elif "teşekkür" in mesaj_lower or "sağol" in mesaj_lower:
        cevap = "Rica ederim, ne zaman istersen buradayım!"
    elif "ders" in mesaj_lower or "çalışmak" in mesaj_lower or "ödev" in mesaj_lower:
        cevap = "Harika! Hangi dersle ilgili bir sorunun var? Veya hangi konudan başlayayım?"
    else:
        cevap = f"Anladım, '{kullanici_mesaji}' ilginç bir konu! Ama biliyorsun, benim uzmanlık alanım eğitim. Ders kartlarından birini seçerek ilerleyelim mi?"

    return cevap
    
