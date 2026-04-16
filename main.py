import streamlit as st

st.set_page_config(page_title="دكان بلس - الرئيسية", page_icon="👑", layout="centered")

# تنسيق الأيقونات لتكون مثل الصورة
st.markdown("""
<style>
    .main { background-color: #f5f7f9; }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        cursor: pointer;
        transition: 0.3s;
    }
    .card:hover { transform: translateY(-5px); }
    .icon { font-size: 40px; }
    .title { font-weight: bold; color: #333; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: right;'>مرحباً بك في دكان بلس 👋</h2>", unsafe_allow_html=True)
st.write("---")

# توزيع الأيقونات في صفوف وأعمدة
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="icon">📓</div>
        <div class="title">دفتر الديون</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("افتح الدفتر", key="btn1"):
        st.info("انتقل الآن إلى 'دفتر الشكك' من القائمة الجانبية")

with col2:
    st.markdown("""
    <div class="card">
        <div class="icon">🍅</div>
        <div class="title">سوق الخضار</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("عرض الأسعار", key="btn2"):
        st.info("انتقل الآن إلى 'سوق الخضار' من القائمة الجانبية")

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="card">
        <div class="icon">🛡️</div>
        <div class="title">ركن المحارب</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("دخول الحصن", key="btn3"):
        st.info("انتقل الآن إلى 'ركن المحارب' من القائمة الجانبية")

with col4:
    st.markdown("""
    <div class="card">
        <div class="icon">🛒</div>
        <div class="title">المعرض العام</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("تصفح البضاعة", key="btn4"):
        st.info("انتقل الآن إلى 'المعرض' من القائمة الجانبية")
        
