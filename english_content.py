# english_content.py
# İngilizce Tenses ve Temel Kelime Bilgisi

KONULAR_ENG = {
    "simple present tense": "⭐ Simple Present Tense: Geniş zamandır. Günlük rutinler, alışkanlıklar ve genel gerçekler için kullanılır. (Örnek: I go to school every day).",
    "modals can": "Modal 'Can', yetenek (ability) ve izin (permission) bildiren bir yardımcı fiildir. (Örnek: She can speak three languages).",
    "present continuous": "Şimdiki zamandır. Şu anda yapılan eylemleri anlatır. (Örnek: They are watching a movie now).",
    "vocabulary": "Vocabulary (Kelime Bilgisi), bir dilde iletişim kurmak için hayati önem taşır. Yeni kelimeler öğrenmek, dil becerilerini geliştirir.",
    "again": "Again kelimesinin Türkçe karşılığı 'tekrar', 'yeniden' veya 'bir daha' demektir. (Örnek: Please come again - Lütfen tekrar gel).",
}

def konuyu_bul_eng(arama_terimi):
    arama_terimi = arama_terimi.lower().strip()
    if arama_terimi in KONULAR_ENG:
        return f"🇬🇧 ENGLISH TOPIC EXPLANATION:\n\n{KONULAR_ENG[arama_terimi]}"
    else:
        # Kelime Bilgisi modu da bu fonksiyonu kullanır.
        return f"Üzgünüm, aradığınız '{arama_terimi}' İngilizce konu başlığı tanımlı değildir."

def soru_cozumu_yap_eng(arama_termi):
    arama_termi = arama_termi.lower().strip()
    return "❓ Example Question Solution (English): The solution uses the rules of Tenses, Modals, and subject-verb agreement."
