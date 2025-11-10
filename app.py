import streamlit as st
import time

# --- MODÜL VE KÜTÜPHANE İÇE AKTARMA ---
# Hata olasılığına karşı, modül içe aktarmaları try-except bloğuna alınmıştır.
try:
    # Not: Bu dosyaların (turkish_content.py, english_content.py, math_content.py) app.py ile aynı dizinde olduğundan emin olun.
    from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
    from english_content import konuyu_bul_eng, soru_cozumu_yap_eng
    from math_content import konuyu_bul_math, soru_cozumu_yap_math 
except ImportError as e:
    st.error(f"Eğitim İçerik Dosyası Hatası: Lütfen 'turkish_content.py', 'english_content.py' ve 'math_content.py' dosyalarının 'app.py' ile aynı dizinde olduğundan emin olun. Hata: {e}")
    # Hata durumunda fonksiyonların boş tanımları
    def konuyu_bul_tr(konu): return f"İçerik modülü yüklenemediği için Türkçe '{konu}' konusu bulunamıyor."
    def soru_cozumu_yap_tr(soru): return f"İçerik modülü yüklenemediği için Türkçe '{soru}' sorusu çözülemiyor."
    def konuyu_bul_eng(konu): return f"İçerik modülü yüklenemediği için İngilizce '{konu}' konusu bulunamıyor."
    def soru_cozumu_yap_eng(soru): return f"İçerik modülü yüklenemediği için İngilizce '{konu}' sorusu çözülemiyor."
    def konuyu_bul_math(konu): return f"İçerik modülü yüklenemediği için Matematik '{konu}' konusu bulunamıyor."
    def soru_cozumu_yap_math(soru): return f"İçerik modülü yüklenemediği için Matematik '{konu}' sorusu çözülemiyor."


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

# OTURUM DURUMU BAŞLANGIÇ DEĞERLERİ (Hata almamak için kodun en başında tanımlanmıştır)
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
if 'chat_history' not in st.session_state: 
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
def soh
