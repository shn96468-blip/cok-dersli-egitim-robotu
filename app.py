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
if 'secilen_ders' not in st.session_state:
    st.session_state['secilen_ders'] = None
if 'show_kanka_chat' not in st.session_state:
    st.session_state['show_kanka_chat'] = False
if 'music_enabled' not in st.session_state:
    st.session_state['music_enabled'] = False
if 'music_url' not in st.session_state:
    st.session_state['music_url'] = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"


# --- MODÜL VE KÜTÜPHANE İÇE AKTARMA (Hata Kontrollü) ---
# Eksik dosyalar sorunu (history_content ve religion_content) devam ediyor.
# Bu blok, dosya eksik olsa bile uygulamanın açılmasını sağlayacak bir yedekleme içerir.

# Varsayılan (Yedek) Fonksiyonlar Tanımlanır
def yedek_konu(ders, konu): return f"İçerik modülü yüklenemediği için {ders} dersi '{konu}' konusu bulunamıyor."
def yedek_soru(ders, soru): return f"İçerik modülü yüklenemediği için {ders} dersi '{soru}' sorusu çözülemiyor."

# Fonksiyon Atamaları (Varsayılan olarak yedek fonksiyonlar atanır)
konuyu_bul_tr = lambda konu: yedek_konu("Türkçe", konu)
soru_cozumu_yap_tr = lambda soru: yedek_soru("Türkçe", soru)
konuyu_bul_eng = lambda konu: yedek_konu("İngilizce", konu)
soru_cozumu_yap_eng = lambda soru: yedek_soru("İngilizce", soru)
konuyu_bul_math = lambda konu: yedek_konu("Matematik", konu)
soru_cozumu_yap_math = lambda soru: yedek_soru("Matematik", soru)
konuyu_bul_history = lambda konu: yedek_konu("Tarih", konu)
soru_cozumu_yap_history = lambda soru: yedek_soru("Tarih", soru)
konuyu_bul_religion = lambda konu: yedek_konu("Din K.", konu)
soru_cozumu_yap_religion = lambda soru: yedek_soru("Din K.", soru)


# Başarılı İçe Aktarma Denemesi (Sadece varsa yükler)
try:
    from turkish_content import konuyu_bul_tr, soru_cozumu_yap_tr
except ImportError:
    st.info("🇹🇷 Türkçe İçerik Dosyası Bulunamadı. Simülasyon Devam Ediyor.")

try:
    from english_content import konuyu_bul_eng, soru_cozumu_yap_eng
except ImportError:
    st.info("🇬🇧 İngilizce İçerik Dosyası Bulunamadı. Simülasyon Devam Ediyor.")
    
try:
    from math_content import konuyu_bul_math, soru_cozumu_yap_math
except ImportError:
    st.info("📐 Matematik İçerik Dosyası Bulunamadı. Simülasyon Devam Ediyor.")
    
try:
    from history_content import konuyu_bul_history, soru_cozumu_yap_history
except ImportError:
    st.info("🏛️ Tarih İçerik Dosyası Bulunamadı. Simülasyon Devam Ediyor.")
    
try:
    from religion_content import konuyu_bul_religion, soru_cozumu_yap_religion
except ImportError:
    st.info("🕌 Din Kültürü İçerik Dosyası Bulunamadı. Simülasyon Devam Ediyor.")

# --- SAYFA VE SİMGE AYARLARI ---
st.set_page_config(
    page_title="Eğitim Robotu | Yusuf Efe Şahin",
    layout="wide",
    page_icon="📚"
)

# --- GİRİŞ/ÇIKIŞ FONKSİYONLARI (Kısaltıldı) ---
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
    clean_text = text.replace('"', '').replace('\n', ' ')
    js_code = f"""
    <script>
        var utterance = new SpeechSynthesisUtterance("{clean_text}");
        window.speechSynthesis.speak(utterance);
    </script>
    """
    st.markdown(js_code, unsafe_allow_html=True)


# --- SOHBET VE ÇEVİRİ MANTIKLARI (AYRILDI) ---
basit_sozluk = {
    "merhaba": "Hello", "selam": "Hi", "teşekkürler": "Thanks", "sağol": "Thanks",
    "elma": "Apple", "armut": "Pear", "kedi": "Cat", "köpek": "Dog",
    "apple": "Elma", "pear": "Armut", "cat": "Kedi", "dog": "Köpek",
    "again": "Tekrar / Yine",
    "teach": "Öğretmek", "study": "Çalışmak", "kitap": "Book", "kalem": "Pen"
}

def general_chat_kanka(kullanici_mesaji):
    mesaj_lower = kullanici_mesaji.lower().strip()

    # Kanka Sohbeti Mantığı
    if "merhaba" in mesaj_lower or "selam" in mesaj_lower or "kanka" in mesaj_lower:
        cevap = "Selam! Ben senin yapay zeka kankanım. Ders mi çalışalım yoksa güncel bir konudan mı konuşalım?"
    elif "nasılsın" in mesaj_lower:
        cevap = "Çok iyi çalışıyorum, teşekkür ederim! Peki sen nasılsın, dersler nasıl gidiyor?"
    elif "teşekkür" in mesaj_lower or "sağol" in mesaj_lower:
        cevap = "Rica ederim, ne zaman istersen buradayım!"
    elif "ders" in mesaj_lower or "çalışmak" in mesaj_lower or "ödev" in mesaj_lower:
        cevap = "Harika! Hangi dersle ilgili bir sorunun var? Veya hangi konudan başlayayım?"
    else:
        cevap = f"Anladım, '{kullanici_mesaji}' ilginç bir konu! Ama biliyorsun, benim uzmanlık alanım eğitim. Ders kartlarından birini seçerek ilerleyelim mi?"

    return cevap

def instant_translate(kelime_veya_cumle):
    mesaj_lower = kelime_veya_cumle.lower().strip()

    if mesaj_lower in basit_sozluk: # Türkçe'den İngilizce'ye
         return f"'{kelime_veya_cumle.title()}' kelimesinin İngilizce karşılığı: **{basit_sozluk[mesaj_lower]}**."
    elif mesaj_lower in [v.lower() for v in basit_sozluk.values()]: # İngilizce'den Türkçe'ye
        tr_karsilik = next(k for k, v in basit_sozluk.items() if v.lower() == mesaj_lower)
        return f"'{kelime_veya_cumle.title()}' kelimesinin Türkçe karşılığı: **{tr_karsilik}**."
    else:
        # Google Translate Simülasyonu
        return f"'{kelime_veya_cumle}' ifadesi için hazır çeviri bulamadım. Bu uzunluğu çevirmek için gerçek bir dil modeline ihtiyacım var. (Simülasyon)"

# --- TEMA RENGİ VE MÜZİK KONTROLÜ ---
if st.session_state['admin_mode']:
    st.markdown(f'<style>h1, h2, h3, h4, h5, h6 {{color: {st.session_state["app_color"]};}}</style>', unsafe_allow_html=True)
else:
    app_color_display = st.session_state.get('app_color', '#1E90FF')
    # Öğrenci modunda başlık rengini beyaz yapalım
    st.markdown(f'<style>h1, h2, h3, h4, h5, h6 {{color: #FFFFFF;}}</style>', unsafe_allow_html=True)

# --- MÜZİK ÇALMA MANTIĞI (Yönetici açarsa uygulama genelinde çalar) ---
if st.session_state['music_enabled']:
    st.markdown(f"""
        <audio autoplay loop>
          <source src="{st.session_state['music_url']}" type="audio/mp3">
          Tarayıcınız ses çalmayı desteklemiyor.
        </audio>
        """,
        unsafe_allow_html=True
    )
    # Öğrenci modunda çalma uyarısı
    if not st.session_state['admin_mode']:
        st.info("🎵 Sitemizin fon müziği çalıyor! (Sesi kısabilirsiniz)")
# --------------------------------------------------

# --- ANA ROBOT GÖVDESİ ---
st.title("📚 Çok Dersli Eğitim Robotu")

# SADECE ÖĞRENCİ MODUNDA İSE GÖSTER
if not st.session_state['admin_mode']:

    # 2. KARŞILAMA VE DUYURU
    st.markdown("---")
    if st.session_state['announcement_color'] == 'warning':
        st.warning(f"📣 DUYURU: {st.session_state['announcement']}")
    elif st.session_state['announcement_color'] == 'info':
        st.info(f"📣 DUYURU: {st.session_state['announcement']}")
    elif st.session_state['announcement_color'] == 'success':
        st.success(f"📣 DUYURU: {st.session_state['announcement']}")
    elif st.session_state['announcement_color'] == 'error':
        st.error(f"📣 DUYURU: {st.session_state['announcement']}")

    st.markdown(f"✨ Merhaba! Ben sizin <span style='color:{app_color_display}'>kişisel eğitim robotunuz</span>.", unsafe_allow_html=True)
    st.markdown("Aşağıdan dersinizi ve yapmak istediğiniz işlemi seçerek hemen bilgi almaya başlayın.")
    st.markdown("---")


    # 3. DERS SEÇİMİ (KARTLAR ŞEKLİNDE)
    st.header("📚 Ders Seçimi")

    # DERSLERİN TANIMLARI (Tüm 6 ders + Çeviri)
    # Kart görselindeki gibi 4'erli iki satır oluşturuyoruz.
    col_din, col_fen, col_eng, col_mat = st.columns(4)
    col_tarih, col_tr, col_cevir, col_bos = st.columns(4)

    DERSLER = [
        {"isim": "Din Kültürü", "simgesi": "🕌", "kolon": col_din},
        {"isim": "Fen Bilimleri", "simgesi": "🔬", "kolon": col_fen},
        {"isim": "İngilizce", "simgesi": "🇬🇧", "kolon": col_eng},
        {"isim": "Matematik", "simgesi": "📐", "kolon": col_mat},
        {"isim": "Tarih", "simgesi": "🏛️", "kolon": col_tarih},
        {"isim": "Türkçe", "simgesi": "🇹🇷", "kolon": col_tr},
        {"isim": "Anlık Çeviri", "simgesi": "🔄", "kolon": col_cevir},
    ]

    for ders in DERSLER:
        with ders["kolon"]:
            if st.button(f"{ders['simgesi']} {ders['isim']}", key=f"btn_{ders['isim']}", use_container_width=True):
                st.session_state['secilen_ders'] = ders['isim']
                st.rerun()

    st.markdown("---")

    secilen_ders = st.session_state['secilen_ders']

    if secilen_ders:
        st.subheader(f"✅ Seçili İşlem: {secilen_ders}")

        # ANLIK ÇEVİRİ MODU (Yeni Arayüz)
        if secilen_ders == "Anlık Çeviri":
            st.header("🔄 Anlık Kelime ve Kısa Cümle Çevirisi")
            st.info("Türkçe veya İngilizce bir kelime/kısa cümle girin, anında çevireyim.")

            cevirilecek_metin = st.text_input("Çevirilecek Kelime/Cümle:")
            if st.button("Çevir"):
                if cevirilecek_metin:
                    cevap = instant_translate(cevirilecek_metin)
                    st.success(cevap)
                else:
                    st.error("Lütfen çevrilecek bir kelime veya cümle giriniz.")


        # DERS İŞLEM MODU (Mevcut Yapı)
        else:
            islem_modu = st.radio(
                "Şimdi yapmak istediğiniz işlemi seçin:",
                ("Detaylı Konu Anlatımı", "Soru Çözümü", "Kelime Bilgisi"),
                horizontal=True
            )

            konu_adi = st.text_input(f"Aradığınız Konu Adını veya Kelimeyi Giriniz:")

            if st.button("Başlat"):
                if konu_adi:

                    konu_adi_lower = konu_adi.lower().strip()
                    konu_icerigi = "Üzgünüm, aradığınız konuyu/kelimeyi bulamadım."

                    # --- ANA MANTIK (YENİ DERSLER DAHİL) ---
                    if islem_modu == "Kelime Bilgisi":
                        if secilen_ders == "Türkçe":
                            konu_icerigi = konuyu_bul_eng(konu_adi_lower)
                        elif secilen_ders == "İngilizce":
                            konu_icerigi = konuyu_bul_tr(konu_adi_lower)
                        else:
                            st.warning("Bu mod sadece Türkçe ve İngilizce derslerinde desteklenmektedir.")
                            konu_icerigi = "Geçersiz Mod Seçimi."

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

                        elif secilen_ders == "Tarih":
                            if islem_modu == "Soru Çözümü":
                                konu_icerigi = soru_cozumu_yap_history(konu_adi_lower)
                            else:
                                konu_icerigi = konuyu_bul_history(konu_adi_lower)

                        elif secilen_ders == "Din Kültürü":
                            if islem_modu == "Soru Çözümü":
                                konu_icerigi = soru_cozumu_yap_religion(konu_adi_lower)
                            else:
                                konu_icerigi = konuyu_bul_religion(konu_adi_lower)

                        elif secilen_ders == "Fen Bilimleri":
                            # Fen Bilimleri içeriğini Türkçe modül ile simüle edelim
                            st.warning("Fen Bilimleri içeriği Türkçe modülü ile simüle edilmiştir.")
                            if islem_modu == "Soru Çözümü":
                                konu_icerigi = soru_cozumu_yap_tr(konu_adi_lower)
                            else:
                                konu_icerigi = konuyu_bul_tr(konu_adi_lower)

                    # --- EVRENSEL BİLGİ YEDEĞİ ve SONUÇ YAZDIRMA ---
                    if "Üzgünüm" in konu_icerigi or "bulamadım" in konu_icerigi or "İçerik modülü yüklenemediği" in konu_icerigi:

                         evrensel_cevap = f"🤖 **ROBOT CEVAP YEDEĞİ:** Aradığınız **'{konu_adi.upper()}'** konusu, tanımlı ders içeriklerimizde bulunamamıştır. Robot, yapay zeka desteğiyle bu konuda genel bilgi verme simülasyonu yapabilir:\n\n"
                         st.info("🤖 Robot Diyor ki: Bu bir simülasyon cevabıdır.")
                         evrensel_cevap += "Örneğin, 'Dünyanın en derin okyanusu nedir?' diye sorsaydınız, cevabım 'Büyük Okyanus' olurdu. (Genel Bilgi Yedeği)"
                         konu_icerigi = evrensel_cevap + "\n\n*Not: Robotun bilgi havuzunu genişletmek için yönetici panelinden yeni içerik eklenmeli veya içerik dosyaları doğru yerleştirilmelidir.*"


                    # Sonucu Ekrana Yazdırma
                    if "Geçersiz Mod Seçimi" not in konu_icerigi:
                        if islem_modu == "Kelime Bilgisi":
                            st.success(f"İşte '{konu_adi.upper()}' için KELİME BİLGİSİ:")
                        else:
                            st.success(f"İşte '{konu_adi.upper()}' için cevap/açıklama:")

                        # Konuşma Özelliği (Metin Okuma)
                        col_yazi, col_ses = st.columns([4, 1])
                        with col_yazi:
                            st.markdown(konu_icerigi)
                        with col_ses:
                            if st.button("🎤 Seslendir", key="seslendir_konu_anlatimi"):
                                metin_oku(konu_icerigi)

                    else:
                        st.warning(konu_icerigi)

                else:
                    st.error("Lütfen bir konu adı veya kelime giriniz.")

    # 4. KANKA CHATBOTU (Simülasyon - Floating Chat)
    kanka_toggle_js = f"""
    <div style='position: fixed; right: 20px; bottom: 20px; z-index: 9999;'>
        <button onclick
