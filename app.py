import streamlit as st 
import time

# OTURUM DURUMU BAŞLANGIÇ DEĞERLERİ (YENİ YERİ: Burası 3. satır civarında olmalı)
if 'admin_mode' not in st.session_state:
    st.sessionion_state['admin_mode'] = False
if 'user_logged_in' not in st.session_state:
# ... (Diğer tüm st.session_state başlatma kodları buraya taşınacak) ...
if 'music_url' not in st.session_state:
    st.session_state['music_url'] = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"


# --- MODÜL VE KÜTÜPHANE İÇE AKTARMA --- (Bu kısım biraz aşağı kayacak)
try:
    from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
# ... (diğer importlar devam ediyor) ...
