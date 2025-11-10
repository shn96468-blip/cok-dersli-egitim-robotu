import streamlit as st
# TÜRKÇE VE İNGİLİZCE modüllerini çağırıyoruz
from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
from english_content import konuyu_bul_eng, soru_cozumu_yap_eng


# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Türkçe ve İngilizce Asistanı",
    layout="wide"
)

# --- ANA ROBOT EKRANI ---
st.title("🇹🇷🇬🇧 Türkçe (7. Sınıf) ve İngilizce Konu Anlatım Robotu")
st.markdown("Merhaba! 7. Sınıf Türkçe ve Temel İngilizce konularında uzmanlaşmış bir robotum. Hangi konuda bilgi istersin (Örn: **ek fiil**, **simple present tense**):")

# Mod Seçimi
islem_modu = st.radio(
    "Lütfen yapmak istediğiniz işlemi seçin:",
    ("Konu Anlatımı", "Soru Çözümü"),
    horizontal=True
)

konu_adi = st.text_input(f"İstediğiniz Konu Adını Giriniz (Örn: **ek fiil** veya **simple present tense**):")

# Sesli Konuşma Kontrolü
konusma_acik = st.checkbox("Robotun Konuyu Sesli Anlatmasını İster misiniz?")

# İngilizce anahtar kelimeler
ingilizce_anahtarlar = ['tense', 'modal', 'present', 'future', 'to be', 'vocabulary', 'friendship', 'teen life', 'tourism', 'adjective', 'adverb']


# Yanıt düğmesi
if st.button("Başlat"):
    if konu_adi:
        
        konu_adi_lower = konu_adi.lower().strip()
        konu_icerigi = "Üzgünüm, aradığınız konuyu bulamadım."
        
        # Hangi dilde arama yapılacağını belirleme (İngilizce mi? Türkçe mi?)
        if any(keyword in konu_adi_lower for keyword in ingilizce_anahtarlar):
            konu_icerigi = konuyu_bul_eng(konu_adi_lower)
            soru_cevabi = soru_cozumu_yap_eng(konu_adi_lower)
        else:
            konu_icerigi = konuyu_bul_tr(konu_adi_lower)
            soru_cevabi = soru_cozumu_yap_tr(konu_adi_lower)


        # --- Konu Anlatımı Modu ---
        if islem_modu == "Konu Anlatımı":
            
            if "Üzgünüm" not in konu_icerigi:
                st.success(f"İşte '{konu_adi.upper()}' konusu ile ilgili bilmen gerekenler:")
                st.markdown(konu_icerigi)

            else:
                st.warning(konu_icerigi)
        
        # --- Soru Çözümü Modu ---
        elif islem_modu == "Soru Çözümü":
                            
            if "Üzgünüm" not in konu_icerigi:
                st.info(f"'{konu_adi.upper()}' konusu için bir örnek soru çözümü:")
                st.markdown(soru_cevabi)
            else:
                st.warning("Konu bulunamadığı için örnek soru çözümü yapılamadı.")

        # Sesli okuma (Eğer açıksa)
        if konusma_acik and "Üzgünüm" not in (konu_icerigi if islem_modu == "Konu Anlatımı" else soru_cevabi):
            sesli_metin = konu_icerigi if islem_modu == "Konu Anlatımı" else soru_cevabi
            st.components.v1.html(f"""
                <script>
                    const text = `{sesli_metin.replace("`", "")}`; 
                    const utterance = new SpeechSynthesisUtterance(text);
                    utterance.lang = 'tr-TR'; // Türkçe için
                    if (text.includes("English")) {{ utterance.lang = 'en-US'; }} // İngilizce için dil değiştirme
                    utterance.rate = 1.0; 
                    speechSynthesis.speak(utterance);
                </script>
            """, height=0)

    else:
        st.error("Lütfen bir konu adı giriniz.")

# --- KENAR ÇUBUĞU VE ALT BÖLÜM ---
st.sidebar.title("Kullanılabilir Dersler")
st.sidebar.markdown(
    """
    **🇹🇷 Türkçe (7. Sınıf):** Dil Bilgisi (Fiil, Ek Fiil), Anlam Bilgisi, Yazım-Noktalama.
    **🇬🇧 İngilizce:** Tenses, Modals, Kelime Bilgisi (Vocabulary).
    """
)
st.sidebar.caption("Bu Uygulama **Yusuf Efe Şahin** Tarafından Geliştirilmiştir.")
