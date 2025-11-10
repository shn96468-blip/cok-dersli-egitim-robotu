# app.py dosyasında, Line 37 civarındaki Oturum Durumu Başlangıç Değerleri bölümü:

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
