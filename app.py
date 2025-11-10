import streamlit as st 
import time

# --- YÖNETİCİ GİRİŞİ AYARLARI VE OTURUM BAŞLATMA ---

# OTURUM DURUMU BAŞLANGIÇ DEĞERLERİ (Hata almamak için bu kısım burada BAŞLIYOR)
if 'admin_mode' not in st.session_state:
    st.session_state['admin_mode'] = False
if 'user_logged_in' not in st.session_state:
    st.session_state['user_logged_in'] = False
if 'current_user' not in st.session_state:
    st.session_state['current_user'] = None
if 'show_admin_login' not in st.session_state:
    st.session_state['show_admin_login'] = False
# ... (Diğer tüm st.session_state kodları buraya devam edecek) ...

# --- MODÜL VE KÜTÜPHANE İÇE AKTARMA ---
try:
    from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
    from english_content import konuyu_bul_eng, soru_cozumu_yap_eng
    from math_content import konuyu_bul_math, soru_cozumu_yap_math
    from history_content import konuyu_bul_history, soru_cozumu_yap_history
    from religion_content import konuyu_bul_religion, soru_cozumu_yap_religion
except ImportError as e:
    st.error(f"Eğitim İçerik Dosyası Hatası: Lütfen tüm içerik dosyalarının 'app.py' ile aynı dizinde olduğundan emin olun. Hata: {e}")
    # ... (Hata durumunda fonksiyonların boş tanımları buraya devam edecek) ...
    
# --- SAYFA VE SİMGE AYARLARI ---
st.set_page_config(
    page_title="Eğitim Robotu | Yusuf Efe Şahin",
    layout="wide",
    page_icon="📚"
)
# ... (KODUN KALANI BURADAN AŞAĞIYA HİÇBİR BOŞLUK OLMADAN DEVAM EDECEK) ...
