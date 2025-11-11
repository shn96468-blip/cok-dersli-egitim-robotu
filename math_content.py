# Matematik İçerik Modülü

def konuyu_bul_math(konu):
    konu_lower = konu.lower()
    if "üslü" in konu_lower or "sayı" in konu_lower:
        return "Üslü Sayılar: Bir sayının kendisiyle kaç kez çarpıldığını gösteren ifadedir. Örnek: 2 üzeri 3 (2³) = 2 * 2 * 2 = 8'dir."
    elif "dört işlem" in konu_lower or "toplama" in konu_lower:
        return "Temel Dört İşlem: Matematikte toplama (+), çıkarma (-), çarpma (x) ve bölme (÷) işlemleridir. Her birinin matematiksel işlem önceliği kuralları vardır."
    else:
        return f"Matematik dersi için '{konu.upper()}' konusuyla ilgili detaylı içerik bulunamamıştır."

def soru_cozumu_yap_math(soru):
    soru_lower = soru.lower()
    if "denklem" in soru_lower or "bilinmeyen" in soru_lower:
        return "Çözüm: Bu bir denklem problemidir. Bilinmeyeni (genellikle x) yalnız bırakarak veya her iki tarafa aynı işlemi uygulayarak çözüme ulaşabilirsiniz."
    else:
        return f"Matematik dersi için '{soru.upper()}' sorusuna özgü bir çözüm yolu bulamadım."
