# english_content.py

# --- İngilizce Konu Anlatımı Fonksiyonu ---
def konuyu_bul_eng(konu):
    konular = {
        "present simple": """
        **Present Simple Tense (Geniş Zaman) Konu Anlatımı**
        
        **Kullanımı:**
        1. Alışkanlıkları ve rutinleri ifade eder.
           * Örnek: I **drink** coffee every morning. (Her sabah kahve içerim.)
        2. Genel gerçekleri ve bilimsel olguları ifade eder.
           * Örnek: The Sun **rises** in the east. (Güneş doğudan doğar.)
        
        **Yapı:**
        * **Olumlu:** I/You/We/They + Fiilin Yalın Hali (V1)
          He/She/It + Fiilin Yalın Hali + **-s** takısı
        * **Olumsuz:** I/You/We/They + **don't** + V1
          He/She/It + **doesn't** + V1
        * **Soru:** **Do** + I/You/We/They + V1?
          **Does** + He/She/It + V1?
        """,
        "past simple": """
        **Past Simple Tense (Geçmiş Zaman) Konu Anlatımı**
        
        **Kullanımı:** Geçmişte belirli bir zamanda başlayıp bitmiş eylemleri anlatmak için kullanılır.
        
        **Yapı:**
        * **Olumlu:** Tüm özneler + Fiilin İkinci Hali (V2 - Düzenli fiiller için -ed, Düzensiz fiiller ezberlenmelidir).
            * Örnek (Düzenli): I **studied** yesterday.
            * Örnek (Düzensiz): She **went** to the cinema last night.
        * **Olumsuz:** Tüm özneler + **didn't** + Fiilin Yalın Hali (V1)
            * Örnek: They **didn't eat** the cake.
        * **Soru:** **Did** + Tüm özneler + Fiilin Yalın Hali (V1)?
            * Örnek: **Did** you **call** me?
        """,
        "verb": """
        **Verb (Fiil) Konu Anlatımı**
        
        Fiiller, bir eylemi, durumu veya oluşu anlatan kelimelerdir. İngilizcede fiillerin zamanlara göre çekimleri önemlidir (V1, V2, V3).
        
        **Fiil Çeşitleri:**
        * **Action Verbs (Eylem Fiilleri):** Koşmak, yemek, konuşmak.
        * **Stative Verbs (Durum Fiilleri):** Bilmek, sevmek, inanmak (Genellikle -ing almazlar).
        * **Auxiliary Verbs (Yardımcı Fiiller):** Be, do, have (Zaman oluşturmak için kullanılırlar).
        """,
        "apple": "Apple kelimesinin Türkçe karşılığı **Elma**'dır.",
        "hello": "Hello kelimesinin Türkçe karşılığı **Merhaba**'dır.",
        "dog": "Dog kelimesinin Türkçe karşılığı **Köpek**'tir.",
        "cat": "Cat kelimesinin Türkçe karşılığı **Kedi**'dir."
    }
    
    return konular.get(konu.lower().strip(), f"Üzgünüm, İngilizce dersinde '{konu}' başlığı altında detaylı bir konu anlatımı veya kelime bulamadım. Başka bir konu deneyin (örn: Present Simple, Past Simple) veya kelime girin (örn: Apple).")


# --- İngilizce Soru Çözümü Fonksiyonu ---
def soru_cozumu_yap_eng(soru):
    soru_lower = soru.lower().strip()
    
    if "fill in the blank" in soru_lower or "boşluk" in soru_lower or "doldur" in soru_lower:
        cevap = """
        **Örnek Soru Çözümü: Boşluk Doldurma (Present Perfect)**
        
        **Soru:** I ______ (see) him for ages.
        
        **Çözüm:** Cümlede 'for ages' (yıllardır/uzun süredir) ifadesi Present Perfect Tense gerektirir. Olumsuz bir anlam da kastedildiği varsayılırsa:
        * **Cevap:** I **haven't seen** him for ages. (Onu uzun süredir görmedim.)
        
        **Robot Cevabı:** Bu tarz bir sorunun çözümü genellikle fiil çekimi veya tense bilgisi gerektirir. Sorduğunuz tam cümleyi veya soruyu girerseniz daha spesifik bir çözüm sunabilirim.
        """
    elif "which sentence" in soru_lower or "hangi cümle" in soru_lower:
        cevap = """
        **Örnek Soru Çözümü: Anlam Bütünlüğü**
        
        **Soru:** Which sentence is grammatically correct?
        
        **Çözüm:** Gramer hataları genellikle özne-fiil uyumu, tense kullanımı veya kelime sırası ile ilgilidir. Doğru cevabı bulmak için şıkları analiz etmek gerekir.
        
        **Robot Cevabı:** Lütfen kontrol etmem gereken cümleleri tek tek girin. Hangi cümlenin doğru olduğunu belirlemek için gramer kurallarını uygulayarak size yardımcı olabilirim.
        """
    else:
        cevap = f"Üzgünüm, İngilizce için '{soru}' sorusu için hazır bir çözüm şablonu bulamadım. Lütfen bir boşluk doldurma veya gramer sorusu girin."
        
    return cevap


# --- İngilizce Kelime için Türkçe karşılığı (Bu fonksiyon app.py'de 'Kelime Bilgisi' modu için TR aradığında çağrılır) ---
def konuyu_bul_tr(konu):
    # Bu fonksiyon normalde türkçe_content.py'de tanımlı olsa da, 
    # ingilizce_content.py içinde de tanımlanarak Kelime Bilgisi modunda çakışma engellenir.
    kelimeler = {
        "apple": "**Apple** kelimesinin Türkçe karşılığı **Elma**'dır.",
        "hello": "**Hello** kelimesinin Türkçe karşılığı **Merhaba**'dır.",
        "dog": "**Dog** kelimesinin Türkçe karşılığı **Köpek**'tir.",
        "cat": "**Cat** kelimesinin Türkçe karşılığı **Kedi**'dir.",
        "teach": "**Teach** kelimesinin Türkçe karşılığı **Öğretmek**'tir."
    }
    return kelimeler.get(konu.lower().strip(), f"Üzgünüm, İngilizce '{konu}' kelimesinin Türkçe karşılığını bulamadım.")
