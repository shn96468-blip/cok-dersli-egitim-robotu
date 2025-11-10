# turkish_content.py
# 7. Sınıf ve Genel Türkçe Konuları

KONULAR_TR = {
    "isimler": "İsimler (Adlar), canlı ve cansız varlıkları, duygu ve düşünceleri karşılayan kelimelerdir. Varlıklara verilişlerine göre özel ve cins isimler olarak ikiye ayrılır.",
    "ek fiil": "Ek fiilin iki temel görevi vardır: İsimleri yüklem yapmak ('idi', 'imiş', 'ise', 'dir') veya basit zamanlı fiilleri birleşik zamanlı yapmak.",
    "cümle türleri": "Cümleler, yapılarına, yüklemin yerine ve anlamına göre ayrılırlar. Örnek: Basit cümle, birleşik cümle, olumlu/olumsuz cümle.",
    "sıfatlar": "Sıfatlar (Ön Adlar), isimlerin önüne gelerek onları niteleyen veya belirten kelimelerdir. Örnek: Kırmızı araba, iki kişi.",
    "paragraf": "Paragraf, tek bir düşünceyi tam olarak anlatan cümleler bütünüdür. Giriş, gelişme ve sonuç bölümlerinden oluşur.",
}

def konuyu_bul_tr(arama_terimi):
    arama_terimi = arama_terimi.lower().strip()
    if arama_terimi in KONULAR_TR:
        return f"🇹🇷 TÜRKÇE KONU ANLATIMI:\n\n{KONULAR_TR[arama_terimi]}"
    else:
        # Eğer tam eşleşme yoksa, Yedek Mekanizma devreye girer.
        return "Üzgünüm, aradığınız konuyu 7. Sınıf Türkçe sözlüğünde bulamadım."

def soru_cozumu_yap_tr(arama_termi):
    arama_termi = arama_termi.lower().strip()
    return "❓ Örnek Soru Çözümü (Türkçe): Soru çözümü, cümle analiz kurallarını kullanır ve detaylı bir yapısal inceleme gerektirir."
