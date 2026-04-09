import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="دكان بلس", page_icon="👑", layout="wide")

# 2. تصميم الواجهة (CSS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stButton>button { border-radius: 12px; width: 100%; background-color: #2e8b57; color: white; border: none; height: 3em; }
</style>
""", unsafe_allow_html=True)

# 3. إدارة البيانات وحالة الدخول
if "step" not in st.session_state:
    st.session_state.step = "register"
if "clients_db" not in st.session_state:
    st.session_state.clients_db = pd.DataFrame(columns=["الاسم", "المبلغ", "الموبايل", "الحالة", "التقييم"])

st.markdown("<h1 style='text-align: center; color: #2e8b57;'>👑 دكان بلس</h1>", unsafe_allow_html=True)

# --- المرحلة الأولى: التسجيل والتوثيق ---
if st.session_state.step == "register":
    st.subheader("📝 إنشاء حساب جديد موثق")
    u_name = st.text_input("الأسم الثلاثي لضمان الحقوق")
    u_phone = st.text_input("رقم الواتساب (مثال: 2010...)")
    u_type = st.radio("نوع الحساب", ["تاجر (لوحة تحكم)", "مشتري (تصفح)"])
    
    if st.button("تسجيل وتفعيل الحساب 📲"):
        if u_name and u_phone:
            st.session_state.u_name = u_name
            st.session_state.u_phone = u_phone
            st.session_state.u_type = u_type
            st.session_state.step = "home"
            st.success("تم التوثيق بنجاح")
            st.rerun()
        else:
            st.error("من فضلك أكمل البيانات")

# --- المرحلة الثانية: التطبيق الرئيسي ---
elif st.session_state.step == "home":
    choice = option_menu(None, ["المعرض", "دفتر الشكك", "محرك الصيد"], 
        icons=['shop', 'journal-text', 'map'], orientation="horizontal")

    if choice == "المعرض":
        st.subheader(f"مرحباً {st.session_state.u_name}، ماذا تتصفح اليوم؟")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            with st.expander("🚗 السيارات"):
                st.write("🏎️ ملاكي\n🚛 نقل\n🏍️ موتوسيكلات")
        with col2:
            with st.expander("🐮 المواشي"):
                st.write("🐑 أغنام\n🐄 عجول\n🌾 أعلاف")
        with col3:
            with st.expander("🦜 الطيور"):
                st.write("🐣 زينة\n🍗 أكل\n🏗️ معدات")
        with col4:
            with st.expander("👕 الملابس"):
                st.write("👔 رجالي\n👗 حريمي\n👶 أطفال")

    elif choice == "دفتر الشكك":
        if st.session_state.u_type == "تاجر (لوحة تحكم)":
            tab1, tab2 = st.tabs(["📓 عرض الديون", "➕ إضافة عميل"])
            
            with tab1:
                if not st.session_state.clients_db.empty:
                    st.table(st.session_state.clients_db)
                else:
                    st.write("الدفتر فارغ حالياً.")
            
            with tab2:
                n_name = st.text_input("اسم المشتري")
                n_phone = st.text_input("رقم واتساب المشتري")
                n_price = st.text_input("المبلغ")
                if st.button("تسجيل في الدفتر ➕"):
                    new_rec = pd.DataFrame([{"الاسم": n_name, "المبلغ": n_price, "الموبايل": n_phone, "الحالة": "مطلوب", "التقييم": "💎"}])
                    st.session_state.clients_db = pd.concat([st.session_state.clients_db, new_rec], ignore_index=True)
                    st.success("تم الحفظ")
                    st.rerun()
        else:
            st.warning("⚠️ هذه اللوحة مخصصة للتجار فقط.")

    elif choice == "محرك الصيد":
        st.subheader("📍 رادار المحلات والموردين")
        st.info("جارِ ربط محرك الخرائط لسحب بيانات الجوار...")

    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.step = "register"
        st.rerun()

st.markdown("---")
st.caption("بإشراف المهندس سيلا - دكان بلس 2026")
                    
