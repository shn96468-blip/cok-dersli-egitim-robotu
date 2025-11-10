import streamlit as st
from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
from english_content import konuyu_bul_eng, soru_cozumu_yap_eng
from math_content import konuyu_bul_math, soru_cozumu_yap_math 
import time

# --- SAYFA VE SİMGE AYARLARI ---
st.set_page_config(
    page_title="Eğitim Robotu | Yusuf Efe Şahin",
    layout="wide",
    page_icon="📚" 
)

# --- YÖNETİCİ GİRİŞİ AYARLARI VE OTURUM BAŞLATMA ---
ADMIN_PASSWORD = "123" 
# SIMÜLASYON KULLANICILARI (Demo Hesaplar: ali/a123, ayse/a456)
MOCK_USERS = [
    {"username": "ali", "email": "ali@okul.com", "password_hash": "a123"},
    {"username": "ayse", "email": "ayse@okul.com", "password_hash": "a456"},
]

# OTURUM DURUMU BAŞLANGIÇ DEĞERLERİ
if 'admin_mode' not in st.session_state:
    st.session_state['admin_mode'] = False
if 'user_logged_in' not in st.session_state:
    st.session_state['user_logged_in'] = False
if 'current_user' not in st.session_state:
    st.session_state['current_user'] = None
if 'show_admin_login' not in st.session_state:
    st.session_state['show_admin_login'] = False
if 'show_user_login' not in st.session_state:
    st.session_state['show_user_login'] = False
if 'show_user_register' not in st.session_state:
    st.session_state['show_user_register'] = False
if 'app_color' not in st.session_state:
    st.session_state['app_color'] = '#1E90FF' 
if 'announcement' not in st.session_state:
    st.session_state['announcement'] = "🤖 Eğitim robotu aktif! Yeni konuları keşfetmeye başlayın."
if 'announcement_color' not in st.session_state:
    st.session_state['announcement_color'] = 'warning' 
if 'registration_allowed' not in st.session_state:
    st.session_state['registration_allowed'] = True 
if 'user_login_allowed' not in st.session_state:
    st.session_state['user_login_allowed'] = True 
if 'chat_history' not in st.session_state: # Yeni Özellik: Sohbet geçmişi
    st.session_state['chat_history'] = []
    
# --- GİRİŞ/ÇIKIŞ FONKSİYONLARI ---

def attempt_admin_login(password):
    if password == ADMIN_PASSWORD:
        st.session_state['admin_mode'] = True
        st.session_state['show_admin_login'] = False
        st.rerun() 
    else:
        st.error("Hatalı yönetici şifresi.")

def admin_logout():
    st.session_state['admin_mode'] = False
    st.rerun() 

def user_login(username, password):
    if not st.session_state['user_login_allowed']:
        st.error("Üye girişi şu anda bakımdadır. Lütfen daha sonra tekrar deneyin.")
        return
        
    for user in MOCK_USERS:
        if user["username"] == username and user["password_hash"] == password:
            st.session_state['user_logged_in'] = True
            st.session_state['current_user'] = username
            st.session_state['show_user_login'] = False
            st.success(f"Hoş geldiniz, {username.upper()}!")
            time.sleep(1)
            st.rerun()
            return
    st.error("Kullanıcı adı veya şifre yanlış.")

def user_logout():
    st.session_state['user_logged_in'] = False
    st.session_state['current_user'] = None
    st.rerun()

# --- MOD AÇMA/KAPAMA FONKSİYONLARI ---

def toggle_admin_login_panel():
    st.session_state['show_admin_login'] = not st.session_state['show_admin_login']
    st.session_state['show_user_login'] = False
    st.session_state['show_user_register'] = False

def toggle_user_login_panel():
    if st.session_state['user_login_allowed']:
        st.session_state['show_user_login'] = not st.session_state['show_user_login']
        st.session_state['show_admin_login'] = False
        st.session_state['show_user_register'] = False
    else:
        st.sidebar.error("Üye girişi şu anda bakımdadır.")

def toggle_user_register_panel():
    if st.session_state['registration_allowed']:
        st.session_state['show_user_register'] = not st.session_state['show_user_register']
        st.session_state['show_admin_login'] = False
        st.session_state['show_user_login'] = False
    else:
        st.sidebar.error("Yeni kayıtlar şu anda kapalıdır.")


# --- ŞİFRE UNUTTUM SIMÜLASYONU ---
def forgot_password_simulation(email_or_username, is_admin=False):
    st.sidebar.warning("Sistemimiz simülasyon modunda olduğundan, şifre sıfırlama linki kayıtlı e-posta adresinize gönderilmiştir.")
    time.sleep(1)
    if is_admin:
        st.sidebar.success(f" Yönetici Şifresi sıfırlama maili 'admin@robot.com' adresine gönderildi.")
    else:
        user_email = "kayıtlı_eposta_adresi"
        for user in MOCK_USERS:
            if user["username"] == email_or_username:
                user_email = user["email"]
                break
        
        st.sidebar.success(f" Kullanıcı şifresi sıfırlama linki '{user_email}' adresine gönderildi.")

# --- METİN OKUMA FONKSİYONU ---
def metin_oku(text):
    """Verilen metni tarayıcının yerleşik Text-to-Speech motoru ile seslendirir."""
    clean_text = text.replace('"', '').replace('\n', ' ')
    js_code = f"""
    <script>
        var utterance = new SpeechSynthesisUtterance("{clean_text}");
        window.speechSynthesis.speak(utterance);
    </script>
    """
    st.markdown(js_code, unsafe_allow_html=True)

# --- SOHBET VE ÇEVİRİ MANTIKLARI ---
def sohbet_ve_cevir(kullanici_mesaji):
    mesaj_lower = kullanici_mesaji.lower().strip()
    
    # 1. Hazır Cevaplar (Sohbet)
    if "merhaba" in mesaj_lower or "selam" in mesaj_lower:
        cevap = "Merhaba! Ben yapay zeka destekli eğitim robotuyum. Nasıl yardımcı olabilirim?"
    elif "adın ne" in mesaj_lower or "kimsin" in mesaj_lower:
        cevap = "Ben Yusuf Efe Şahin tarafından geliştirilen Çok Dersli Eğitim Robotuyum."
    elif "teşekkür" in mesaj_lower or "sağol" in mesaj_lower:
        cevap = "Rica ederim, her zaman buradayım!"
        
    # 2. Basit Çeviri Simülasyonu
    elif "çevir" in mesaj_lower or "translate" in mesaj_lower:
        # Basit bir anahtar kelime tabanlı çeviri simülasyonu
        if "elma" in mesaj_lower:
            cevap = "Kelime: Elma. İngilizce Çevirisi: Apple."
        elif "apple" in mesaj_lower:
            cevap = "Kelime: Apple. Türkçe Çevirisi: Elma."
        elif "again" in mesaj_lower:
            cevap = "Kelime: Again. Türkçe Çevirisi: Tekrar/Yine."
        else:
            cevap = f"'{kullanici_mesaji}' ifadesi için çeviri simülasyonu yapıldı. Gerçek bir dil modeli ile anlık çeviri yapabilirim."
            
    # 3. Genel Cevaplar (Eğitim)
    else:
        cevap = f"Anladım, '{kullanici_mesaji}' hakkında bilgi istiyorsunuz. Lütfen yukarıdaki menüden dersinizi ve işlem modunu seçerek detaylı bilgi almayı deneyin."
        
    st.session_state.chat_history.append({"user": kullanici_mesaji, "robot": cevap})
    return cevap
    
    
# Yönetici Modunda Tema Rengi Uygulama
if st.session_state['admin_mode']:
    st.markdown(f'<style>h1, h2, h3, h4, h5, h6 {{color: {st.session_state["app_color"]};}}</style>', unsafe_allow_html=True)
else:
    st.markdown(f'<style>h1, h2, h3, h4, h5, h6 {{color: #FFFFFF;}}</style>', unsafe_allow_html=True)


# --- ANA ROBOT GÖVDESİ ---
st.title("📚 Çok Dersli Eğitim Robotu")

# YÖNETİCİ PANELİ
if st.session_state['admin_mode']:
    st.header(f"⚙️ YÖNETİCİ PANELİ (Aktif)")
    
    # 1. Renk ve Temel Ayarlar
    st.subheader("🎨 Site Görünümü ve Temel Ayarlar")
    col_app_color, col_duyuru_color = st.columns(2)
    with col_app_color:
        yeni_renk = st.color_picker('Uygulama Vurgu Rengini Seçin', st.session_state['app_color'])
        if yeni_renk != st.session_state['app_color']:
            st.session_state['app_color'] = yeni_renk
            st.rerun() 
        st.info(f"Uygulama Vurgu Rengi: {st.session_state['app_color']}")
    
    with col_duyuru_color:
        yeni_duyuru_color = st.selectbox(
            'Duyuru Vurgu Rengini Seçin:', 
            ('warning', 'info', 'success', 'error'), 
            index=('warning', 'info', 'success', 'error').index(st.session_state['announcement_color'])
        )
        if yeni_duyuru_color != st.session_state['announcement_color']:
            st.session_state['announcement_color'] = yeni_duyuru_color
            st.rerun() 
        st.info(f"Duyuru Rengi: {st.session_state['announcement_color']}")
        

    st.markdown("---")
    
    # 2. Üye Girişi / Kaydı Kontrolü
    st.subheader("🔒 Kullanıcı Erişim Kontrolü")
    col_login, col_reg = st.columns(2)
    with col_login:
        yeni_login_izin = st.checkbox("Üye Girişine İzin Ver", st.session_state['user_login_allowed'])
        if yeni_login_izin != st.session_state['user_login_allowed']:
            st.session_state['user_login_allowed'] = yeni_login_izin
            st.rerun()
            
    with col_reg:
        yeni_reg_izin = st.checkbox("Yeni Kayda İzin Ver", st.session_state['registration_allowed'])
        if yeni_reg_izin != st.session_state['registration_allowed']:
            st.session_state['registration_allowed'] = yeni_reg_izin
            st.rerun()
            
    st.caption("Bakım veya yoğunluk durumunda girişleri kapatabilirsiniz.")
    st.markdown("---")

    # 3. İçerik Güncelleme Simülasyonu
    st.subheader("✍️ İçerik Güncelleme (Simülasyon)")
    secilen_ders_admin = st.selectbox("İçerik Eklenecek Ders:", ("Türkçe", "İngilizce", "Matematik"), key="admin_select_ders")
    konu_basligi = st.text_input("Yeni Konu Başlığı:", key="admin_input_baslik")
    konu_detay = st.text_area("Konu Açıklaması (Detaylı):", key="admin_input_detay")
    if st.button("İçeriği Ekle", key="admin_button_ekle"):
        if konu_basligi and konu_detay:
            st.success(f"'{secilen_ders_admin}' dersine '{konu_basligi}' başlıklı yeni içerik başarı
