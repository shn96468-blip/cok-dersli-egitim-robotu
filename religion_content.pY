def konuyu_bul_religion(konu):
    konu = konu.lower()
    if "islam" in konu or "iman" in konu:
        return """
        **İslam'da İman Esasları:**
        İman, altı temel esastan oluşur: Allah'a, meleklere, kitaplara, peygamberlere, ahiret gününe ve kaza-kadere iman.
        Bu esaslar, dinin temel inanç sistemini oluşturur ve tevhidi (Allah'ın birliğini) esas alır. (Simülasyon İçeriği)
        """
    elif "namaz" in konu or "ibadet" in konu:
        return """
        **Temel İbadetler (Namaz):**
        Namaz, İslam'ın beş şartından biridir ve günde beş vakit farzdır. Allah ile kul arasında doğrudan bir bağlantı kurar.
        Namaz öncesinde abdest almak gerekir. (Simülasyon İçeriği)
        """
    else:
        return f"Üzgünüm, Din Kültürü dersi için '{konu}' konusu hakkında bilgi bulamadım."

def soru_cozumu_yap_religion(soru):
    soru = soru.lower()
    if "kaza" in soru or "kader" in soru:
        return """
        **Cevap:** Kader, Allah'ın her şeyi önceden takdir etmesi; kaza ise takdir edilen şeylerin zamanı gelince gerçekleşmesidir.
        (Sorunuzun çözümü simülasyon olarak verilmiştir.)
        """
    elif "oruç" in soru or "ramazan" in soru:
        return """
        **Cevap:** Oruç, Ramazan ayında tutulur ve imsak vaktinden iftar vaktine kadar yemek, içmek ve kötü davranışlardan uzak durmaktır.
        (Sorunuzun çözümü simülasyon olarak verilmiştir.)
        """
    else:
        return f"Üzgünüm, Din Kültürü dersi için bu sorunun ('{soru}') çözümünü bulamadım."
