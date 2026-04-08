import streamlit as st
from streamlit_option_menu import option_menu

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="دكان بلس", page_icon="🏪", layout="wide")

# 2. تحسين المظهر (CSS) - تم التأكد من توافق الأكواد
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stButton>button { border-radius: 15px; height: 3em; background-color: #2e8b57; color: white; }
</style>
""", unsafe_allow_html=True)

# 3. إدارة تسجيل الدخول
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

st.markdown("<h1 style='text-align: center; color: #2e8b57;'>🏪 دكان بلس</h1>", unsafe_allow_html=True)

# 4. القائمة الرئيسية
choice = option_menu(None, ["دخول المشتري", "لوحة التاجر"], 
    icons=['cart', 'lock'], orientation="horizontal")

if choice == "دخول المشتري":
    st.session_state.authenticated = False # تسجيل خروج تلقائي عند التبديل
    st.subheader("🔎 استكشف المنتجات")
    st.text_input("عما تبحث؟ (مثلاً: خراف، ملابس، بنزين...)", key="search_bar")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander("🐮 الحيوانات"):
            st.write("🐑 خراف - 🐄 عجول")
    with col2:
        with st.expander("🦜 الطيور"):
            st.write("🐣 طيور زينة - 🍗 طيور أكل")
    with col3:
        with st.expander("👕 الملابس"):
            st.write("👔 رجالي - 👗 حريمي")

else: # لوحة التاجر
    if not st.session_state.authenticated:
        st.info("🔐 يرجى إدخال الكود السري للوصول لبياناتك")
        password = st.text_input("كود التاجر", type="password")
        if st.button("فتح الخزانة"):
            if password == "SILA2026":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ الكود غير صحيح")
    else:
        st.success("✅ أهلاً بك يا هندسة في لوحة تحكمك")
        tab1, tab2 = st.tabs(["📓 دفتر الشكك", "🗺️ محرك الصيد (الخرائط)"])
        
        with tab1:
            st.subheader("إدارة الديون")
            # عرض بيانات تجريبية للتأكد من العمل
            data = {"العميل": ["أحمد علي", "محمود حسن"], "المبلغ": ["500 ج", "1200 ج"], "الموعد": ["1-5", "10-5"]}
            st.table(data)
            
        with tab2:
            st.subheader("البحث في الخرائط")
            st.write("📍 جارٍ تجهيز الربط مع خرائط جوجل لجلب البيانات...")

st.markdown("---")
