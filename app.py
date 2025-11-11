for ders in DERSLER:
        with ders["kolon"]:
            if st.button(f"{ders['simgesi']} {ders['isim']}", key=f"btn_{ders['isim']}", use_container_width=True):
                st.session_state['secilen_ders'] = ders['isim'] # <-- BU SATIRIN EKSİKSİZ VE KAPALI OLMASI GEREKİYOR
                st.rerun()
