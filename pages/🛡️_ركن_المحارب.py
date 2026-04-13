import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="ركن المحارب الأنيق", page_icon="🛡️")

# تصميم فخم (ذهبي وأسود) ليناسب شموخ المحارب
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .main { background-color: #0e1117; }
    .stHeader { background-color: rgba(0,0,0,0); }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; } /* لون ذهبي */
    .p-text { color: #e0e0e0; text-align: center; font-size: 1.2em; }
    .stButton>button { background: linear-gradient(45deg, #d4af37, #b8860b); color: black; font-weight: bold; border-radius: 10px; border: none; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🛡️ ركن المحارب الأنيق</h1>", unsafe_allow_html=True)
st.markdown("<p class='p-text'>مساحة للهدوء، الثبات، وإعادة ترتيب الأوراق</p>", unsafe_allow_html=True)
st.write("---")

# ١. نافذة الثبات (تفاعلية)
st.subheader("بوصلة الحالة")
mood = st.select_slider(
    "كيف تجد معدنك اليوم وسط التحديات؟",
    options=["عاصفة", "ثبات مهتز", "صمت القوة", "يقين تام"]
)

if mood == "عاصفة":
    st.info("💡 تذكر: المعدن الأصيل لا يتغير مهما كانت التحديات. العاصفة تختبر القوة ولا تكسرها.")
elif mood == "صمت القوة":
    st.success("✨ الصمت هو درعك الأنيق. قل دائماً أقل مما هو ضروري لتحتفظ بوقارك.")
elif mood == "يقين تام":
    st.balloons()
    st.markdown("<h3 style='color: #4caf50 !important;'>اليقين دائماً يكسب</h3>", unsafe_allow_html=True)

st.write("---")

# ٢. تمرين المحارب (تحويل الطاقة لإنجاز)
st.subheader("🔧 مختبر التحويل")
st.write("حوّل تركيزك الآن من التفكير في الخارج إلى بناء الداخل. جرب حل هذا اللغز البرمجي الصغير:")

problem = st.code("X = 10 \n Y = 20 \n Result = X + Y", language="python")
user_ans = st.number_input("ما هي قيمة Result؟", min_value=0)

if st.button("تأكيد الإنجاز"):
    if user_ans == 30:
        st.success("إنجاز رائع! لقد نجحت في تحويل تركيزك لعملية بناء. استمر.")
    else:
        st.warning("حاول مرة أخرى، الدقة هي صفة المحارب.")

st.write("---")
st.caption("دكان بلس 2026 - ركن خاص للمعدن الأصيل")
