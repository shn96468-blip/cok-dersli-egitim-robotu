# app.py, 178. satır civarı:
    # 3. Genel Cevaplar (Eğitim)
    else: # <-- 184. satıra denk gelebilir
        cevap = f"Anladım, '{kullanici_mesaji}' hakkında bilgi istiyorsunuz. Lütfen yukarıdaki menüden dersinizi ve işlem modunu seçerek detaylı bilgi almayı deneyin."
        
    st.session_state.chat_history.append({"user": kullanici_mesaji, "robot": cevap})
    return cevap
