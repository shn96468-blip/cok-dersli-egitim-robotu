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


# --- DERS FONKSİYONLARI YEDEK TANIMLARI (Harici dosya import hatası vermemek için) ---
def konuyu_bul_yedek(ders, konu): 
    return f"🤖 İçerik dosyaları yüklenmediği için {ders} dersi '{konu}' konusu hakkında genel bilgi veriyorum: (Simülasyon Cevabı)"
    
def soru_cozumu_yap_yedek(ders, soru): 
    return f"🤖 İçerik dosyaları yüklenmediği için {ders} dersi '{soru}' sorusu çözülemiyor. (Simülasyon Cevabı)"

konuyu_bul_tr = lambda konu: konuyu_bul_yedek("Türkçe", konu)
soru_cozumu_yap_tr = lambda soru: soru_cozumu_yap_yedek("Türkçe", soru)
konuyu_bul_eng = lambda konu: konuyu_bul_yedek("İngilizce", konu)
soru_cozumu_yap_eng = lambda soru: soru_cozumu_yap_yedek("İngilizce", soru)
konuyu_bul_math = lambda konu: konuyu_bul_yedek("Matematik", konu)
soru_cozumu_yap_math = lambda soru: soru_cozumu_yap_yedek("Matematik", soru)
konuyu_bul_history = lambda konu: konuyu_bul_yedek("Tarih", konu)
soru_cozumu_
