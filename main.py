import streamlit as st
import pandas as pd
from datetime import datetime
import requests
import time

# --- إعدادات الواجهة والجماليات ---
st.set_page_config(page_title="منصة داكان بلس", page_icon="👑", layout="wide")

def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None
    return None

# --- نظام تسجيل الدخول المتطور ---
if "user_authenticated" not in st.session_state:
    st.session_state.user_authenticated = False
    st.session_state.username = ""

if not st.session_state.user_authenticated:
    # تم إصلاح الخطأ هنا في السطر التالي
    st.markdown("<h1 style='text-align: center; color: #2e8b57;'>👑 مرحباً بك في إمبراطورية داكان بلس</h1>", unsafe_allow_html=True)
    
    st.subheader("تسجيل الدخول للمنظومة")
    tab1, tab2, tab3 = st.tabs(["🔒 حساب خاص", "🌐 التواصل الاجتماعي", "📱 واتساب"])
    
    with tab1:
        u_name = st.text_input("اسم المستخدم أو الإيميل")
        u_pass = st.text_input("كلمة السر", type="password")
        if st.button("دخول"):
            if u_name and u_pass: 
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
    
    st.balloons()
    # تم إصلاح الخطأ هنا أيضاً
    st.markdown(f"""
    <div style="background-color: #e1f5fe; padding: 20px; border-radius: 15px; text-align: center; border: 2px solid #01579b;">
        <h2 style="color: #01579b;">أهلاً بك يا شريك النجاح في داكان بلس 👑</h2>
        <p style="font-size: 18px;">يسعدنا انضمامك لمنظومتنا. ابدأ الآن بإدارة تجارتك بذكاء "واليقين دائماً يكسب".</p>
    </div>
    """, unsafe_allow_html=True)
    
    # قائمة جانبية بسيطة لضمان التشغيل
    menu = st.sidebar.selectbox("قائمة التاجر", ["الرئيسية", "ملابس", "طيور أكل", "طيور زينة", "مواشي", "سيارات", "الديون"])

    if menu == "الديون":
        st.header("💸 تحصيل الديون الذكي")
        st.write(f"المستخدم الحالي: {st.session_state.username}")
        brand_footer = f"\n---\nبإشراف المهندس سيلا - داكان بلس 👑"
        st.text_area("معاينة توقيع الرسالة:", brand_footer)

    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.user_authenticated = False
        st.rerun()
        
