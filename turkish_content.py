# turkish_content.py

# --- Türkçe Konu Anlatımı Fonksiyonu ---
def konuyu_bul_tr(konu):
    konular = {
        "zarf": """
        **Zarf (Belirteç) Konu Anlatımı**
        
        Zarflar, fiilleri, fiilimsileri, sıfatları ve bazen de başka zarfları anlamca tamamlayan kelimelerdir. 
        Cümleye zaman, durum, miktar, yer-yön ve soru anlamları katarlar.
        
        **Zarf Çeşitleri:**
        * **Durum Zarfı (Niteleme):** Fiile sorulan "Nasıl?" sorusuna cevap verir.
            * Örnek: Hızlı **koştu**. (Nasıl koştu? Hızlı)
        * **Zaman Zarfı:** Fiile sorulan "Ne zaman?" sorusuna cevap verir.
            * Örnek: Yarın **gelecek**. (Ne zaman gelecek? Yarın)
        * **Miktar Zarfı (Azlık-Çokluk):** Fiile, sıfata veya zarfa sorulan "Ne kadar?" sorusuna cevap verir.
            * Örnek: Çok **güzel** konuştu. (Ne kadar güzel? Çok)
        * **Yer-Yön Zarfı:** Fiile sorulan "Nereye?" sorusuna cevap verir (ek almazlar).
            * Örnek: Aşağı **indiler**. (Nereye indiler? Aşağı)
        * **Soru Zarfı:** Fiili soru yoluyla belirtir.
            * Örnek: Niçin **bekliyorsunuz**?
        
        """,
        "isim": """
        **İsim (Ad) Konu Anlatımı**
        
        İsimler, canlı ve cansız varlıkları, kavramları, durumları ve duyguları karşılayan kelimelerdir.
        
        **İsim Çeşitleri:**
        * **Varlıklara Verilişine Göre:**
            * **Özel İsim:** Tek olan, eşi benzeri bulunmayan varlıkları karşılar (Türkiye, Ali, Van Gölü).
            * **Cins (Tür) İsim:** Aynı türden birçok varlığı karşılar (kitap, masa, çiçek).
        * **Sayılarına Göre:**
            * **Tekil İsim:** Çoğul eki (-ler, -lar) almamış isimlerdir (ev, ağaç).
            * **Çoğul İsim:** Çoğul eki (-ler, -lar) almış isimlerdir (evler, ağaçlar).
            * **Topluluk İsim:** Yapıca tekil, anlamca çoğul olan isimlerdir (ordu, sınıf, aile).
        
        """,
        "ekler": """
        **Çekim ve Yapım Ekleri Konu Anlatımı**
        
        * **Yapım Ekleri:** Kelimenin anlamını veya türünü değiştirerek yeni bir kelime oluşturan eklerdir. 
            * Örnek: göz (isim) + **-lük** (yapım eki) = gözlük (yeni isim)
            
        * **Çekim Ekleri:** Kelimenin anlamını ve türünü değiştirmeyen, sadece cümledeki görevini belirleyen eklerdir.
            * **İsim Çekim Ekleri:** Hal, iyelik, çoğul, tamlama ekleri.
            * **Fiil Çekim Ekleri:** Zaman, şahıs, kip ekleri.
            * Örnek: kalem + **-ler** (çoğul eki)
        
        """
    }
    
    return konular.get(konu.lower().strip(), f"Üzgünüm, Türkçe dersinde '{konu}' başlığı altında detaylı bir konu anlatımı bulamadım. Başka bir konu deneyin (örn: Zarf, İsim, Ekler).")


# --- Türkçe Soru Çözümü Fonksiyonu ---
def soru_cozumu_yap_tr(soru):
    soru_lower = soru.lower().strip()
    
    if "edat" in soru_lower or "edat grubu" in soru_lower:
        cevap = """
        **Örnek Soru Çözümü: Edatlar**
        
        **Soru:** Aşağıdaki cümlelerin hangisinde edat grubu kullanılmıştır?
        
        **Çözüm:** Edatlar (ilgeçler) tek başlarına anlamı olmayan, ancak cümlede kendilerinden önceki kelime ile anlam ilişkisi kuran kelimelerdir (gibi, için, ile, göre, kadar...). Edat grupları, edatların kendinden önceki kelimeyle oluşturduğu gruplardır.
        
        Örneğin: "Yağmur **yağdığı için** dışarı çıkamadık." cümlesinde "**yağdığı için**" bir edat grubudur.
        
        **Robot Cevabı:** Sizin sorduğunuz soruya benzer bir örnek çözüm sundum. Lütfen spesifik cümlenizi giriniz.
        """
    elif "yazım" in soru_lower or "noktalama" in soru_lower:
        cevap = """
        **Örnek Soru Çözümü: Yazım Kuralları**
        
        **Soru:** "2024 yılının Mayıs ayı da bitti." cümlesindeki yazım hatasını bulunuz.
        
        **Çözüm:** Belirli bir tarih bildiren ay ve gün adları büyük harfle başlar. Bu cümlede yıl adı verildiği için "Mayıs" kelimesinin M harfi büyük olmalıdır.
        
        **Robot Cevabı:** Sizin sorunuzun cevabı, genellikle büyük harflerin, bağlaçların veya sayıların yazımı ile ilgilidir. Soru cümlesini daha detaylı yazarsanız kesin çözümü sunabilirim.
        """
    else:
        cevap = f"Üzgünüm, '{soru}' sorusu için hazır bir çözüm şablonu bulamadım. Lütfen Türkçe dil bilgisi veya anlam bilgisi ile ilgili net bir soru girin."
        
    return cevap
