# english_content.py
KONULAR_ENG = {
    # BURAYA EN AZ 1 KONU BAŞLIĞI OLMALI
    "simple present tense": "⭐ Simple Present Tense: Geniş zamandır. Günlük rutinler ve genel gerçekler için kullanılır. (I go, She goes).",
    "modals can": "Yetenek (ability) ve izin (permission) bildirir. (I can swim).",
}

def konuyu_bul_eng(arama_terimi):
    if arama_terimi in KONULAR_ENG:
        return f"🇬🇧 ENGLISH TOPIC EXPLANATION:\n{KONULAR_ENG[arama_terimi]}"
    else:
        # Kelime Bilgisi modunda kullanıldığı için daha genel bir cevap döndürür.
        return f"Üzgünüm, aradığınız '{arama_terimi}' kelimesi tanımlı bir İngilizce konu başlığı değildir. Lütfen farklı bir konu deneyin."

def soru_cozumu_yap_eng(arama_termi):
    return "❓ Example Question Solution (English): The solution uses the rules of Tenses and Modals."
    
