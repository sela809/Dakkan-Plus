import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
import time

# --- إعدادات الواجهة والجماليات ---
st.set_page_config(page_title="منصة داكان بلس", page_icon="👑", layout="wide")

def load_lottieurl(url):
    r = requests.get(url); return r.json() if r.status_code == 200 else None

# --- نظام تسجيل الدخول المتطور ---
if "user_authenticated" not in st.session_state:
    st.session_state.user_authenticated = False
    st.session_state.username = ""

if not st.session_state.user_authenticated:
    st.markdown("<h1 style='text-align: center; color: #2e8b57;'>👑 مرحباً بك في إمبراطورية داكان بلس</h1>", unsafe_allow_with_complete_page=True)
    st_lottie(load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_m6cuL6.json"), height=200)
    
    st.subheader("تسجيل الدخول للمنظومة")
    tab1, tab2, tab3 = st.tabs(["🔒 حساب خاص", "🌐 التواصل الاجتماعي", "📱 واتساب"])
    
    with tab1:
        u_name = st.text_input("اسم المستخدم أو الإيميل")
        u_pass = st.text_input("كلمة السر", type="password")
        if st.button("دخول"):
            if u_name and u_pass: # هنا ممكن تربطها بقاعدة بيانات لاحقاً
                st.session_state.user_authenticated = True
                st.session_state.username = u_name
                st.rerun()
                
    with tab2:
        col_fb, col_gg = st.columns(2)
        if col_fb.button("🔵 الدخول بواسطة Facebook"):
            st.info("جاري الربط مع Facebook API...")
        if col_gg.button("🔴 الدخول بواسطة Google"):
            st.info("جاري الربط مع Google Account...")
            
    with tab3:
        wa_num = st.text_input("أدخل رقم الواتساب المرتبط بحسابك")
        if st.button("إرسال كود التحقق (OTP)"):
            st.success(f"تم إرسال كود سري للرقم {wa_num} عبر الواتساب")

else:
    # --- بعد تسجيل الدخول: رسالة الترحيب ---
    st.sidebar.success(f"مرحباً، {st.session_state.username} 👋")
    
    # رسالة ترحيبية فخمة تظهر مرة واحدة
    st.balloons()
    st.markdown(f"""
    <div style="background-color: #e1f5fe; padding: 20px; border-radius: 15px; text-align: center; border: 2px solid #01579b;">
        <h2 style="color: #01579b;">أهلاً بك يا شريك النجاح في داكان بلس 👑</h2>
        <p style="font-size: 18px;">يسعدنا انضمامك لمنظومتنا. ابدأ الآن بإدارة تجارتك بذكاء "واليقين دائماً يكسب".</p>
    </div>
    """, unsafe_allow_with_complete_page=True)
    
    # --- المنيو الجانبي ---
    with st.sidebar:
        menu = option_menu("قائمة التاجر", 
            ["الرئيسية", "ملابس", "طيور أكل", "طيور زينة", "مواشي", "سيارات", "الديون"], 
            icons=['house', 'bag-check', 'egg', 'twitter', 'cow', 'car', 'cash'], 
            default_index=0)

    # هنا نضع محتوى الأقسام كما في الكود السابق...
    if menu == "الديون":
        st.header("💸 تحصيل الديون الذكي")
        st.write(f"المستخدم الحالي: {st.session_state.username}")
        # إضافة خاصية التوقيع في الرسائل
        brand_footer = f"\n---\nبإشراف المهندس سيلا - داكان بلس 👑"
        st.text_area("معاينة توقيع الرسالة:", brand_footer)

    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.user_authenticated = False
        st.rerun()
        
