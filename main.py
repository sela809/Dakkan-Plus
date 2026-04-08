import streamlit as st
from streamlit_option_menu import option_menu

# إعدادات الصفحة
st.set_page_config(page_title="دكان بلس", page_icon="🏪", layout="wide")

# التصميم (CSS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stButton>button { border-radius: 20px; height: 3em; width: 100%; background-color: #2e8b57; color: white; border: none; }
</style>
""", unsafe_allow_html=True)

# نظام حفظ حالة الدخول
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.markdown("<h1 style='text-align: center; color: #2e8b57;'>🏪 دكان بلس</h1>", unsafe_allow_html=True)

# القائمة العلوية
identity = option_menu(None, ["دخول المشتري (المتفرج)", "لوحة تحكم التاجر"], 
    icons=['cart', 'shield-lock'], menu_icon="cast", default_index=0, orientation="horizontal")

if identity == "دخول المشتري (المتفرج)":
    st.session_state.logged_in = False # إعادة تعيين الدخول عند الخروج
    st.subheader("🔦 ماذا تبحث عنه اليوم؟")
    st.text_input("🔍 ابحث بالكتابة (خروف، فستان، بنزين...)", placeholder="اكتب هنا...")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander("🐮 الحيوانات"):
            st.button("🐑 خراف وعجول")
    with col2:
        with st.expander("🦜 الطيور"):
            st.button("🐣 طيور تربية")
    with col3:
        with st.expander("👕 الملابس"):
            st.button("👔 رجالي")

elif identity == "لوحة تحكم التاجر":
    if not st.session_state.logged_in:
        st.warning("🔐 هذه المنطقة محمية.")
        pwd = st.text_input("كود التاجر السري", type="password")
        if st.button("دخول الخزانة"):
            if pwd == "SILA2026":
                st.session_state.logged_in = True
                st.success("تم الدخول بنجاح!")
                st.rerun()
            else:
                st.error("❌ الكود غير صحيح!")
    else:
        # --- ما يظهر للتاجر بعد الدخول الصحيح ---
        st.success("مرحباً بك في لوحة التحكم الآمنة ✅")
        tab1, tab2 = st.tabs(["📓 دفتر الشكك", "🗺️ سحب بيانات الخرائط"])
        
        with tab1:
            st.subheader("📓 إدارة المديونيات")
            st.info("هنا ستظهر قائمة العملاء والديون قريباً...")
            # مثال بسيط لشكل البيانات
            st.table({"العميل": ["أحمد", "محمد"], "المبلغ": ["500 ج", "1200 ج"], "التاريخ": ["2026-04-01", "2026-04-05"]})
            
        with tab2:
            st.subheader("🗺️ محرك الصيد الذكي")
            st.write("سيتم ربط بيانات الخرائط هنا للبحث عن تجار الجملة.")

st.info("💡 نصيحة دكان بلس: دائماً ابحث عن التاجر ذو التقييم العالي لضمان المصداقية.")
