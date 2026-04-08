import streamlit as st
from streamlit_option_menu import option_menu

# إعدادات الصفحة
st.set_page_config(page_title="دكان بلس", page_icon="🏪", layout="wide")

# تصميم الواجهة
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stButton>button { border-radius: 20px; height: 3em; width: 100%; background-color: #2e8b57; color: white; border: none; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #2e8b57;'>🏪 دكان بلس</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>المنصة الأقوى للتجارة والوساطة الذكية</p>", unsafe_allow_html=True)

# 1. بوابة الهوية
identity = option_menu(None, ["دخول المشتري (المتفرج)", "لوحة تحكم التاجر"], 
    icons=['cart', 'shield-lock'], menu_icon="cast", default_index=0, orientation="horizontal")

if identity == "دخول المشتري (المتفرج)":
    st.subheader("🔦 ماذا تبحث عنه اليوم؟")
    search_input = st.text_input("🔍 ابحث بالكتابة (خروف، فستان، بنزين...)", placeholder="اكتب هنا...")
    
    st.write("### 🎪 الأقسام الرئيسية")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.expander("🐮 الحيوانات ومستلزماتها"):
            st.button("🐑 خراف وعجول")
            st.button("🌾 أعلاف وحبوب")
            st.button("💊 أدوية بيطرية")
            
    with col2:
        with st.expander("🦜 الطيور"):
            st.button("🐣 طيور تربية")
            st.button("🦜 طيور زينة")
            st.button("🏗️ فقاسات ومعدات")
            
    with col3:
        with st.expander("👕 الملابس والأزياء"):
            st.button("👔 رجالي وشبابي")
            st.button("👗 حريمي وبناتي")
            st.button("👶 أطفال")
            st.button("👠 أحذية وشنط")

    st.divider()
    st.write("⛽ **خدمات أخرى:**")
    st.button("📍 أقرب محطة بنزين / غاز")

elif identity == "لوحة تحكم التاجر":
    st.warning("🔐 هذه المنطقة محمية. يرجى تسجيل الدخول للوصول إلى (دفتر الشكك) وسحب بيانات الخرائط.")
    st.text_input("كود التاجر السري", type="password")
    st.button("دخول الخزانة")

st.info("💡 نصيحة دكان بلس: دائماً ابحث عن التاجر ذو التقييم العالي لضمان المصداقية.")
