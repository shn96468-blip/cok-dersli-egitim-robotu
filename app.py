import streamlit as st
from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
from english_content import konuyu_bul_eng, soru_cozumu_yap_eng
from math_content import konuyu_bul_math, soru_cozumu_yap_math
from religion_content import konuyu_bul_rel, soru_cozumu_yap_rel
from prophet_content import konuyu_bul_prophet, soru_cozumu_yap_prophet


# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Çok Dersli Eğitim Robotu",
    layout="wide"
)

# --- ANA ROBOT EKRANI ---
st.title("📚 Çok Dersli Eğitim Robotu: Konu Anlatım ve Soru Çözüm Asistanı")
st.markdown("Merhaba! Hangi konuda bilgi istersin (Türkçe, İngilizce, Matematik, Din Kültürü veya Peygamber Hayatı) ya da hangi konuyla ilgili **örnek soru çözümü** yapmamı istersin? 😉")

# Mod Seçimi
islem_modu = st.radio(
    "Lütfen yapmak istediğiniz işlemi seçin:",
    ("Konu Anlatımı", "Soru Çözümü"),
    horizontal=True
)

konu_adi = st.text_input(f"İstediğiniz Konu Adını Giriniz (Örn: **ek fiil**, **simple present tense** veya **doğal sayılar**):")

# Sesli Konuşma Kontrolü
konusma_acik = st.checkbox("Robotun Konuyu Sesli Anlatmasını İster misiniz?")

# Tüm dillerden anahtar kelimeler
ingilizce_anahtarlar = ['tense', 'modal', 'present', 'future', 'to be', 'vocabulary', 'friendship', 'teen life', 'tourism']
matematik_anahtarlar = ['sayı', 'denklem', 'oran', 'alan', 'çevre', 'limit', 'türev', 'integral'] # Güncelledik
din_anahtarlar = ['iman', 'ibadet', 'kader', 'zekat', 'ahiret']
peygamber_anahtarlar = ['hicret', 'vahiy', 'sahabe', 'mekke', 'medine']

# Yanıt düğmesi
if st.button("Başlat"):
    if konu_adi:
        
        konu_adi_lower = konu_adi.lower().strip()
        konu_icerigi = "Üzgünüm, aradığınız konuyu hiçbir sözlükte bulamadım." # Varsayılan değer
        soru_cevabi = "Soru çözümü için uygun içerik bulunamadı."

        # Hangi dilde/derste arama yapılacağını belirleme ve içeriği çekme
        if any(keyword in konu_adi_lower for keyword in ingilizce_anahtarlar):
            konu_icerigi = konuyu_bul_eng(konu_adi_lower)
        elif any(keyword in konu_adi_lower for keyword in matematik_anahtarlar):
            konu_icerigi = konuyu_bul_math(konu_adi_lower)
        elif any(keyword in konu_adi_lower for keyword in din_anahtarlar):
            konu_icerigi = konuyu_bul_rel(konu_adi_lower)
        elif any(keyword in konu_adi_lower for keyword in peygamber_anahtarlar):
            konu_icerigi = konuyu_bul_prophet(konu_adi_lower)
        else: # Hiçbir anahtar kelime bulunamazsa Türkçe'ye bak (Türkçe temel dilimiz)
            konu_icerigi = konuyu_bul_tr(konu_adi_lower)

        # --- Konu Anlatımı Modu ---
        if islem_modu == "Konu Anlatımı":
            
            if "Üzgünüm" not in konu_icerigi:
                st.success(f"İşte '{konu_adi.upper()}' konusu ile ilgili bilmen gerekenler:")
                st.markdown(konu_icerigi)

                if konusma_acik:
                    # Sesli konuşma kodu
                    pass

            else:
                st.warning(konu_icerigi)
        
        # --- Soru Çözümü Modu ---
        elif islem_modu == "Soru Çözümü":
            
            if any(keyword in konu_adi_lower for keyword in ingilizce_anahtarlar):
                soru_cevabi = soru_cozumu_yap_eng(konu_adi_lower)
            elif any(keyword in konu_adi_lower for keyword in matematik_anahtarlar):
                soru_cevabi = soru_cozumu_yap_math(konu_adi_lower)
            elif any(keyword in konu_adi_lower for keyword in din_anahtarlar):
                soru_cevabi = soru_cozumu_yap_rel(konu_adi_lower)
            elif any(keyword in konu_adi_lower for keyword in peygamber_anahtarlar):
                soru_cevabi = soru_cozumu_yap_prophet(konu_adi_lower)
            else:
                soru_cevabi = soru_cozumu_yap_tr(konu_adi_lower)

            st.info(f"'{konu_adi.upper()}' konusu için bir örnek soru çözümü:")
            st.markdown(soru_cevabi)

            if konusma_acik:
                # Sesli konuşma kodu
                pass

    else:
        st.error("Lütfen bir konu adı giriniz.")

# --- KENAR ÇUBUĞU VE ALT BÖLÜM (GÜNCELLENDİ) ---
st.sidebar.title("Kullanılabilir Konular (5 Ders)")
st.sidebar.markdown(
    """
    **🇹🇷 Türkçe:** Dil Bilgisi, Anlam (Sözcük, Cümle, Paragraf).
    **🇬🇧 İngilizce:** Tenses, Modals, **Kelime Bilgisi (Vocabulary) Dahil**.
    **📐 Matematik:** Sayılar, Denklemler, İleri Analiz (Limit, Türev, İntegral).
    **🕌 Din Kültürü:** İman Esasları, İbadetler, Kaza ve Kader.
    **🌙 Peygamber Hayatı:** Hicret, Vahiy, Savaşlar (Önemli Olaylar).
    """
)
st.sidebar.caption("Bu Uygulama **Yusuf Efe Şahin** Tarafından Geliştirilmiştir.")