import streamlit as st
# SADECE MEVCUT DERSLERİ ÇAĞIRIYORUZ
from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
from english_content import konuyu_bul_eng, soru_cozumu_yap_eng
from math_content import konuyu_bul_math, soru_cozumu_yap_math 

# --- YÖNETİCİ GİRİŞİ AYARLARI (AYNI KALDI) ---
ADMIN_PASSWORD = "123" 
if 'admin_mode' not in st.session_state:
    st.session_state['admin_mode'] = False
if 'show_admin_login' not in st.session_state:
    st.session_state['show_admin_login'] = False
    
def attempt_admin_login(password):
    if password == ADMIN_PASSWORD:
        st.session_state['admin_mode'] = True
        st.session_state['show_admin_login'] = False
        st.rerun() 
    else:
        st.error("Hatalı yönetici şifresi.")

def toggle_admin_login_panel():
    st.session_state['show_admin_login'] = not st.session_state['show_admin_login']
    
def admin_logout():
    st.session_state['admin_mode'] = False
    st.rerun() 


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
    st.warning(f"Bu mod aktiftir. Yönetici Şifresi: '{ADMIN_PASSWORD}'") 
else:
    st.markdown("Merhaba! Lütfen önce dersinizi seçin.")


# --- YÖNETİCİ/ÜYE GİRİŞİ (SIDEBAR AYNI KALDI) ---
st.sidebar.title("Kullanıcı İşlemleri")
if st.session_state['admin_mode']:
    st.sidebar.button("🔒 YÖNETİCİ ÇIKIŞI", on_click=admin_logout)
else:
    st.sidebar.button("🔒 Yönetici Girişi", on_click=toggle_admin_login_panel)
    
    if st.session_state['show_admin_login']:
        admin_pass = st.sidebar.text_input("Yönetici Şifresi", type="password", key="admin_pass_input")
        st.sidebar.button("Giriş Yap", on_click=attempt_admin_login, args=(admin_pass,))

st.sidebar.button("👤 Üye Girişi (Pasif)", on_click=lambda: st.sidebar.warning("Üye Girişi özelliği geliştirme aşamasındadır."))
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

    # --- YENİ AKIŞ: ÖNCE DERS, SONRA İŞLEM ---
    
    # 1. Ders Seçimi: En Üste Çıktı
    secilen_ders = st.selectbox(
        "Lütfen önce ilgili dersi seçin:",
        ("Türkçe", "İngilizce", "Matematik")
    )
    
    # 2. İşlem Modu
    islem_modu = st.radio(
        "Şimdi yapmak istediğiniz işlemi seçin:",
        ("Konu Anlatımı", "Soru Çözümü", "Kelime Çevirisi"),
        horizontal=True
    )
    

    konu_adi = st.text_input(f"Aradığınız Konu Adını, Kelimeyi veya Çevrilecek Metni Giriniz:")

    if st.button("Başlat"):
        if konu_adi:
            
            konu_adi_lower = konu_adi.lower().strip()
            konu_icerigi = "Üzgünüm, aradığınız konuyu/kelimeyi bulamadım. Lütfen seçili derse ait bir konu başlığı veya geçerli bir kelime deneyin."
            
            
            # --- ANA MANTIK (AYNI KALDI) ---
            if secilen_ders == "Türkçe":
                if islem_modu == "Kelime Çevirisi":
                    konu_icerigi = konuyu_bul_eng(konu_adi_lower) 
                elif islem_modu == "Soru Çözümü":
                     konu_icerigi = soru_cozumu_yap_tr(konu_adi_lower)
                else: 
                    konu_icerigi = konuyu_bul_tr(konu_adi_lower)
            
            elif secilen_ders == "İngilizce":
                if islem_modu == "Kelime Çevirisi":
                    konu_icerigi = konuyu_bul_tr(konu_adi_lower) 
                elif islem_modu == "Soru Çözümü":
                     konu_icerigi = soru_cozumu_yap_eng(konu_adi_lower)
                else: 
                    konu_icerigi = konuyu_bul_eng(konu_adi_lower)
            
            elif secilen_ders == "Matematik":
                if islem_modu == "Kelime Çevirisi":
                    konu_icerigi = "Matematik dersinde çeviri modu desteklenmemektedir."
                elif islem_modu == "Soru Çözümü":
                     konu_icerigi = soru_cozumu_yap_math(konu_adi_lower)
                else: 
                    konu_icerigi = konuyu_bul_math(konu_adi_lower)

            
            # Sonucu Ekrana Yazdırma
            if "Üzgünüm" not in konu_icerigi and "desteklenmemektedir" not in konu_icerigi:
                if islem_modu == "Kelime Çevirisi":
                    st.success(f"İşte '{konu_adi.upper()}' için ÇEVİRİ/BİLGİ:")
                else:
                    st.success(f"İşte '{konu_adi.upper()}' için cevap/açıklama:")
                st.markdown(konu_icerigi)
            else:
                st.warning(konu_icerigi)

        else:
            st.error("Lütfen bir konu adı, kelime veya çevrilecek metin giriniz.")
