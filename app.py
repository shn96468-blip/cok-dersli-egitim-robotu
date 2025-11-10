# app.py, 105. satır civarı:
def toggle_user_login_panel():
    # 106. satır:
    if st.session_state['user_login_allowed']: 
        # 107. satır (GEREKLİ GIRINTILI BLOK):
        st.session_state['show_user_login'] = not st.session_state['show_user_login']
        st.session_state['show_admin_login'] = False
        st.session_state['show_user_register'] = False
    else: # 111. satır
        st.sidebar.error("Üye girişi şu anda bakımdadır.")
