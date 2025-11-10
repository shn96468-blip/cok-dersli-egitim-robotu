# Bu dosya, İngilizce konularını ve genel kelime çeviri mantığını içerir.
KONULAR_ENG = {
    "simple present tense": "⭐ Simple Present Tense: Geniş zamandır. Günlük rutinler ve genel gerçekler için kullanılır. (I go, She goes).",
    "present continuous tense": "Şimdiki zamandır. Şu anda yapılan eylemler için kullanılır. (I am going, She is going).",
    "future tense will": "Gelecek zamandır. Anlık kararlar ve tahminler için kullanılır. (I will go).",
    "modals can": "Yetenek (ability) ve izin (permission) bildirir. (I can swim).",
    "modals must": "Zorunluluk (obligation) bildirir. (You must study).",
    "adjectives": "Sıfatlardır. İsimleri niteler. (A big house).",
    "adverbs": "Zarflardır. Fiilleri, sıfatları veya başka zarfları niteler. (He runs quickly).",
}

def konuyu_bul_eng(arama_terimi):
    if arama_terimi in KONULAR_ENG:
        return f"🇬🇧 ENGLISH TOPIC EXPLANATION:\n{KONULAR_ENG[arama_terimi]}"
    else:
        return f"🇬🇧 KELİME ÇEVİRİSİ / EK BİLGİ:\n\nAradığınız '{arama_terimi}' kelimesi, İngilizce sözlüğümüzde tanımlı bir konu değildir. Ancak bu kelime, genel bir kelime olarak kabul edilmiştir. (Örn: 'Apple' kelimesi Türkçe'de 'Elma' demektir). Lütfen tam bir cümle veya konu başlığı yazarak tekrar deneyin."

def soru_cozumu_yap_eng(arama_termi):
    return "❓ Example Question Solution (English): The solution uses the rules of Tenses and Modals."
