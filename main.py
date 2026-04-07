import streamlit as st
import pandas as pd
from datetime import datetime

# --- إعدادات الصفحة ---
st.set_page_config(page_title="داكان بلس", page_icon="🏪", layout="wide")

# --- التحقق من الكود السري ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔐 تفعيل نسخة داكان بلس")
    pwd = st.text_input("أدخل كود التفعيل:", type="password")
    if st.button("تفعيل الآن"):
        if pwd == "SILA2026":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("الكود غير صحيح!")
else:
    # --- إنشاء مخزن للبيانات (في الذاكرة حالياً) ---
    if "data" not in st.session_state:
        st.session_state.data = pd.DataFrame(columns=["العميل", "المبلغ", "التاريخ", "ملاحظات"])

    # --- القائمة الجانبية ---
    st.sidebar.header("🏪 لوحة التحكم")
    choice = st.sidebar.selectbox("اختر القسم:", ["📋 دفتر الديون", "📈 الإحصائيات", "💬 مراسلة العملاء"])

    if choice == "📋 دفتر الديون":
        st.header("📝 تسجيل مديونية جديدة")
        
        with st.form("debt_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("اسم العميل")
                amount = st.number_input("المبلغ (جنيه)", min_value=0)
            with col2:
                date = st.date_input("تاريخ الدين", datetime.now())
                note = st.text_area("ملاحظات")
            
            submit = st.form_submit_button("حفظ في الدفتر")
            
            if submit and name and amount > 0:
                new_row = {"العميل": name, "المبلغ": amount, "التاريخ": date.strftime("%Y-%m-%d"), "ملاحظات": note}
                st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_row])], ignore_index=True)
                st.success(f"تم تسجيل {amount} جنيه على {name}")

        st.divider()
        st.subheader("📜 سجل الديون الحالي")
        st.dataframe(st.session_state.data, use_container_width=True)

    elif choice == "📈 الإحصائيات":
        st.header("📊 ملخص الحسابات")
        if not st.session_state.data.empty:
            total_money = st.session_state.data["المبلغ"].sum()
            total_clients = st.session_state.data["العميل"].nunique()
            
            c1, c2 = st.columns(2)
            c1.metric("إجمالي الفلوس بره", f"{total_money} ج.م")
            c2.metric("عدد العملاء المديونين", total_clients)
            
            st.bar_chart(st.session_state.data.set_index("العميل")["المبلغ"])
        else:
            st.info("لا توجد بيانات لعرض إحصائياتها.")

    elif choice == "💬 مراسلة العملاء":
        st.header("📲 تذكير العملاء عبر واتساب")
        if not st.session_state.data.empty:
            target_client = st.selectbox("اختر العميل:", st.session_state.data["العميل"].unique())
            client_total = st.session_state.data[st.session_state.data["العميل"] == target_client]["المبلغ"].sum()
            
            message = f"يا أستاذ {target_client}، بنفكرك إن متبقي عليك مبلغ {client_total} جنيه لمحل داكان بلس. تسلم مقدماً!"
            st.text_area("نص الرسالة:", message)
            
            wa_url = f"https://wa.me/?text={message}"
            st.link_button("إرسال للواتساب الآن 🚀", wa_url)
        else:
            st.warning("يجب إضافة عملاء أولاً لتتمكن من مراسلتهم.")
            
