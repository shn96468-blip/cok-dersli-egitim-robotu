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
# Varsayılan (Yedek) Fonksiyonlar Tanımlanır
def yedek_konu(ders, konu): return f"İçerik modülü yüklenemediği için {ders} dersi '{konu}' konusu bulunamıyor. Lütfen ilgili ders dosyasını ekleyin."
def yedek_soru(ders, soru): return f"İçerik modülü yüklenemediği için {ders} dersi '{konu}' sorusu çözülemiyor. Lütfen ilgili ders dosyasını ekleyin."

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


# Başarılı İçe Aktarma Denemesi (Sadece varsa yükler, yoksa hata vermez)
# Tüm "try/except" bloklarının girintileri 0'a (sola) sıfırlanmıştır.
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

# 133. satır hatası (tırnak) ve girinti hataları burada DÜZELTİLMİŞTİR
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


# --- SOHBET VE ÇEVİRİ MANTIKLARI ---
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
    st.markdown(f'<style>h1, h2, h3, h4, h5, h6 {{color: #
