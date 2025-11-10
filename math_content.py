# math_content.py
# 12. Sınıfa Kadar Kapsam Genişletildi

KONULAR_MATH = {
    "denklemler": "Denklemler, iki matematiksel ifadenin eşitliğini gösteren ifadelerdir. Bilinmeyeni (x) bulmak için kullanılır. (Örnek: 2x + 3 = 7).",
    "üslü sayılar": "Bir sayının kendisiyle kaç kez çarpılacağını gösteren sayılardır. (Örnek: 2³ = 8).",
    "türev": "Türev, bir fonksiyonun anlık değişim hızını bulmaya yarar. Maksimum ve minimum değerleri bulmak için kullanılır. (Lise 12. Sınıf Konusu).",
    "integral": "İntegral, bir eğrinin altında kalan alanı hesaplamaya yarar. Türevin tersi olarak da bilinir. (Lise 12. Sınıf Konusu).",
    "logaritma": "Logaritma, üslü ifadenin ters işlemidir. Büyük sayıları daha küçük sayılarla temsil etmekte kullanılır. (Örnek: log₂(8) = 3).",
}

def konuyu_bul_math(arama_terimi):
    arama_terimi = arama_terimi.lower().strip()
    if arama_terimi in KONULAR_MATH:
        return f"📐 MATEMATİK KONU ANLATIMI:\n\n{KONULAR_MATH[arama_terimi]}"
    else:
        return "Üzgünüm, aradığınız matematik konusunu bulamadım."

def soru_cozumu_yap_math(arama_termi):
    arama_termi = arama_termi.lower().strip()
    return "❓ Örnek Soru Çözümü (Matematik): Çözüm, cebirsel işlemler, formüller ve ispatlar kullanılarak yapılır."
