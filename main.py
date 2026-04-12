import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# 1. إعدادات الصفحة وإلغاء القائمة الجانبية تماماً
st.set_page_config(page_title="دكان بلس", page_icon="👑", layout="wide", initial_sidebar_state="collapsed")

# 2. تصميم الواجهة (CSS) لمنع التداخل وتحسين مظهر الجداول
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    [data-testid="stSidebar"] { display: none; }
    .stButton>button { border-radius: 12px; width: 100%; background-color: #2e8b57; color: white; border: none; height: 3.5em; }
    .stExpander { border-radius: 12px; border: 1px solid #2e8b57; }
    /* تنسيق البحث */
    .stTextInput input { text-align: right; direction: rtl; }
</style>
""", unsafe_allow_html=True)

# 3. إدارة البيانات
if "step" not in st.session_state:
    st.session_state.step = "register"
if "clients_db" not in st.session_state:
    # قاعدة بيانات تجريبية (الاسم، المبلغ، الموبايل)
    st.session_state.clients_db = pd.DataFrame(columns=["الاسم", "المبلغ", "الموبايل"])

st.markdown("<h1 style='text-align: center; color: #2e8b57;'>👑 دكان بلس</h1>", unsafe_allow_html=True)

# --- المرحلة الأولى: التسجيل ---
if st.session_state.step == "register":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.subheader("📝 دخول المنظومة")
        u_phone = st.text_input("رقم الواتساب للدخول", key="login_phone")
        u_type = st.radio("نوع الحساب", ["تاجر (لوحة تحكم)", "مشتري (تصفح)"], horizontal=True)
        if st.button("فتح الدكان 📲"):
            if u_phone:
                st.session_state.u_phone = u_phone
                st.session_state.u_type = u_type
                st.session_state.step = "home"
                st.rerun()

# --- المرحلة الثانية: التطبيق الرئيسي ---
elif st.session_state.step == "home":
    choice = option_menu(None, ["المعرض", "دفتر الشكك", "محرك الصيد"], 
        icons=['shop', 'journal-text', 'map'], orientation="horizontal")

    if choice == "المعرض":
        st.markdown("<h3 style='text-align: center;'>أقسام دكان بلس</h3>", unsafe_allow_html=True)
        with st.expander("🚗 قسم السيارات"):
            st.write("🏎️ ملاكي | 🚛 نقل | 🏍️ موتوسيكلات")
        with st.expander("🐮 قسم المواشي واللحوم"):
            st.write("🐑 أغنام | 🐄 عجول | 🌾 أعلاف")
        with st.expander("👕 قسم الملابس والأزياء"):
            st.write("👔 رجالي | 👗 حريمي | 👶 أطفال")

    elif choice == "دفتر الشكك":
        if st.session_state.u_type == "تاجر (لوحة تحكم)":
            tab1, tab2 = st.tabs(["📓 البحث وعرض الديون", "➕ إضافة عميل جديد"])
            
            with tab1:
                st.subheader("🔍 ابحث عن زبون")
                # خانة البحث الذكي
                search_query = st.text_input("اكتب اسم الزبون للوصول السريع...", placeholder="مثال: محمد، أحمد...")
                
                df = st.session_state.clients_db
                
                if not df.empty:
                    # عملية الفلترة بناءً على البحث
                    if search_query:
                        filtered_df = df[df['الاسم'].str.contains(search_query, na=False)]
                    else:
                        filtered_df = df
                    
                    if not filtered_df.empty:
                        st.write(f"تم العثور على ({len(filtered_df)}) سجل:")
                        st.dataframe(filtered_df, use_container_width=True)
                        
                        # زر الحذف السريع لآخر عملية بحث أو اختيار
                        if st.button("تصفية الحساب (حذف المختار) 🗑️"):
                            st.info("حدد السجل من الجدول لإدارته (ميزة قادمة)")
                    else:
                        st.warning("لا يوجد زبون بهذا الاسم.")
                else:
                    st.info("الدفتر فارغ تماماً.")

            with tab2:
                st.subheader("سجل مديونية جديدة")
                # استخدام autocomplete="off" لتقليل الحروف الإنجليزية
                n_name = st.text_input("اسم المشتري (بالعربي)")
                n_phone = st.text_input("رقم الموبايل")
                n_price = st.text_input("المبلغ المطلوب")
                
                if st.button("حفظ في الدفتر ➕"):
                    if n_name and n_price:
                        new_rec = pd.DataFrame([{"الاسم": n_name, "المبلغ": n_price, "الموبايل": n_phone}])
                        st.session_state.clients_db = pd.concat([st.session_state.clients_db, new_rec], ignore_index=True)
                        st.success(f"تم تسجيل {n_name} بنجاح")
                        st.rerun()

    # زر الخروج
    st.sidebar.write("---")
    if st.button("🔴 تسجيل خروج"):
        st.session_state.step = "register"
        st.rerun()

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>دكان بلس 2026 - تجارة ذكية بمصداقية عالية</p>", unsafe_allow_html=True)
                             
