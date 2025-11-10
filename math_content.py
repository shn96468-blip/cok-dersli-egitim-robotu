# Bu dosya, sadece Matematik konularını ve fonksiyonlarını içerir.
# 📐 MATEMATİK KONULARI SÖZLÜĞÜ (12. Sınıf Dahil)
KONULAR_MATH = {
    # Temel Konular (5. - 8. Sınıflar)
    "doğal sayılar": "⭐ **Doğal Sayılar:** 0'dan başlayıp sonsuza giden pozitif tam sayılardır. (0, 1, 2, 3, ...).",
    "tam sayılar": "Doğal sayılar, negatifleri ve sıfırdan oluşur. (-3, -2, -1, 0, 1, 2, 3, ...).",
    "rasyonel sayılar": "a/b şeklinde yazılabilen sayılardır. Kesirler, ondalık sayılar rasyoneldir.",
    "üslü ifadeler": "Bir sayının kendisiyle kaç kez çarpılacağını gösterir. (3² = 9).",
    "köklü ifadeler": "Hangi sayının kendisiyle çarpıldığında verilen sayıyı verdiğini bulma işlemidir. (√9 = 3).",
    "oran ve orantı": "Oran: İki miktarın birbirine bölünmesi. Orantı: İki oranın birbirine eşit olmasıdır.",
    "denklemler": "İki cebirsel ifadenin eşitliğini gösteren ifadelerdir. Bilinmeyeni (x) bulmayı amaçlar.",
    "geometri temel kavramlar": "Nokta, doğru, ışın, düzlem gibi geometrinin başlangıç terimleri.",
    "alan ve çevre": "Alan: Bir şeklin kapladığı yüzey miktarı. Çevre: Bir şeklin dış sınırının uzunluğu.",

    # Lise Konuları (9. - 12. Sınıflar)
    "kümeler": "Belirli ve farklı nesneler topluluğudur. Birleşim, kesişim, fark gibi işlemleri vardır.",
    "fonksiyonlar": "Bir kümenin her elemanını, ikinci bir kümenin tek bir elemanına eşleyen kuraldır. f(x) olarak gösterilir.",
    "polinomlar": "Çok terimli demektir. x'in doğal sayı kuvvetlerinden oluşan ifadelerdir. P(x) ile gösterilir.",
    "trigonometri": "Üçgenlerin açıları ve kenarları arasındaki ilişkileri inceler. Sinüs (sin), Kosinüs (cos) temel fonksiyonlarıdır.",
    "logaritma": "Üslü ifadelerin tersi işlemidir. Bir sayının, başka bir sayının hangi kuvveti olduğunu bulur. log(x) ile gösterilir.",
    "diziler": "Terimleri belirli bir kurala göre sıralanan sayılar kümesidir. Aritmetik ve Geometrik diziler en çok bilinir.",
    "limit": "Bir fonksiyonda değişkenin yaklaştığı değeri inceler.",
    "türev": "Bir fonksiyonun belli bir noktadaki anlık değişim hızını bulur. Eğim ve teğet hesaplamalarında kullanılır.",
    "integral": "Türevin tersi işlemidir. Eğriler altındaki alanı veya birikimli değişimi hesaplamakta kullanılır.",
    "matris ve determinant": "Sayıların dikdörtgen düzenlemeleridir. Doğrusal denklem sistemlerini çözmekte kullanılır.",
}

def konuyu_bul_math(arama_terimi):
    if arama_terimi in KONULAR_MATH:
        return f"📐 MATEMATİK KONU ANLATIMI (12. Sınıf Kapsamlı):\n{KONULAR_MATH[arama_terimi]}"
    else:
        return "Üzgünüm, aradığınız konuyu Matematik sözlüğünde (Temel-İleri Seviye) bulamadım."

def soru_cozumu_yap_math(arama_termi):
    if "türev" in arama_termi or "integral" in arama_termi or "limit" in arama_termi:
        return "❓ **Örnek Soru Çözümü (İleri Matematik):** İleri Matematik sorularında limit, türev veya integral kuralları uygulanır. Hangi kuralın (zincir kuralı, kısmi integrasyon vb.) uygulanacağı belirlenir. **Cevap:** Gerekli limit/türev/integral kuralı kullanılarak çözüldü."
    elif "denklem" in arama_termi or "sayı" in arama_termi or "ifade" in arama_termi or "fonksiyon" in arama_termi:
        return "❓ **Örnek Soru Çözümü (Temel Matematik):** Sorunun türüne göre uygun cebirsel/geometrik formül uygulanır. **Cevap:** Problemin çözümünde Rasyonel Sayılar veya Denklem çözme kuralları kullanıldı."
    else:
        return "Şu an sadece **Temel Sayılar, Cebir, Fonksiyonlar** ve **İleri Analiz (Limit, Türev, İntegral)** konularıyla ilgili örnek soruları çözebilirim."