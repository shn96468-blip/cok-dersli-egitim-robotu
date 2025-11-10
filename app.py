import streamlit as st
from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
from english_content import konuyu_bul_eng, soru_cozumu_yap_eng
from math_content import konuyu_bul_math, soru_cozumu_yap_math 


# --- 1. YÖNETİCİ GİRİŞİ İÇİN SESSION STATE ---
# Robotun, kullanıcının Yönetici modunda olup olmadığını hatırlamasını sağlar.
if 'admin_mode' not in st.session_state:
    st.session_state['admin_mode'] = False
    
def toggle_admin_mode():
    """Yönetici giriş/çıkış modunu değiştirir ve uygulamayı yeniden başlatır."""
    st.session_state['admin_mode'] = not st.session_state['admin_mode']
    st.experimental_rerun() # Sayfanın yenilenmesini sağlar.
    
# --- SAYFA VE SİMGE AYARLARI ---
st.set_page_config(
    page_title="Eğitim Robotu",
    layout="wide",
    page_icon="📚" 
)

# --- ANA ROBOT GÖVDESİ ---
st.title("📚 Çok Dersli Eğitim Robotu")

# Yönetici modu başlığı
if st.session_state['admin_mode']:
    st.header("⚙️ YÖNETİCİ PANELİ")
    st.warning("Bu mod aktiftir. Buraya Site Ayarları Kodları Eklenebilir.")
else:
    st.markdown("Merhaba! Türkçe, İngilizce ve Matematik konularında uzmanlaşmış bir robotum. Hangi konuda bilgi istersin?")


# --- 2. YÖNETİCİ/ÜYE GİRİŞİ (ARTIK ÇALIŞIYOR) ---
st.sidebar.title("Kullanıcı İşlemleri")
if st.session_state['admin_mode']:
    # Yönetici modundaysa "Çıkış" butonu göster
    st.sidebar.button("🔒 YÖNETİCİ ÇIKIŞI", on_click=toggle_admin_mode)
else:
    # Yönetici modunda değilse "Giriş" butonu göster
    st.sidebar.button("🔒 Yönetici Girişi", on_click=toggle_admin_mode) 

st.sidebar.button("👤 Üye Girişi (Pasif)")
st.sidebar.markdown("---") 

# --- DERS LİSTESİ ---
st.sidebar.title("Kullanılabilir Dersler")
st.sidebar.markdown(
    """
    **🇹🇷 Türkçe (7. Sınıf)**
    **🇬🇧 İngilizce**
    **📐 Matematik**
    """
)
st.sidebar.caption("Bu Uygulama Yusuf Efe Şahin Tarafından Geliştirilmiştir.")


# SADECE ÖĞRENCİ MODUNDA İSE GÖSTER
if not st.session_state['admin_mode']:

    # --- MOD SEÇİMİ VE ARAMA ---
    islem_modu = st.radio(
        "Lütfen yapmak istediğiniz işlemi seçin:",
        ("Konu Anlatımı", "Soru Çözümü", "Soru Sorma (Detaylı Cevap)"),
        horizontal=True
    )

    konu_adi = st.text_input(f"İstediğiniz Konu Adını veya Soruyu Giriniz:")

    # 3. MATEMATİK ANAHTARLARI GÜNCELLENDİ
    # Robotun daha kolay anlaması için 'matematik' ve 'geometri' kelimeleri eklendi
    ingilizce_anahtarlar = ['tense', 'modal', 'present', 'future', 'to be', 'vocabulary', 'adjective', 'adverb']
    matematik_anahtarlar = ['matematik', 'geometri', 'sayı', 'denklem', 'oran', 'alan', 'çevre', 'limit', 'türev', 'integral']


    if st.button("Başlat"):
        if konu_adi:
            
            konu_adi_lower = konu_adi.lower().strip()
            konu_icerigi = "Üzgünüm, aradığınız konuyu bulamadım."
            
            # Hangi derste arama yapılacağını belirleme (Matematik ilk kontrol edilir)
            if any(keyword in konu_adi_lower for keyword in matematik_anahtarlar):
                konu_icerigi = konuyu_bul_math(konu_adi_lower)
                if islem_modu == "Soru Çözümü":
                     konu_icerigi = soru_cozumu_yap_math(konu_adi_lower)
            elif any(keyword in konu_adi_lower for keyword in ingilizce_anahtarlar):
                konu_icerigi = konuyu_bul_eng(konu_adi_lower)
                if islem_modu == "Soru Çözümü":
                     konu_icerigi = soru_cozumu_yap_eng(konu_adi_lower)
            else: # Varsayılan Türkçe
                konu_icerigi = konuyu_bul_tr(konu_adi_lower)
                if islem_modu == "Soru Çözümü":
                     konu_icerigi = soru_cozumu_yap_tr(konu_adi_lower)

            
            # Sonucu Ekrana Yazdırma
            if "Üzgünüm" not in konu_icerigi:
                st.success(f"İşte '{konu_adi.upper()}' için cevap/açıklama:")
                st.markdown(konu_icerigi)
            else:
                st.warning(konu_icerigi)

        else:
            st.error("Lütfen bir konu adı veya sorusu giriniz.")
