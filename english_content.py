# Bu dosya, sadece İngilizce konularını, Kelime Bilgisi içeriğini ve özel fonksiyonları içerir.

# 🇬🇧 İNGİLİZCE KONULAR SÖZLÜĞÜ (Tenses, Modals, Vocabulary, Ünite İfadeleri)
KONULAR_ENG = {
    # Temel Gramer (2. - 5. Sınıflar)
    "to be": "⭐ **To Be (am, is, are):** İngilizcede 'olmak' fiilidir ve isim cümlelerinin olmazsa olmazıdır. Örn: 'I **am** happy.'",
    "simple present tense": "Geniş Zaman (Yaparım). Düzenli yapılan eylemleri ve genel gerçekleri anlatır. Örn: 'She **goes** to school every day.'",
    "present continuous tense": "Şimdiki Zaman (Yapıyorum). Şu anda olan, devam eden eylemleri anlatır. Örn: 'I **am reading** a book now.'",
    "simple past tense": "Geçmiş Zaman (Yaptım). Geçmişte başlayıp bitmiş olayları anlatır. Fiillerin 2. halleri (V2) kullanılır. Örn: 'He **visited** Paris last year.'",
    "adjectives and adverbs": "Sıfatlar (isimleri niteler) ve Zarflar (fiilleri niteler). Sıfatlara -ly eklenerek zarf yapılabilir (quick → quickly).",
    
    # Ortaokul ve Lise Konuları (6. - 12. Sınıflar)
    "modals": "Can, Must, Should gibi yeterlilik, zorunluluk, tavsiye bildiren yardımcı fiillerdir. Örn: 'You **should** study hard.'",
    "future tense": "Gelecek Zaman (Yapacağım). Will veya Going To ile yapılır. Will daha genel, Going To daha kesin planları belirtir.",
    "present perfect tense": "Yakın Geçmiş Zaman (Yaptım/Bulundum). Geçmişte başlayıp etkisi devam eden veya zamanı belli olmayan eylemler için kullanılır. (Have/Has + V3).",
    "conditional sentences": "Koşul Cümleleri (If Clauses). Type 0, 1, 2, 3 gibi türleri vardır. Şart ve sonuç bildirirler. Örn: 'If I study, I will pass.'",
    "comparatives and superlatives": "Sıfatların karşılaştırma (bigger, more expensive) ve en üstünlük (the biggest, the most expensive) dereceleri.",
    "regular and irregular verbs": "Düzenli (ed alan) ve Düzensiz (şekil değiştiren) fiillerin geçmiş zaman ve Perfect Tense'lerde kullanımı.",
    
    # Yeni Eklenen Kelime Bilgisi/Vocabulary Özellikleri
    "vocabulary": "Kelime bilgisi, okuduğunu anlama, dinlediğini anlama ve etkin iletişim kurma için gereken temel kelimeler ve ifadelerdir.",
    "prepositions": "Yer ve zaman bildiren edatlardır (in, on, at, under, behind, next to vb.).",
    "phrasal verbs": "Fiil + Edat/Zarf ile birleşerek yeni anlam kazanan fiillerdir (turn off, look up, take off vb.).",
    
    # Ünite Örnekleri (8. Sınıf)
    "friendship": "Arkadaşlık, davet etme ve kabul/reddetme ifadeleri ile ilgili kelime ve kalıplar.",
    "teen life": "Gençlik hayatı, hobiler ve günlük aktivitelerle ilgili ifadeler.",
    "tourism": "Turizm, seyahat, yerler ve tatil aktiviteleriyle ilgili ifadeler.",
}

def konuyu_bul_eng(arama_terimi):
    if arama_terimi in KONULAR_ENG:
        return f"🇬🇧 İNGİLİZCE KONU ANLATIMI:\n{KONULAR_ENG[arama_terimi]}"
    else:
        return "Üzgünüm, aradığınız konuyu İngilizce sözlükte bulamadım."

def soru_cozumu_yap_eng(arama_termi):
    if "tense" in arama_termi or "modal" in arama_termi or "if" in arama_termi or "to be" in arama_termi:
        return "❓ **Örnek Soru Çözümü (İngilizce Gramer):** İngilizcede Tense soruları için öncelikle zaman zarfına (now, yesterday, every day) bakmalıyız. Bu zarf, doğru zaman (Tense) yapısını belirler. **Cevap:** Doğru zaman yapısı (Tense) kullanıldı."
    
    elif "kelime" in arama_termi or "vocabulary" in arama_termi or "phrasal" in arama_termi or "preposition" in arama_termi or "friendship" in arama_termi or "teen life" in arama_termi or "tourism" in arama_termi:
        return "❓ **Örnek Soru Çözümü (İngilizce Kelime/Ünite):** Kelime sorularında, cümlenin anlam bütünlüğünü kontrol etmeli ve boşluğa gelmesi gereken kelimenin türünü (isim, fiil, sıfat) belirlemeliyiz. **Cevap:** Doğru kelime seçimi ile anlam bütünlüğü sağlandı."
    
    else:
        return "Şu an sadece **İngilizce Tense/Modal** veya **Kelime Bilgisi** konularıyla ilgili örnek soruları çözebilirim."
