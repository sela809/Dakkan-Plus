import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="دكان بلس", page_icon="🏪", layout="wide")

# 2. تحسين المظهر (CSS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stButton>button { border-radius: 12px; width: 100%; background-color: #2e8b57; color: white; }
    .stDataFrame { direction: rtl; }
</style>
""", unsafe_allow_html=True)

# 3. إدارة البيانات (في ذاكرة المتصفح مؤقتاً)
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "clients_db" not in st.session_state:
    # قاعدة بيانات افتراضية للبدء
    st.session_state.clients_db = pd.DataFrame(columns=["الاسم", "المبلغ", "الحالة"])

st.markdown("<h1 style='text-align: center; color: #2e8b57;'>🏪 دكان بلس</h1>", unsafe_allow_html=True)

# 4. القائمة الرئيسية
choice = option_menu(None, ["دخول المشتري", "لوحة التاجر"], 
    icons=['cart', 'lock'], orientation="horizontal")

if choice == "دخول المشتري":
    st.session_state.authenticated = False
    st.subheader("🔎 استكشف الأقسام")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        with st.expander("🐮 الحيوانات"):
            st.write("🐑 أغنام - 🐄 مواشي")
    with col2:
        with st.expander("🦜 الطيور"):
            st.write("🐣 زينة - 🍗 أكل")
    with col3:
        with st.expander("👕 الملابس"):
            st.write("👔 رجالي - 👗 حريمي")
    with col4:
        with st.expander("🚗 السيارات"):
            st.write("🏎️ ملاكي - 🚛 نقل - 🏍️ موتوسيكلات")

else: # لوحة التاجر
    if not st.session_state.authenticated:
        st.info("🔐 منطقة محمية")
        password = st.text_input("كود التاجر", type="password")
        if st.button("فتح النظام"):
            if password == "SILA2026":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ الكود غير صحيح")
    else:
        st.success("✅ مرحباً بك في إدارة دكان بلس")
        t1, t2, t3 = st.tabs(["📓 دفتر الشكك", "➕ إدارة العملاء", "🗺️ الخرائط"])
        
        with t1:
            st.subheader("قائمة المديونيات الحالية")
            if not st.session_state.clients_db.empty:
                for index, row in st.session_state.clients_db.iterrows():
                    c1, c2, c3, c4 = st.columns([2, 1, 1, 1])
                    c1.write(f"👤 **{row['الاسم']}**")
                    c2.write(f"💰 {row['المبلغ']} ج")
                    status_color = "🟢" if row['الحالة'] == "تم السداد" else "🔴"
                    c3.write(f"{status_color} {row['الحالة']}")
                    
                    if row['الحالة'] == "مطلوب":
                        if c4.button("تأكيد السداد ✅", key=f"pay_{index}"):
                            st.session_state.clients_db.at[index, 'الحالة'] = "تم السداد"
                            st.rerun()
                    else:
                        if c4.button("إلغاء السداد ↩️", key=f"undo_{index}"):
                            st.session_state.clients_db.at[index, 'الحالة'] = "مطلوب"
                            st.rerun()
                st.divider()
            else:
                st.write("لا يوجد عملاء حالياً.")

        with t2:
            st.subheader("إضافة أو حذف عميل")
            new_name = st.text_input("اسم العميل الجديد")
            new_amount = st.text_input("المبلغ المستحق")
            if st.button("إضافة للدفتر ➕"):
                if new_name and new_amount:
                    new_entry = pd.DataFrame([{"الاسم": new_name, "المبلغ": new_amount, "الحالة": "مطلوب"}])
                    st.session_state.clients_db = pd.concat([st.session_state.clients_db, new_entry], ignore_index=True)
                    st.success(f"تمت إضافة {new_name}")
                    st.rerun()
            
            st.divider()
            st.write("🗑️ **حذف عميل نهائياً:**")
            del_index = st.number_input("أدخل رقم السطر للحذف", min_value=0, max_value=len(st.session_state.clients_db)-1, step=1)
            if st.button("حذف العميل نهائياً ❌"):
                st.session_state.clients_db = st.session_state.clients_db.drop(st.session_state.clients_db.index[del_index])
                st.rerun()

        with t3:
            st.write("📍 جارٍ العمل على محرك صيد الموردين...")

st.markdown("---")
st.caption("إدارة دكان بلس 2026")
