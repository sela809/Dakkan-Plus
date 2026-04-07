import streamlit as st
import pandas as pd

# --- إعدادات الأمان ---
def check_license():
    if "is_active" not in st.session_state:
        st.session_state.is_active = False
    if not st.session_state.is_active:
        st.title("🔐 تفعيل نسخة داكان بلس")
        st.info("مرحباً بك في نظام التاجر الذكي. يرجى التفعيل للبدء.")
        license_key = st.text_input("أدخل كود التفعيل الخاص بك:", type="password")
        if st.button("تفعيل الآن"):
            # الكود السري الخاص بك (يمكنك تغييره لاحقاً)
            if license_key == "SILA2026": 
                st.session_state.is_active = True
                st.success("تم التفعيل! جاري فتح النظام...")
                st.rerun()
            else:
                st.error("الكود غير صحيح. اطلبه عبر انستا باي.")
        return False
    return True

# --- تشغيل البرنامج بعد التفعيل ---
if check_license():
    st.sidebar.title("🏪 لوحة تحكم داكان بلس")
    st.sidebar.success("النسخة مفعلة ✅")
    
    menu = st.sidebar.radio("اختر القسم:", ["دفتر الديون", "سحب البيانات", "حول البرنامج"])
    
    if menu == "دفتر الديون":
        st.header("📑 إدارة ديون العملاء")
        st.write("سجل ديونك هنا وذكّر عملائك عبر واتساب.")
        # (سنقوم بتطوير الجدول هنا في الخطوة القادمة)
        
    elif menu == "سحب البيانات":
        st.header("🔍 صائد البيانات التسويقية")
        st.write("ابحث عن أرقام هواتف العملاء والمحلات في منطقتك.")

    elif menu == "حول البرنامج":
        st.write("برنامج داكان بلس - إصدار 2026")
        st.write("للدعم الفني والاشتراك، تواصل مع المطور.")
      
