import streamlit as st
# Gerekli içerik dosyaları
from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
from english_content import konuyu_bul_eng, soru_cozumu_yap_eng
from math_content import konuyu_bul_math, soru_cozumu_yap_math 

# --- SAYFA VE SİMGE AYARLARI (EN ÜSTTE OLMALI) ---
st.set_page_config(
    page_title="Eğitim Robotu",
    layout="wide",
    page_icon="📚" 
)

# --- YÖNETİCİ GİRİŞİ AYARLARI VE OTURUM BAŞLATMA (Hata Düzeltildi) ---
ADMIN_PASSWORD = "123" 

# Tüm session state değişkenlerini burada, kodun başında başlatıyoruz
if 'admin_mode' not in st.session_state:
    st.session_state['admin_mode'] = False
if 'show_admin_login' not in st.session_state:
    st.session_state['show_admin_login'] = False
if 'app_color' not in st.session_state:
    st.session_state['app_color'] = '#1E90FF' 
    
def attempt_admin_login(password):
    if password == ADMIN_PASSWORD:
        st.session_state['admin_mode'] = True
        st.session_state['show_admin_login'] = False
        st.experimental_rerun() # Sayfayı yenileme komutu
    else:
        st.error("Hatalı yönetici şifresi.")

def toggle_admin_login_panel():
    st.session_state['show_admin_login'] = not st.session_state['show_admin_login']
    
def admin_logout():
    st.session_state['admin_mode'] = False
    st.experimental_rerun() # Sayfayı yenileme komutu


# Yönetici Modunda Tema Rengi Uygulama (Gerekli)
if st.session_state['admin_mode']:
    st.markdown(f'<style>body {{ color: {st.session_state["app_color"]}; }}</style>', unsafe_allow_html=True)


# --- ANA ROBOT GÖVDESİ ---
st.title("📚 Çok Dersli Eğitim Robotu")

# Yönetici modu başlığı ve yeni özellikler
if st.session_state['admin_mode']:
    st.header(f"⚙️ YÖNETİCİ PANELİ (Aktif)")
    
    # 1. Site Görünümü Ayarları (YÖNETİCİ ÖZELLİĞİ)
    st.subheader("🎨 Site Görünümü ve Temel Ayarlar")
    
    yeni_renk = st.color_picker('Uygulama Rengini Seçin', st.session_state['app_color'])
    if yeni_renk != st.session_state['app_color']:
        st.session_state['app_color'] = yeni_renk
        st.experimental_rerun() 
        
    st.info(f"Uygulama Başlık Rengi: {st.session_state['app_color']}")
    
    st.markdown("---")
    
    # 2. İçerik Yönetimi Simülasyonu (YÖNETİCİ ÖZELLİĞİ)
    st.subheader("✍️ İçerik Güncelleme (Simülasyon)")
    st.caption("Bu özellik sadece görsel bir simülasyondur, konuları gerçekten dosyaya kaydetmez.")
    
    secilen_ders_admin = st.selectbox("İçerik Eklenecek Ders:", ("Türkçe", "İngilizce", "Matematik"), key="admin_select_ders")
    konu_basligi = st.text_input("Yeni Konu Başlığı:", key="admin_input_baslik")
    konu_detay = st.text_area("Konu Açıklaması (Detaylı):", key="admin_input_detay")
    
    if st.button("İçeriği Ekle", key="admin_button_ekle"):
        if konu_basligi and konu_detay:
            st.success(f"'{secilen_ders_admin}' dersine '{konu_basligi}' başlıklı **{len(konu_detay.split())} kelimelik** yeni içerik başarıyla EKLEME SİMÜLASYONU yapıldı!")
        else:
            st.warning("Lütfen başlık ve detay alanlarını doldurun.")

else:
    # Öğrenci Modu Karşılama
    st.markdown("Merhaba! Lütfen önce dersinizi seçin.")


# --- YÖNETİCİ/ÜYE GİRİŞİ (SIDEBAR) ---
st.sidebar.title("Kullanıcı İşlemleri")

# Yönetici Girişi Mantığı
if st.session_state['admin_mode']:
    st.sidebar.button("🔒 YÖNETİCİ ÇIKIŞI", on_click=admin_logout)
else:
    st.sidebar.button("🔒 Yönetici Girişi", on_click=toggle_admin_login_panel)
    
    if st.session_state['show_admin_login']:
        admin_pass = st.sidebar.text_input("Yönetici Şifresi", type="password", key="admin_pass_input")
        st.sidebar.button("Giriş Yap", on_click=attempt_admin_login, args=(admin_pass,))
        st.sidebar.info(f"Şifrenizi mi unuttunuz? Şifre ipucu: İlk üç sayı. (Gerçek Şifre: {ADMIN_PASSWORD})")


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

    # --- MOD VE DERS SEÇİMİ ---
    secilen_ders = st.selectbox(
        "Lütfen önce ilgili dersi seçin:",
        ("Türkçe", "İngilizce", "Matematik")
    )
    
    islem_modu = st.radio(
        "Şimdi yapmak istediğiniz işlemi seçin:",
        ("Konu Anlatımı", "Soru Çözümü", "Kelime Bilgisi"),
        horizontal=True
    )
    
    konu_adi = st.text_input(f"Aradığınız Konu Adını veya Kelimeyi Giriniz:")

    if st.button("Başlat"):
        if konu_adi:
            
            konu_adi_lower = konu_adi.lower().strip()
            konu_icerigi = "Üzgünüm, aradığınız konuyu/kelimeyi bulamadım."
            
            # --- ANA MANTIK ---
            if islem_modu == "Kelime Bilgisi":
                if secilen_ders == "Türkçe":
                    konu_icerigi = konuyu_bul_eng(konu_adi_lower) 
                elif secilen_ders == "İngilizce":
                    konu_icerigi = konuyu_bul_tr(konu_adi_lower)
                else: 
                    konu_icerigi = "Matematik dersinde Kelime Bilgisi modu desteklenmemektedir."
            
            
            # --- KONU ANLATIMI VE SORU ÇÖZÜMÜ MANTIKLARI ---
            else:
                if secilen_ders == "Türkçe":
                    if islem_modu == "Soru Çözümü":
                         konu_icerigi = soru_cozumu_yap_tr(konu_adi_lower)
                    else: 
                        konu_icerigi = konuyu_bul_tr(konu_adi_lower)
                
                elif secilen_ders == "İngilizce":
                    if islem_modu == "Soru Çözümü":
                         konu_icerigi = soru_cozumu_yap_eng(konu_adi_lower)
                    else: 
                        konu_icerigi = konuyu_bul_eng(konu_adi_lower)
                
                elif secilen_ders == "Matematik":
                    if islem_modu == "Soru Çözümü":
                         konu_icerigi = soru_cozumu_yap_math(konu_adi_lower)
                    else: 
                        kon
