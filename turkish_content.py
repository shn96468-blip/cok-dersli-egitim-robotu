# turkish_content.py
KONULAR_TR = {
    # BURAYA EN AZ 1 KONU BAŞLIĞI OLMALI
    "isimler": "İsimler, canlı ve cansız varlıkları, duygu ve düşünceleri karşılayan kelimelerdir. Varlıklara verilişlerine göre özel ve cins isimler olarak ikiye ayrılır.",
    "ek fiil": "Ek fiilin iki temel görevi vardır: İsimleri yüklem yapmak veya basit zamanlı fiilleri birleşik zamanlı yapmak.",
}

def konuyu_bul_tr(arama_terimi):
    if arama_terimi in KONULAR_TR:
        return f"🇹🇷 TÜRKÇE KONU ANLATIMI:\n{KONULAR_TR[arama_terimi]}"
    else:
        return "Üzgünüm, aradığınız konuyu 7. Sınıf Türkçe sözlüğünde bulamadım."

def soru_cozumu_yap_tr(arama_termi):
    return "❓ Örnek Soru Çözümü (Türkçe): Soru çözümü, cümle analiz kurallarını kullanır."
