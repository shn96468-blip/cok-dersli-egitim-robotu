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
    st.session_state['admin_mode'] = False  # Bu satır 4 boşluk girintili olmalı
if 'user_logged_in' not in st.session_state:
    st.session_state['user_logged_in'] = False # Bu satır 4 boşluk girintili olmalı
if 'current_user' not in st.session_state:
    st.session_state['current_user'] = None    # Bu satır 4 boşluk girintili olmalı
# ... ve diğer 'if' blokları da aynı şekilde devam etmeli
