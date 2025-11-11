# İngilizce İçerik Modülü

def konuyu_bul_eng(konu):
    konu_lower = konu.lower()
    if "present" in konu_lower or "simple" in konu_lower:
        return "Present Simple Tense (Geniş Zaman): Günlük alışkanlıkları, genel gerçekleri ve sabit durumları ifade etmek için kullanılır. Fiilin yalın hali (He/She/It için -s takısı alır) kullanılır."
    elif "verb" in konu_lower or "fiil" in konu_lower:
        return "Verbs (Fiiller): Cümlede eylem, durum veya oluş bildiren kelimelerdir. İngilizcede düzenli (regular) ve düzensiz (irregular) fiiller bulunur."
    else:
        return f"İngilizce dersi için '{konu.upper()}' konusuyla ilgili detaylı içerik bulunamamıştır."

def soru_cozumu_yap_eng(soru):
    soru_lower = soru.lower()
    if "past" in soru_lower and "tense" in soru_lower:
        return "Çözüm: Past Tense sorusudur. Eylem geçmişte tamamlanmıştır. Düzenli fiiller -ed, düzensiz fiiller ise ikinci hallerini (V2) kullanır."
    else:
        return f"İngilizce dersi için '{soru.upper()}' sorusuna özgü bir çözüm yolu bulamadım."
