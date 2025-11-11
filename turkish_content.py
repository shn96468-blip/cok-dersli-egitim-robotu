# Türkçe İçerik Modülü

def konuyu_bul_tr(konu):
    konu_lower = konu.lower()
    if "edat" in konu_lower or "bağlaç" in konu_lower:
        return "Türkçe Dil Bilgisi: Edatlar ve Bağlaçlar, cümledeki kelimeler arasında anlam ilişkisi kurar. Edatlar tek başına anlamı olmayan, bağlaçlar ise kelimeleri/cümleleri birbirine bağlayan sözcüklerdir."
    elif "yazım" in konu_lower or "noktalama" in konu_lower:
        return "Yazım Kuralları ve Noktalama İşaretleri: Türkçenin doğru kullanımını sağlayan temel kurallardır. Örneğin, özel isimler her zaman büyük harfle başlar ve cümle sonuna nokta (.) konur."
    else:
        return f"Türkçe dersi için '{konu.upper()}' konusuyla ilgili detaylı içerik bulunamamıştır."

def soru_cozumu_yap_tr(soru):
    soru_lower = soru.lower()
    if "isim" in soru_lower and "sıfat" in soru_lower:
        return "Çözüm: İsimler varlıkları, sıfatlar ise varlıkların özelliklerini (nasıl olduğunu) belirtir. Soru köküne bakılarak cevabı bulabilirsiniz."
    else:
        return f"Türkçe dersi için '{soru.upper()}' sorusuna özgü bir çözüm yolu bulamadım."
