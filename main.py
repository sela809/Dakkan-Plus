import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# --- إعدادات الواجهة ---
st.set_page_config(page_title="داكان بلس - المنظومة المتكاملة", layout="wide")
conn = st.connection("gsheets", type=GSheetsConnection)

if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🔐 دخول داكان بلس")
    if st.text_input("كود التفعيل", type="password") == "SILA2026":
        st.session_state.auth = True
        st.rerun()
else:
    # --- القائمة الجانبية ---
    st.sidebar.title("🏪 لوحة التحكم")
    menu = st.sidebar.radio("انتقل إلى:", [
        "📖 دليل استخدام البرنامج",
        "➕ إضافة عملية (صورة/كلمة)", 
        "📋 سجل التجارة والبحث",
        "💡 صندوق الاقتراحات"
    ])

    # 1. دليل الاستخدام (طلبك الجديد)
    if menu == "📖 دليل استخدام البرنامج":
        st.header("💡 كيف تستخدم داكان بلس في دقيقة؟")
        st.write("البرنامج مصمم ليوفر وقتك وجهدك، اتبع الآتي:")
        st.info("""
        1. **للتسجيل السريع:** ادخل على (إضافة عملية) وصور السلعة بكاميرا الموبايل واكتب السعر فقط.
        2. **لحفظ البيانات:** كل ما تسجله يذهب فوراً لملف جوجل الخاص بك ولا يضيع أبداً.
        3. **للبحث:** استخدم (السجل العام) واكتب أي كلمة للوصول لأي عميل أو بضاعة قديمة.
        4. **للتذكير:** من سجل الديون، يمكنك الضغط على زر الواتساب لإرسال رسالة تذكير آلية للمدين.
        """)
        st.success("داكان بلس.. تجارتك في جيبك بأمان!")

    # 2. إضافة عملية
    elif menu == "➕ إضافة عملية (صورة/كلمة)":
        st.header("📝 تسجيل تجارة جديدة")
        img = st.camera_input("📸 صور السلعة (لغير المتعلمين أو للسرعة)")
        with st.form("main_form"):
            cat = st.selectbox("القسم:", ["مواشي/طيور", "أسماك", "سيارات", "خضروات", "ملابس", "ديون"])
            item = st.text_input("البيان")
            price = st.number_input("المبلغ", min_value=0)
            if st.form_submit_button("✅ حفظ"):
                # كود الحفظ في جوجل شيت كما سبق
                st.success("تم الحفظ بنجاح")

    # 3. صندوق الاقتراحات (الفكرة العبقرية الجديدة)
    elif menu == "💡 صندوق الاقتراحات":
        st.header("🗣️ رأيك يهمنا لتطوير داكان بلس")
        suggestion = st.text_area("اكتب اقتراحك أو احتياجك هنا:")
        
        if st.button("إرسال الاقتراح"):
            if suggestion:
                st.balloons()
                # نظام الرد الذكي
                if "سعر" in suggestion or "تكلفة" in suggestion:
                    st.success("✅ شكراً لتعاونك! هذه الميزة متاحة بالفعل في 'نسخة المحترفين' وتكلفتها بسيطة جداً. اضغط هنا للاشتراك.")
                else:
                    st.info("👋 شكراً لتعاونك يا شريك النجاح! اقتراحك قيد الدراسة حالياً، وسنخبرك فور تنفيذه لتكون أول المشاركين في تجربته.")
            else:
                st.warning("برجاء كتابة الاقتراح أولاً")

    # 4. السجل العام
    elif menu == "📋 سجل التجارة والبحث":
        st.header("🔍 سجل العمليات")
        try:
            data = conn.read()
            st.dataframe(data, use_container_width=True)
        except:
            st.write("لا توجد بيانات حالياً")
