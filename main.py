import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import urllib.parse

# 1. إعدادات الصفحة وإلغاء القائمة الجانبية لتفادي تداخل الحروف
st.set_page_config(page_title="دكان بلس", page_icon="👑", layout="wide", initial_sidebar_state="collapsed")

# 2. تصميم الواجهة (CSS) لمنع تداخل الحروف وتنسيق المحتوى في المنتصف
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    
    /* إلغاء أي هوامش جانبية تسبب ظهور حروف عشوائية */
    [data-testid="stSidebar"] { display: none; }
    [data-testid="stHeader"] { display: none; }
    
    .stButton>button { border-radius: 12px; width: 100%; background-color: #2e8b57; color: white; border: none; height: 3.5em; font-size: 1.1em; }
    .stExpander { border-radius: 12px; border: 1px solid #2e8b57; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# 3. إدارة البيانات
if "step" not in st.session_state:
    st.session_state.step = "register"
if "clients_db" not in st.session_state:
    st.session_state.clients_db = pd.DataFrame(columns=["الاسم", "المبلغ", "الموبايل", "الحالة"])

# العنوان الرئيسي مع التاج
st.markdown("<h1 style='text-align: center; color: #2e8b57;'>👑 دكان بلس</h1>", unsafe_allow_html=True)

# --- المرحلة الأولى: التسجيل ---
if st.session_state.step == "register":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.subheader("📝 دخول المنظومة")
        u_phone = st.text_input("رقم الواتساب للدخول")
        u_type = st.radio("نوع الحساب", ["تاجر (لوحة تحكم)", "مشتري (تصفح)"], horizontal=True)
        
        if st.button("فتح الدكان 📲"):
            if u_phone:
                st.session_state.u_phone = u_phone
                st.session_state.u_type = u_type
                st.session_state.step = "home"
                st.rerun()
            else:
                st.error("أدخل رقم الهاتف أولاً")

# --- المرحلة الثانية: التطبيق الرئيسي ---
elif st.session_state.step == "home":
    # المنيو العلوي الاحترافي
    choice = option_menu(None, ["المعرض", "دفتر الشكك", "محرك الصيد"], 
        icons=['shop', 'journal-text', 'map'], orientation="horizontal")

    st.markdown("<br>", unsafe_allow_html=True)

    if choice == "المعرض":
        st.markdown("<h3 style='text-align: center;'>ماذا تتصفح اليوم في دكان بلس؟</h3>", unsafe_allow_html=True)
        
        # عرض الأقسام بشكل طولي مريح للموبايل
        with st.expander("🚗 قسم السيارات"):
            st.write("🏎️ ملاكي | 🚛 نقل | 🏍️ موتوسيكلات")
            st.button("تصفح المتاح في منطقتك", key="car_btn")
            
        with st.expander("🐮 قسم المواشي واللحوم"):
            st.write("🐑 أغنام | 🐄 عجول | 🌾 أعلاف")
            st.button("تصفح المزارع القريبة", key="cow_btn")
            
        with st.expander("🦜 قسم الطيور"):
            st.write("🐣 زينة | 🍗 أكل | 🏗️ معدات")
            st.button("تصفح سوق الطيور", key="bird_btn")
            
        with st.expander("👕 قسم الملابس والأزياء"):
            st.write("👔 رجالي | 👗 حريمي | 👶 أطفال")
            st.button("تصفح أحدث الموديلات", key="cloth_btn")

    elif choice == "دفتر الشكك":
        if st.session_state.u_type == "تاجر (لوحة تحكم)":
            tab1, tab2 = st.tabs(["📓 عرض المديونيات", "➕ إضافة عميل جديد"])
            
            with tab1:
                if not st.session_state.clients_db.empty:
                    st.dataframe(st.session_state.clients_db, use_container_width=True)
                else:
                    st.info("الدفتر فارغ حالياً.")
            
            with tab2:
                n_name = st.text_input("اسم العميل")
                n_phone = st.text_input("رقم الموبايل")
                n_price = st.text_input("المبلغ المطلوب")
                if st.button("حفظ في الدفتر ➕"):
                    new_rec = pd.DataFrame([{"الاسم": n_name, "المبلغ": n_price, "الموبايل": n_phone, "الحالة": "مطلوب"}])
                    st.session_state.clients_db = pd.concat([st.session_state.clients_db, new_rec], ignore_index=True)
                    st.success("تم التسجيل بنجاح")
                    st.rerun()
        else:
            st.warning("⚠️ هذا القسم مخصص للتجار فقط.")

    elif choice == "محرك الصيد":
        st.subheader("📍 رادار البحث الجغرافي")
        st.info("جارِ الربط مع الخرائط لرصد الموردين وتجار الجملة...")

    # زر الخروج في الأسفل بشكل شيك
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🔴 تسجيل خروج"):
        st.session_state.step = "register"
        st.rerun()

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>دكان بلس 2026 - تجارة ذكية بمصداقية عالية</p>", unsafe_allow_html=True)
