# math_content.py
KONULAR_MATH = {
    # BURAYA EN AZ 1 KONU BAŞLIĞI OLMALI
    "denklemler": "Denklemler, iki matematiksel ifadenin eşitliğini gösteren ifadelerdir. Bilinmeyeni bulmak için kullanılır. (Örnek: 2x + 3 = 7).",
    "üslü sayılar": "Bir sayının kendisiyle kaç kez çarpılacağını gösteren sayılardır. (Örnek: 2^3 = 8).",
}

def konuyu_bul_math(arama_terimi):
    if arama_terimi in KONULAR_MATH:
        return f"📐 MATEMATİK KONU ANLATIMI:\n{KONULAR_MATH[arama_terimi]}"
    else:
        return "Üzgünüm, aradığınız matematik konusunu bulamadım."

def soru_cozumu_yap_math(arama_termi):
    return "❓ Örnek Soru Çözümü (Matematik): Çözüm, cebirsel işlemler ve formüller kullanılarak yapılır."
