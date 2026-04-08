import streamlit as st
from streamlit_option_menu import option_menu

# 1. إعدادات الصفحة
st.set_page_config(page_title="دكان بلس", page_icon="🏪", layout="wide")

# 2. تحسين المظهر (CSS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stButton>button { border-radius: 15px; height: 3em; background-color: #2e8b57; color: white; border: none; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #f0f2f6; border-radius: 10px; padding: 10px; }
</style>
""", unsafe_allow_html=True)

# 3. إدارة حالة الدخول
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

st.markdown("<h1 style='text-align: center; color: #2e8b57;'>🏪 دكان بلس</h1>", unsafe_allow_html=True)

# 4. القائمة الرئيسية
choice = option_menu(None, ["دخول المشتري", "لوحة التاجر"], 
    icons=['cart', 'lock'], orientation="horizontal", 
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "18px"}, 
        "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#2e8b57"},
    })

if choice == "دخول المشتري":
    st.session_state.authenticated = False
    st.subheader("🔎 استكشف المنتجات المتاحة")
    st.text_input("عما تبحث؟ (خراف، ملابس، طيور...)", key="search_user")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander("🐮 قسم الحيوانات"):
            st.button("🐑 أغنام")
            st.button("🐄 مواشي")
    with col2:
        with st.expander("🦜 قسم الطيور"):
            st.button("🐣 طيور زينة")
            st.button("🍗 طيور ذبح")
    with col3:
        with st.expander("👕 قسم الملابس"):
            st.button("👔 رجالي")
            st.button("👗 حريمي")

else: # لوحة التاجر
    if not st.session_state.authenticated:
        st.info("🔐 منطقة محمية - يرجى إدخال كود الوصول")
        password = st.text_input("كود التاجر السري", type="password")
        if st.button("فتح النظام"):
            if password == "SILA2026":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ الكود غير صحيح")
    else:
        st.success("✅ أهلاً بك في لوحة تحكم دكان بلس")
        
        # توزيع المهام في تابات (Tabs)
        tab1, tab2, tab3 = st.tabs(["📓 دفتر الشكك", "🗺️ محرك الصيد", "⚙️ الإعدادات"])
        
        with tab1:
            st.subheader("إدارة الديون والمديونيات")
            # جدول تجريبي للديون
            debt_data = {
                "الاسم": ["أحمد فؤاد", "إبراهيم السيد", "سعيد محمد"],
                "المبلغ المتبقي": ["750 ج", "2100 ج", "300 ج"],
                "آخر حركة": ["2026-04-01", "2026-04-07", "2026-04-08"]
            }
            st.table(debt_data)
            if st.button("➕ إضافة مديونية جديدة"):
                st.write("سيتم فتح نموذج الإضافة قريباً...")

        with tab2:
            st.subheader("رصد تجار الجملة (الخرائط)")
            st.write("📍 جارٍ معالجة البيانات من الخرائط لتحديد أقرب الموردين.")
            
        with tab3:
            if st.button("تسجيل الخروج"):
                st.session_state.authenticated = False
                st.rerun()

st.markdown("---")
st.caption("إدارة دكان بلس 2026")
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
