import streamlit as st
import time

# --- YÖNETİCİ GİRİŞİ AYARLARI VE OTURUM BAŞLATMA ---
ADMIN_PASSWORD = "123"
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
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'secilen_ders' not in st.session_state:
    st.session_state['secilen_ders'] = None
if 'show_kanka_chat' not in st.session_state:
    st.session_state['show_kanka_chat'] = False
if 'music_enabled' not in st.session_state:
    st.session_state['music_enabled'] = False
if 'music_url' not in st.session_state:
    st.session_state['music_url'] = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"


# --- MODÜL VE KÜTÜPHANE İÇE AKTARMA (Hata Kontrollü) ---
# Varsayılan (Yedek) Fonksiyonlar Tanımlanır
def yedek_konu(ders, konu): return f"İçerik modülü yüklenemediği için {ders} dersi '{konu}' konusu bulunamıyor."
def yedek_soru(ders, soru): return f"İçerik modülü yüklenemediği için {ders} dersi '{soru}' sorusu çözülemiyor."

# Fonksiyon Atamaları (Varsayılan olarak yedek fonksiyonlar atanır)
konuyu_bul_tr = lambda konu: yedek_konu("Türkçe", konu)
soru_cozumu_yap_tr = lambda soru: yedek_soru("Türkçe", soru)
konuyu_bul_eng = lambda konu: yedek_konu("İngilizce", konu)
soru_cozumu_yap_eng = lambda soru: yedek_soru("İngilizce", soru)
konuyu_bul_math = lambda konu: yedek_konu("Matematik", konu)
soru_cozumu_yap_math = lambda soru: yedek_soru("Matematik", soru)
konuyu_bul_history = lambda konu: yedek_konu("Tarih", konu)
soru_cozumu_yap_history = lambda soru: yedek_soru("Tarih", soru)
konuyu_bul_religion = lambda konu: yedek_konu("Din K.", konu)
soru_cozumu_yap_religion = lambda soru: yedek_soru("Din K.", soru)


# Başarılı İçe Aktarma Denemesi (Sadece varsa yükler, hata vermez)
try:
    from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
except ImportError:
    st.info("🇹🇷 Türkçe İçerik Dosyası Bulunamadı. Simülasyon Devam Ediyor.")

try:
    from english_content import konuyu_bul_eng, soru_cozumu_yap_eng
except ImportError:
    st.info("🇬🇧 İngilizce İçerik Dosyası Bulunamadı. Simülasyon Devam Ediyor.")
    
try:
    from math_content import konuyu_bul_math, soru_cozumu_yap_math
except ImportError:
    st.info("📐 Matematik İçerik Dosyası Bulunamadı. Simülasyon Devam Ediyor.")
    
try:
    from history_content import konuyu_bul_history, soru_cozumu_yap_history
except ImportError:
    st.info("🏛️ Tarih İçerik Dosyası Bulunamadı. Simülasyon Devam Ediyor.")
    
try:
    from religion_content import konuyu_bul_religion, soru_cozumu_yap_religion
except ImportError:
    st.info("🕌 Din Kültürü İçerik Dosyası Bulunamadı. Simülasyon Devam Ediyor.")

# --- SAYFA VE SİMGE AYARLARI ---
st.set_page_config(
    page_title="Eğitim Robotu | Yusuf Efe Şahin",
    layout="wide",
    page_icon="📚"
)

# --- GİRİŞ/ÇIKIŞ FONKSİYONLARI (Kısaltıldı) ---
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

def forgot_password_simulation(email_or
