import streamlit as st
from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
from english_content import konuyu_bul_eng, soru_cozumu_yap_eng
from math_content import konuyu_bul_math, soru_cozumu_yap_math 
import time

# --- SAYFA VE SİMGE AYARLARI ---
st.set_page_config(
    page_title="Eğitim Robotu | Yusuf Efe Şahin",
    layout="wide",
    page_icon="📚" 
)

# --- YÖNETİCİ GİRİŞİ AYARLARI VE OTURUM BAŞLATMA ---
ADMIN_PASSWORD = "123" 
# SIMÜLASYON KULLANICILARI
MOCK_USERS = [
    {"username": "ali", "email": "ali@okul.com", "password_hash": "a123"},
    {"username": "ayse", "email": "ayse@okul.com", "password_hash": "a456"},
]

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
    st.session_state['show_user_login'] = not st.session_state['show_user_login']
    st.session_state['show_admin_login'] = False
    st.session_state['show_user_register'] = False

def toggle_user_register_panel():
    st.session_state['show_user_register'] = not st.session_state['show_user_register']
    st.session_state['show_admin_login'] = False
    st.session_state['show_user_login'] = False

# --- ŞİFRE UNUTTUM SIMÜLASYONU ---
def forgot_password_simulation(email_or_username, is_admin=False):
    st.sidebar.warning("Sistemimiz simülasyon modunda olduğundan, şifreniz güvenlik nedeniyle mail adresinize gönderilecektir.")
    time.sleep(1)
    if is_admin:
        st.sidebar.success(f" Yönetici Şifresi sıfırlama maili '{email_or_username}' adresine gönderildi.")
    else:
        st.sidebar.success(f" Kullanıcı şifresi sıfırlama maili '{email_or_username}' adresine gönderildi.")


# Yönetici Modunda Tema Rengi Uygulama
if st.session_state['admin_mode']:
    st.markdown(f'<style>h1, h2, h3, h4, h5, h6 {{color: {st.session_state["app_color"]};}}</style>', unsafe_allow_html=True)
else:
    st.markdown(f'<style>h1, h2, h3, h4, h5, h6 {{color: #FFFFFF;}}</style>', unsafe_allow_html=True)


# --- ANA ROBOT GÖVDESİ ---
st.title("📚 Çok Dersli Eğitim Robotu")

# YÖNETİCİ PANELİ
if st.session_state['admin_mode']:
    st.header(f"⚙️ YÖNETİCİ PANELİ (Aktif)")
    
    # 1. Renk ve Temel Ayarlar
    st.subheader("🎨 Site Görünümü ve Temel Ayarlar")
    yeni_renk = st.color_picker('Uygulama Vurgu Rengini Seçin', st.session_state['app_color'])
    if yeni_renk != st.session_state['app_color']:
        st.session_state['app_color'] = yeni_renk
        st.rerun() 
    st.info(f"Uygulama Vurgu Rengi: {st.session_state['app_color']}")
    st.markdown("---")
    
    # 2. İçerik Güncelleme Simülasyonu
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

    # 3. Ana Sayfa Duyuru Yönetimi
    st.subheader("📢 Ana Sayfa Duyuru Yönetimi")
    yeni_duyuru = st.text_area("Öğrenci Ana Sayfasında Gösterilecek Duyuru Metni:", st.session_state['announcement'])
    if st.button("Duyuruyu Güncelle"):
        st.session_state['announcement'] = yeni_duyuru
        st.success("Duyuru başarıyla güncellendi! Anasayfada gösterilecektir.")
        st.rerun() 

    st.markdown("---")

    # 4. Kullanıcı Hesapları Yönetimi Simülasyonu
    st.subheader("👥 Kullanıcı Hesapları Yönetimi (Simülasyon)")
    
    st.info("Bu tabloda simüle edilmiş kullanıcıların listesi gösterilmektedir.")
    
    # Tablo ile kullanıcıları gösterme
    st.table([
        {"Kullanıcı Adı": u["username"], "E-posta": u["email"], "Son Giriş": f"2025/11/0{i+1}"}
        for i, u in enumerate(MOCK_USERS)
    ])
    
    # Yeni Kullanıcı Ekleme Simülasyonu
    st.caption("Yeni Kullanıcı Kaydı (Simülasyon)")
    with st.expander("Yeni Kullanıcı Ekle"):
        new_user = st.text_input("Yeni Kullanıcı Adı Demo")
        new_email = st.text_input("Yeni E-posta Demo")
        new_pass = st.text_input("Şifre Demo", type="password")
        if st.button("Kullanıcıyı Kaydet (Simülasyon)"):
            if new_user and new_email and new_pass:
                # Demo listeye ekleme simülasyonu
                MOCK_USERS.append({"username": new_user, "email": new_email, "password_hash": new_pass})
                st.success(f"Kullanıcı '{new_user}' simüle edilmiş listeye eklendi!")
                # NOT: Bu demo listesi uygulama yeniden başlatılınca sıfırlanır.
                st.rerun() 

    st.markdown("---")
    
    # 5. Geri Bildirim Yönetimi Simülasyonu
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
    st.warning(f"📣 DUYURU: {st.session_state['announcement']}") 
    st.subheader(f"✨ Merhaba! Ben sizin kişisel eğitim robotunuz.")
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
                # Şifremi Unuttum (Yönetici)
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
                     forgot_password_simulation(user_name or "Kayıtlı Mail Adresi", is_admin=False)
        st.sidebar.caption("Demo Hesaplar: ali/a123, ayse/a456")

    # ÜYE KAYIT BUTONU VE FORMU
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

st.sidebar.markdown("---") 

# --- DERS LİSTESİ ---
st.sidebar.title("Kullanılabilir Dersler")
st.sidebar.markdown(
    """
    * **🇹🇷 Türkçe:** Dil Bilgisi ve Anlam
    * **🇬🇧 İngilizce:** Tenses ve Kelime Bilgisi
    * **📐 Matematik:** Cebir ve Analiz (12. Sınıf Kapsamına kadar)
    """
)
st.sidebar.caption("Geliştirici: Yusuf Efe Şahin")


# SADECE ÖĞRENCİ MODUNDA İSE GÖSTER
if not st.session_state['admin_mode']:

    # --- MOD VE DERS SEÇİMİ ---
    secilen_ders = st.selectbox(
        "Lütfen ilgili dersi seçin:",
        ("Türkçe", "İngilizce", "Matematik")
    )
    
    islem_modu = st.radio(
        "Şimdi yapmak istediğiniz işlemi seçin:",
        ("Konu Anlatımı", "Soru Çözümü", "Kelime Bilgisi"),
        horizontal=True
    )
    
    konu_adi = st.text_input(f"Aradığınız Konu Adını veya Kelimeyi Giriniz:")

    if st.button("Başlat"):
        if konu_adi:
            
            konu_adi_lower = konu_adi.lower().strip()
            konu_icerigi = "Üzgünüm, aradığınız konuyu/kelimeyi bulamadım."
            
            # --- ANA MANTIK ---
            if islem_modu == "Kelime Bilgisi":
                if secilen_ders == "Türkçe":
                    konu_icerigi = konuyu_bul_eng(konu_adi_lower) 
                elif secilen_ders == "İngilizce":
                    konu_icerigi = konuyu_bul_tr(konu_adi_lower)
                else: 
                    konu_icerigi = "Matematik dersinde Kelime Bilgisi modu desteklenmemektedir."
            
            
            # --- KONU ANLATIMI VE SORU ÇÖZÜMÜ MANTIKLARI ---
            else:
                if secilen_ders == "Türkçe":
                    if islem_modu == "Soru Çözümü":
                         konu_icerigi = soru_cozumu_yap_tr(konu_adi_lower)
                    else: 
                        konu_icerigi = konuyu_bul_tr(konu_adi_lower)
                
                elif secilen_ders == "İngilizce":
                    if islem_modu == "Soru Çözümü":
                         konu_icerigi = soru_cozumu_yap_eng(konu_adi_lower)
                    else: 
                        konu_icerigi = konuyu_bul_eng(konu_adi_lower)
                
                elif secilen_ders == "Matematik":
                    if islem_modu == "Soru Çözümü":
                         konu_icerigi = soru_cozumu_yap_math(konu_adi_lower)
                    else: 
                        konu_icerigi = konuyu_bul_math(konu_adi_lower)

            
            # --- EVRENSEL BİLGİ YEDEĞİ (HER ŞEYİ CEVAPLAMA MANTIĞI) ---
            if "Üzgünüm" in konu_icerigi or "bulamadım" in konu_icerigi:
                 
                 evrensel_cevap = f"🤖 **ROBOT CEVAP YEDEĞİ:** Aradığınız **'{konu_adi.upper()}'** konusu, tanımlı ders içeriklerimizde bulunamamıştır. Ancak, robot olarak size genel bilgi verebilirim:\n\n"
                 
                 st.info("🤖 Robot Diyor ki: Lütfen cevabımı dikkatlice okuyun!")
                 
                 evrensel_cevap += "Dünyanın en derin okyanusu nedir? sorusunun cevabı Mariana Çukuru'nun bulunduğu Büyük Okyanus'tur. (Genel Bilgi Yedeği)"
                 
                 konu_icerigi = evrensel_cevap + "\n\n*Not: Bu yedek cevap, robotun her konuya cevap verme isteğiniz üzerine eklenmiştir.*"
            
            
            # Sonucu Ekrana Yazdırma
            if "desteklenmemektedir" not in konu_icerigi:
                if islem_modu == "Kelime Bilgisi":
                    st.success(f"İşte '{konu_adi.upper()}' için KELİME BİLGİSİ:")
                else:
                    st.success(f"İşte '{konu_adi.upper()}' için cevap/açıklama:")
                st.markdown(konu_icerigi)
            else:
                st.warning(konu_icerigi)

        else:
            st.error("Lütfen bir konu adı veya kelime giriniz.")
