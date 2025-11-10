import streamlit as st
import time

# --- MODÜL VE KÜTÜPHANE İÇE AKTARMA ---
# Hata olasılığına karşı, modül içe aktarmaları try-except bloğuna alınmıştır.
try:
    from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
    from english_content import konuyu_bul_eng, soru_cozumu_yap_eng
    from math_content import konuyu_bul_math, soru_cozumu_yap_math 
except ImportError as e:
    st.error(f"Eğitim İçerik Dosyası Hatası: Lütfen 'turkish_content.py', 'english_content.py' ve 'math_content.py' dosyalarının 'app.py' ile aynı dizinde olduğundan emin olun. Hata: {e}")
    # Hata durumunda fonksiyonların boş tanımları
    def konuyu_bul_tr(konu): return f"İçerik modülü yüklenemediği için Türkçe '{konu}' konusu bulunamıyor."
    def soru_cozumu_yap_tr(soru): return f"İçerik modülü yüklenemediği için Türkçe '{soru}' sorusu çözülemiyor."
    def konuyu_bul_eng(konu): return f"İçerik modülü yüklenemediği için İngilizce '{konu}' konusu bulunamıyor."
    def soru_cozumu_yap_eng(soru): return f"İçerik modülü yüklenemediği için İngilizce '{soru}' sorusu çözülemiyor."
    def konuyu_bul_math(konu): return f"İçerik modülü yüklenemediği için Matematik '{konu}' konusu bulunamıyor."
    def soru_cozumu_yap_math(soru): return f"İçerik modülü yüklenemediği için Matematik '{soru}' sorusu çözülemiyor."


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
    
# --- GİRİŞ/ÇIKIŞ FONKSİYONLARI ---

def attempt_admin_login(password):
    if password == ADMIN_PASSWORD:
        st.session_state['admin_mode'] = True
        st.session_state['show_admin_login'] = False
        st.rerun() 
    else:
        st.error("Hatalı yönetici şifresi.")

def admin_logout():
    st.session_state['admin_mode'] = False
    st.rerun() 

def user_login(username, password):
    if not st.session_state['user_login_allowed']:
        st.error("Üye girişi şu anda bakımdadır. Lütfen daha sonra tekrar deneyin.")
        return
        
    for user in MOCK_USERS:
        if user["username"] == username and user["password_hash"] == password:
            st.session_state['user_logged_in'] = True
            st.session_state['current_user'] = username
            st.session_state['show_user_login'] = False
            st.success(f"Hoş geldiniz, {username.upper()}!")
            time.sleep(1)
            st.rerun() 
            return
    st.error("Kullanıcı adı veya şifre yanlış.")

def user_logout():
    st.session_state['user_logged_in'] = False
    st.session_state['current_user'] = None
    st.rerun()

# --- MOD AÇMA/KAPAMA FONKSİYONLARI ---

def toggle_admin_login_panel():
    st.session_state['show_admin_login'] = not st.session_state['show_admin_login']
    st.session_state['show_user_login'] = False
    st.session_state['show_user_register'] = False

def toggle_user_login_panel():
    if st.session_state['user_login_allowed']:
        st.session_state['show_user_login'] = not st.session_state['show_user_login']
        st.session_state['show_admin_login'] = False
        st.session_state['show_user_register'] = False
    else:
        st.sidebar.error("Üye girişi şu anda bakımdadır.")

def toggle_user_register_panel():
    if st.session_state['registration_allowed']:
        st.session_state['show_user_register'] = not st.session_state['show_user_register']
        st.session_state['show_admin_login'] = False
        st.session_state['show_user_login'] = False
    else:
        st.sidebar.error("Yeni kayıtlar şu anda kapalıdır.")


# --- ŞİFRE UNUTTUM SIMÜLASYONU ---
def forgot_password_simulation(email_or_username, is_admin=False):
    st.sidebar.warning("Sistemimiz simülasyon modunda olduğundan, şifre sıfırlama linki kayıtlı e-posta adresinize gönderilmiştir.")
    time.sleep(1)
    if is_admin:
        st.sidebar.success(f" Yönetici Şifresi sıfırlama maili 'admin@robot.com' adresine gönderildi.")
    else:
        user_email = "kayıtlı_eposta_adresi"
        for user in MOCK_USERS:
            if user["username"] == email_or_username:
                user_email = user["email"]
                break
        
        st.sidebar.success(f" Kullanıcı şifresi sıfırlama linki '{user_email}' adresine gönderildi.")

# --- METİN OKUMA FONKSİYONU ---
def metin_oku(text):
    """Verilen metni tarayıcının yerleşik Text-to-Speech motoru ile seslendirir."""
    clean_text = text.replace('"', '').replace('\n', ' ')
    js_code = f"""
    <script>
        var utterance = new SpeechSynthesisUtterance("{clean_text}");
        window.speechSynthesis.speak(utterance);
    </script>
    """
    st.markdown(js_code, unsafe_allow_html=True)

# --- SOHBET VE ÇEVİRİ MANTIKLARI ---
def sohbet_ve_cevir(kullanici_mesaji):
    mesaj_lower = kullanici_mesaji.lower().strip()
    
    # 1. Hazır Cevaplar (Sohbet)
    if "merhaba" in mesaj_lower or "selam" in mesaj_lower:
        cevap = "Merhaba! Ben yapay zeka destekli eğitim robotuyum. Nasıl yardımcı olabilirim?"
    elif "adın ne" in mesaj_lower or "kimsin" in mesaj_lower:
        cevap = "Ben Yusuf Efe Şahin tarafından geliştirilen Çok Dersli Eğitim Robotuyum."
    elif "teşekkür" in mesaj_lower or "sağol" in mesaj_lower:
        cevap = "Rica ederim, her zaman buradayım!"
        
    # 2. Basit Çeviri Simülasyonu
    elif "çevir" in mesaj_lower or "translate" in mesaj_lower:
        # Basit bir anahtar kelime tabanlı çeviri simülasyonu
        if "elma" in mesaj_lower:
            cevap = "Kelime: Elma. İngilizce Çevirisi: Apple."
        elif "apple" in mesaj_lower:
            cevap = "Kelime: Apple. Türkçe Çevirisi: Elma."
        elif "again" in mesaj_lower:
            cevap = "Kelime: Again. Türkçe Çevirisi: Tekrar/Yine."
        else:
            cevap = f"'{kullanici_mesaji}' ifadesi için çeviri simülasyonu yapıldı. Gerçek bir dil modeli ile anlık çeviri yapabilirim."
            
    # 3. Genel Cevaplar (Eğitim)
    else:
        cevap = f"Anladım, '{kullanici_mesaji}' hakkında bilgi istiyorsunuz. Lütfen yukarıdaki menüden dersinizi ve işlem modunu seçerek detaylı bilgi almayı deneyin."
        
    st.session_state.chat_history.append({"user": kullanici_mesaji, "robot": cevap})
    return cevap
    
    
# Yönetici Modunda Tema Rengi Uygulama
if st.session_state['admin_mode']:
    st.markdown(f'<style>h1, h2, h3, h4, h5, h6 {{color: {st.session_state["app_color"]};}}</style>', unsafe_allow_html=True)
else:
    # Bu kısmı düzelttik. Admin modu kapalıyken bile başlığın rengi uygulansın.
    st.markdown(f'<style>h1, h2, h3, h4, h5, h6 {{color: #FFFFFF;}}</style>', unsafe_allow_html=True)


# --- ANA ROBOT GÖVDESİ ---
st.title("📚 Çok Dersli Eğitim Robotu")

# YÖNETİCİ PANELİ
if st.session_state['admin_mode']:
    st.header(f"⚙️ YÖNETİCİ PANELİ (Aktif)")
    
    # 1. Renk ve Temel Ayarlar
    st.subheader("🎨 Site Görünümü ve Temel Ayarlar")
    col_app_color, col_duyuru_color = st.columns(2)
    with col_app_color:
        yeni_renk = st.color_picker('Uygulama Vurgu Rengini Seçin', st.session_state['app_color'])
        if yeni_renk != st.session_state['app_color']:
            st.session_state['app_color'] = yeni_renk
            st.rerun() 
        st.info(f"Uygulama Vurgu Rengi: {st.session_state['app_color']}")
    
    with col_duyuru_color:
        yeni_duyuru_color = st.selectbox(
            'Duyuru Vurgu Rengini Seçin:', 
            ('warning', 'info', 'success', 'error'), 
            index=('warning', 'info', 'success', 'error').index(st.session_state['announcement_color'])
        )
        if yeni_duyuru_color != st.session_state['announcement_color']:
            st.session_state['announcement_color'] = yeni_duyuru_color
            st.rerun() 
        st.info(f"Duyuru Rengi: {st.session_state['announcement_color']}")
        

    st.markdown("---")
    
    # 2. Üye Girişi / Kaydı Kontrolü
    st.subheader("🔒 Kullanıcı Erişim Kontrolü")
    
    col_login, col_reg = st.columns(2)
    with col_login:
        yeni_login_izin = st.checkbox("Üye Girişine İzin Ver", st.session_state['user_login_allowed'])
        if yeni_login_izin != st.session_state['user_login_allowed']:
            st.session_state['user_login_allowed'] = yeni_login_izin
            st.rerun()
            
    with col_reg:
        yeni_reg_izin = st.checkbox("Yeni Kayda İzin Ver", st.session_state['registration_allowed'])
        if yeni_reg_izin != st.session_state['registration_allowed']:
            st.session_state['registration_allowed'] = yeni_reg_izin
            st.rerun()
            
    st.caption("Bakım veya yoğunluk durumunda girişleri kapatabilirsiniz.")
    st.markdown("---")

    # 3. İçerik Güncelleme Simülasyonu
    st.subheader("✍️ İçerik Güncelleme (Simülasyon)")
    secilen_ders_admin = st.selectbox("İçerik Eklenecek Ders:", ("Türkçe", "İngilizce", "Matematik"), key="admin_select_ders")
    konu_basligi = st.text_input("Yeni Konu Başlığı:", key="admin_input_baslik")
    konu_detay = st.text_area("Konu Açıklaması (Detaylı):", key="admin_input_detay")
    if st.button("İçeriği Ekle", key="admin_button_ekle"):
        if konu_basligi and konu_detay:
            st.success(f"'{secilen_ders_admin}' dersine '{konu_basligi}' başlıklı yeni içerik başarıyla EKLEME SİMULASYONU yapıldı!")
        else:
            st.warning("Lütfen başlık ve detay alanlarını doldurun.")

    st.markdown("---")

    # 4. Ana Sayfa Duyuru Yönetimi
    st.subheader("📢 Ana Sayfa Duyuru Yönetimi")
    yeni_duyuru = st.text_area("Öğrenci Ana Sayfasında Gösterilecek Duyuru Metni:", st.session_state['announcement'])
    if st.button("Duyuruyu Güncelle"):
        st.session_state['announcement'] = yeni_duyuru
        st.success("Duyuru başarıyla güncellendi! Anasayfada gösterilecektir.")
        st.rerun() 

    st.markdown("---")

    # 5. Kullanıcı Hesapları Yönetimi Simülasyonu
    st.subheader("👥 Kullanıcı Hesapları Yönetimi (Simülasyon)")
    
    st.info("Bu tabloda simüle edilmiş kullanıcıların listesi gösterilmektedir.")
    
    st.table([
        {"Kullanıcı Adı": u["username"], "E-posta": u["email"], "Son Giriş": f"2025/11/0{i+1}"}
        for i, u in enumerate(MOCK_USERS)
    ])
    
    st.caption("Yeni Kullanıcı Kaydı (Simülasyon)")
    with st.expander("Yeni Kullanıcı Ekle"):
        new_user = st.text_input("Yeni Kullanıcı Adı Demo")
        new_email = st.text_input("Yeni E-posta Demo")
        new_pass = st.text_input("Şifre Demo", type="password")
        if st.button("Kullanıcıyı Kaydet (Simülasyon)"):
            if new_user and new_email and new_pass:
                st.success(f"Kullanıcı '{new_user}' simüle edilmiş listeye eklendi!")
                st.rerun() 

    st.markdown("---")
    
    # 6. Geri Bildirim Yönetimi Simülasyonu
    st.subheader("💬 Geri Bildirim Yönetimi (Simülasyon)")
    if st.button("Yeni Geri Bildirimleri Kontrol Et"):
        st.markdown("### Son Geri Bildirimler:") 
        st.markdown(f"**🟢 2025/11/09 (Türkçe Dersinden):** 'Çözüldü' olarak işaretlendi. *Kelime Bilgisi modunda Türkçe kelime aradım, cevap İngilizce geldi.*")
        st.markdown(f"**🟡 2025/11/10 (Matematik Dersinden):** 'Beklemede'. *Türev konusunda daha fazla örnek istiyorum.*")
        st.markdown(f"**🔴 2025/11/10 (Genel Uygulama):** 'Yeni Hata'. *Uygulama açılırken kırmızı hata alıyorum.* (Çözüm: Dosyaları kontrol edin!)")


else:
    # Öğrenci Modu Karşılama
    st.markdown("---")
    # DUYURU ALANI
    if st.session_state['announcement_color'] == 'warning':
        st.warning(f"📣 DUYURU: {st.session_state['announcement']}")
    elif st.session_state['announcement_color'] == 'info':
        st.info(f"📣 DUYURU: {st.session_state['announcement']}")
    elif st.session_state['announcement_color'] == 'success':
        st.success(f"📣 DUYURU: {st.session_state['announcement']}")
    elif st.session_state['announcement_color'] == 'error':
        st.error(f"📣 DUYURU: {st.session_state['announcement']}")

    # Renk ayarı admin modunda yapılmazsa buraya bir yedek ekleyelim
    app_color_display = st.session_state.get('app_color', '#1E90FF') 
    st.markdown(f"✨ Merhaba! Ben sizin <span style='color:{app_color_display}'>kişisel eğitim robotunuz</span>.", unsafe_allow_html=True)
    st.markdown("Aşağıdan dersinizi ve yapmak istediğiniz işlemi seçerek hemen bilgi almaya başlayın.")
    st.markdown("---")


# --- YÖNETİCİ/ÜYE GİRİŞİ (SIDEBAR) ---
st.sidebar.title("Kullanıcı İşlemleri")

# Yönetici Girişi
if st.session_state['admin_mode']:
    st.sidebar.button("🔒 YÖNETİCİ ÇIKIŞI", on_click=admin_logout)
else:
    st.sidebar.button("🔒 Yönetici Girişi", on_click=toggle_admin_login_panel)
    
    # YÖNETİCİ GİRİŞ FORMU
    if st.session_state['show_admin_login']:
        with st.sidebar.form("admin_login_form"):
            admin_pass = st.text_input("Yönetici Şifresi", type="password", key="admin_pass_input")
            col1, col2 = st.columns(2)
            with col1:
                st.form_submit_button("Giriş Yap", on_click=attempt_admin_login, args=(admin_pass,))
            with col2:
                if st.form_submit_button("Şifremi Unuttum"):
                    forgot_password_simulation("Yönetici Mail Adresi", is_admin=True)

# Üye Girişi ve Kayıt Simülasyonu
if st.session_state['user_logged_in']:
    st.sidebar.success(f"Giriş Yapıldı: {st.session_state['current_user'].upper()}")
    st.sidebar.button("🚪 Üye Çıkışı", on_click=user_logout) 
else:
    # ÜYE GİRİŞİ BUTONU VE FORMU
    st.sidebar.button("👤 Üye Girişi", on_click=toggle_user_login_panel)
    if st.session_state['show_user_login']:
        with st.sidebar.form("user_login_form"):
            user_name = st.text_input("Kullanıcı Adı")
            user_pass = st.text_input("Şifre", type="password")
            col1, col2 = st.columns(2)
            with col1:
                st.form_submit_button("Giriş Yap", on_click=user_login, args=(user_name, user_pass))
            with col2:
                if st.form_submit_button("Şifremi Unuttum"):
                     forgot_password_simulation(user_name or "Bilinmiyor", is_admin=False)
        st.sidebar.caption("Demo Hesaplar: ali/a123, ayse/a456")

    # ÜYE KAYIT BUTONU VE FORMU
    if st.session_state['registration_allowed']:
        st.sidebar.button("📝 Kaydol", on_click=toggle_user_register_panel)
        if st.session_state['show_user_register']:
            with st.sidebar.form("user_register_form"):
                reg_user = st.text_input("Kullanıcı Adı (Kaydol)")
                reg_email = st.text_input("E-posta Adresi")
                reg_pass = st.text_input("Şifre Belirle", type="password")
                if st.form_submit_button("Hesap Oluştur (Simülasyon)"):
                    st.info(f"Kayıt işlemi başarıyla simüle edildi! Lütfen giriş yapın.")
                    st.session_state['show_user_register'] = False
                    st.rerun()
    else:
        st.sidebar.error("Yeni kayıtlar şu anda kapalıdır.")

st.sidebar.markdown("---") 

# --- DERS LİSTESİ ---
st.sidebar.title("Kullanılabilir Dersler")
st.sidebar.markdown(
    """
    * **🇹🇷 Türkçe:** Dil Bilgisi ve Anlam
    * **🇬🇧 İngilizce:** Tenses ve Kelime Bilgisi
    * **📐 Matematik:** Cebir ve Analiz (12. Sınıf Kapsamına kadar)
    * **💬 Sohbet:** Anlık Çeviri ve Etkileşim
    """
)
st.sidebar.caption("Geliştirici: Yusuf Efe Şahin")


# SADECE ÖĞRENCİ MODUNDA İSE GÖSTER
if not st.session_state['admin_mode']:

    # --- MOD VE DERS SEÇİMİ ---
    secilen_ders = st.selectbox(
        "Lütfen ilgili dersi seçin:",
        ("Türkçe", "İngilizce", "Matematik", "Sohbet ve Anlık Çeviri")
    )
    
    # Sohbet modu seçilirse farklı bir arayüz göster
    if secilen_ders == "Sohbet ve Anlık Çeviri":
        st.header("💬 Robot ile Sohbet ve Anlık Çeviri")
        st.info("Bana herhangi bir soru sorabilir ya da çevirmek istediğin bir kelime/cümle yazabilirsin.")
        
        # Sohbet Geçmişi Gösterimi
        for chat in st.session_state.chat_history:
            with st.chat_message("user"):
                st.markdown(chat["user"])
            with st.chat_message("robot"):
                # Konuşma Özelliği (Metin Okuma)
                col_yazi_chat, col_ses_chat = st.columns([4, 1])
                with col_yazi_chat:
                    st.markdown(chat["robot"])
                with col_ses_chat:
                    # Buton anahtarı (key) oluşturulurken hata olasılığına karşı güvenlik eklendi
                    if st.button("🎤 Seslendir", key
