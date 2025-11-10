def konuyu_bul_history(konu):
    konu = konu.lower()
    if "osmanlı" in konu or "kuruluş" in konu:
        return """
        **Osmanlı Devleti'nin Kuruluşu:**
        Osmanlı Beyliği, 13. yüzyıl sonlarında Söğüt ve çevresinde kuruldu. Kurucusu Osman Bey'dir.
        Bizans'a yakınlığı sayesinde cihat ve gaza ruhuyla hızla büyüdü.
        Anadolu beylikleri arasında güçlü merkezi otoritesi ve adil yönetimi ile öne çıktı. (Simülasyon İçeriği)
        """
    elif "inkılap" in konu or "cumhuriyet" in konu:
        return """
        **Türk İnkılap Tarihi:**
        Mustafa Kemal Atatürk'ün liderliğinde, 1919'da başlayan Milli Mücadele'nin ardından
        Türkiye Cumhuriyeti 29 Ekim 1923'te kuruldu. İnkılaplar, toplumsal, siyasal ve hukuki alanda
        modernleşmeyi amaçladı. (Simülasyon İçeriği)
        """
    else:
        return f"Üzgünüm, Tarih dersi için '{konu}' konusu hakkında bilgi bulamadım."

def soru_cozumu_yap_history(soru):
    soru = soru.lower()
    if "osman bey" in soru:
        return """
        **Cevap:** Osmanlı Beyliği'nin ilk kurucusu ve adını veren kişi **Osman Bey**'dir.
        (Sorunuzun çözümü simülasyon olarak verilmiştir.)
        """
    elif "atatürk" in soru or "mücadele" in soru:
        return """
        **Cevap:** Milli Mücadele'nin başlangıç tarihi genellikle **19 Mayıs 1919 (Samsun'a Çıkış)** olarak kabul edilir.
        (Sorunuzun çözümü simülasyon olarak verilmiştir.)
        """
    else:
        return f"Üzgünüm, Tarih dersi için bu sorunun ('{soru}') çözümünü bulamadım."
