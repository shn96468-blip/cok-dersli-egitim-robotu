 # ... (Üstteki kodlar)
if not st.session_state['admin_mode']: # <-- Bu satır sola yaslı olmalı

    # 2. KARŞILAMA VE DUYURU
    st.markdown("---")
    # ... (Diğer kodlar)

    # 3. DERS SEÇİMİ
    st.header("📚 Ders Seçimi")

    # DERSLERİN TANIMLARI
    col_din, col_fen, col_eng, col_mat = st.columns(4)
    # ...
    
    for ders in DERSLER: # <-- Bu satır da doğru girintide olmalı
        with ders["kolon"]:
# ...
