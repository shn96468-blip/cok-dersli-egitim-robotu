 for ders in DERSLER:
        # 4 boşluk girinti
        with ders["kolon"]: 
            # 8 boşluk girinti
            if st.button(f"{ders['simgesi']} {ders['isim']}", key=f"btn_{ders['isim']}", use_container_width=True):
                # 12 boşluk girinti
                st.session_state['secilen_ders'] = ders['isim']
                st.rerun()
