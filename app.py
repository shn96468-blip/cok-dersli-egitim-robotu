import streamlit as st
from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
from english_content import konuyu_bul_eng, soru_cozumu_yap_eng
from math_content import konuyu_bul_math, soru_cozumu_yap_math


# --- SİMGE VE TEMEL AYARLAR ---
if 'admin_mode' not in st.session_state:
    st.session_state['admin_mode'] = False
if 'current_icon' not in st.session_state:
    st.session_state['current_icon'] = "📚" 

st.set_page_config(
    page_title="Çok Dersli Eğitim Robotu",
    layout="wide",
    page_icon=st.session_state['current_icon']
)


# --- YÖNETİCİ GİRİŞ FONKSİYONLARI ---
def login_admin():
    st.session_state['admin_mode'] = True
    st.experimental_rerun()
def logout_admin():
    st.session_state['admin_mode'] = False
    st.experimental_rerun()

# Yönetici Paneli Fonksiyonu
def show_admin_panel():
    st.sidebar.title("🛠️ YÖNETİCİ PANELİ")
    st.warning("Bu panel, sadece bu oturum için simge ve içerik ayarlarını değiştirir.")
    
    # 1. SİMGE AYARI
    st.sidebar.subheader("1. Site Simgesi Ayarı")
    yeni_simge = st.sidebar.text_input("Yeni Simge Emojisi (Örn: 🚀, 💡)", value=st.session_state['current_icon'])
    
    if yeni_simge != st.session_state['current_icon']:
        st.session_state['current_icon'] = yeni_simge
        st.experimental_rerun()

    # 🌟 2. RENK AYARI (YENİ EKLENDİ)
    st.sidebar.subheader("2. Tema Renk Seçimi")
    # Gerçek bir renk seçici widget'ı ekliyoruz
    secilen_renk = st.sidebar.color_picker('Ana Vurgu Rengini Seçin', '#5B9BD5')
    
    if st.sidebar.button("Temayı Uygula"):
        # Bu buton, renk seçimi deneyimini yaşatır ancak global temayı kalıcı değiştirmez.
        st.toast(f"Seçilen renk: {secilen_renk} ile tema uygulandı! (Geçici)")
        st.info("Ana tema renginiz `.streamlit/config.toml` dosyasında ayarlanmıştır. Bu renk seçimi sadece görsel bir bildirimdir.")


# --- KENAR ÇUBUĞU VE GİRİŞ BÖLÜMÜ ---
st.sidebar.title("Kullanıcı İşlemleri")
col_y, col_u = st.sidebar.columns(2)

if st.session_state['admin_mode']:
    col_y.button("🔒 YÖNETİCİ ÇIKIŞI", on_click=logout_admin)
    show_admin_panel()
else:
    col_y.button("🔒 Yönetici Girişi", on_click=login_admin)
    col_u.button("👤 Üye Girişi (Pasif)")
    st.sidebar.markdown("---") 
    st.sidebar.title("Kullanılabilir Dersler")
    st.sidebar.markdown(
        """
        **🇹🇷 Türkçe (7. Sınıf):** Dil Bilgisi ve Anlam Konuları.
        **🇬🇧 İngilizce:** Tenses ve Vocabulary.
        **📐 Matematik (12. Sınıfa Kadar):** Sayılar, Denklemler, Analiz.
        """
    )
    st.sidebar.caption("Bu Uygulama Yusuf Efe Şahin Tarafından Geliştirilmiştir.")

# --- ANA ROBOT GÖVDESİ (SADECE GEREKLİ KISIMLAR) ---
st.title(f"{st.session_state['current_icon']} Çok Dersli Eğitim Robotu")

if not st.session_state['admin_mode']:
    
    islem_modu = st.radio(
        "Lütfen yapmak istediğiniz işlemi seçin:",
        ("Konu Anlatımı", "Soru Çözümü", "Soru Sorma (Detaylı Cevap)"),
        horizontal=True
    )

    konu_adi = st.text_input(f"İstediğiniz Konu Adını veya Soruyu Giriniz:")

    konusma_acik = st.checkbox("Robotun Cevabı Sesli Olarak Vermesini İster misiniz?")

    ingilizce_anahtarlar = ['tense', 'modal', 'present', 'future', 'to be', 'vocabulary', 'adjective', 'adverb']
    matematik_anahtarlar = ['sayı', 'denklem', 'oran', 'alan', 'çevre', 'limit', 'türev', 'integral']

    if st.button("Başlat"):
        if konu_adi:
            
            konu_adi_lower = konu_adi.lower().strip()
            konu_icerigi = "Üzgünüm, aradığınız konuyu bulamadım."
            soru_cevabi = "Soru çözümü için uygun içerik bulunamadı."
            
            if any(keyword in konu_adi_lower for keyword in matematik_anahtarlar):
                konu_icerigi = konuyu_bul_math(konu_adi_lower)
                soru_cevabi = soru_cozumu_yap_math(konu_adi_lower)
            elif any(keyword in konu_adi_lower for keyword in ingilizce_anahtarlar):
                konu_icerigi = konuyu_bul_eng(konu_adi_lower)
                soru_cevabi = soru_cozumu_yap_eng(konu_adi_lower)
            else:
                konu_icerigi = konuyu_bul_tr(konu_adi_lower)
                soru_cevabi = soru_cozumu_yap_tr(konu_adi_lower)

            
            if islem_modu == "Konu Anlatımı" or islem_modu == "Soru Sorma (Detaylı Cevap)":
                
                if "Üzgünüm" not in konu_icerigi:
                    st.success(f"İşte '{konu_adi.upper()}' sorusuna/konusuna ait detaylı cevap:")
                    st.markdown(konu_icerigi)
                else:
                    st.warning(f"Üzgünüm, aradığınız '{konu_adi}' sorusunu mevcut konu sözlüklerimde bulamadım.")
            
            elif islem_modu == "Soru Çözümü":
                
                if "Üzgünüm" not in konu_icerigi:
                    st.info(f"'{konu_adi.upper()}' konusu için bir örnek soru çözümü:")
                    st.markdown(soru_cevabi)
                else:
                    st.warning("Konu bulunamadığı için örnek soru çözümü yapılamadı.")
