import streamlit as st
import time

# --- MODÜL VE KÜTÜPHANE İÇE AKTARMA ---
# Hata olasılığına karşı, modül içe aktarmaları try-except bloğuna alınmıştır.
try:
    # Bu dosyaların (turkish_content.py, english_content.py, math_content.py) app.py ile aynı dizinde olduğundan emin olun.
    from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
    from english_content import konuyu_bul_eng, soru_cozumu_yap_eng
    from math_content import konuyu_bul_math, soru_cozumu_yap_math 
except ImportError as e:
    # Bu hata, içerik dosyalarının henüz boş veya eksik olmasından kaynaklanır. Uygulamanın çalışmasını engellemez.
    st.warning(f"Eğitim İçerik Dosyası Uyarısı: '{e.name}' dosyası bulunamadı veya içe aktarılamadı. İçerik alınamayacak. Lütfen dosyaları doldurun.")
    
    # Hata durumunda fonksiyonların boş tanımları
    def konuyu_bul_tr(konu): return f"İçerik modülü yüklenemediği için Türkçe '{konu}' konusu bulunamıyor."
    def soru_cozumu_yap_tr(soru): return f"İçerik modülü yüklenemediği için Türkçe '{konu}' sorusu çözülemiyor."
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

# OTURUM DURUMU BAŞLANGIÇ DEĞERLERİ (Tüm Hata Düzeltmeleri Yapıldı)
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
    st.session_state['user_
