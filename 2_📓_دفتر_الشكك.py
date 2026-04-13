import streamlit as st
import pandas as pd
from datetime import datetime

# إعداد الصفحة
st.set_page_config(page_title="كشف حساب دكان بلس", layout="wide")

st.markdown("<h2 style='text-align: center; color: #2e8b57;'>🧾 كشف الحساب التراكمي</h2>", unsafe_allow_html=True)

# 1. إنشاء/تحميل قاعدة البيانات (الربط بملف إكسل مصغر CSV)
if "transactions_db" not in st.session_state:
    # هيكل الجدول: التاريخ، الاسم، البيان، مدين (أخذ)، دائن (دفع)، الرصيد
    st.session_state.transactions_db = pd.DataFrame(columns=["التاريخ", "الاسم", "البيان", "مدين (+)", "دائن (-)", "الرصيد"])

# 2. إضافة معاملة جديدة
with st.expander("➕ تسجيل عملية جديدة (بيع / تحصيل / مرتجع)"):
    with st.form("trans_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("اسم العميل")
            type_op = st.selectbox("نوع العملية", ["شراء (مدين)", "دفع مبلع (دائن)", "مرتجع (دائن)"])
        with col2:
            desc = st.text_input("البيان (سكر، زيت، عباية، إلخ)")
            amount = st.number_input("القيمة (جنيه)", min_value=0.0)
        
        if st.form_submit_button("تسجيل المعاملة ✅"):
            if name and amount > 0:
                # تحديد القيمة (مدين أو دائن)
                debit = amount if type_op == "شراء (مدين)" else 0
                credit = amount if type_op in ["دفع مبلع (دائن)", "مرتجع (دائن)"] else 0
                
                # حساب الرصيد التراكمي للعميل
                client_history = st.session_state.transactions_db[st.session_state.transactions_db["الاسم"] == name]
                last_balance = client_history["الرصيد"].iloc[-1] if not client_history.empty else 0
                new_balance = last_balance + debit - credit
                
                # إضافة السطر الجديد
                new_entry = {
                    "التاريخ": datetime.now().strftime("%Y/%m/%d %H:%M"),
                    "الاسم": name,
                    "البيان": desc if type_op != "مرتجع (دائن)" else f"مرتجع: {desc}",
                    "مدين (+)": debit,
                    "دائن (-)": credit,
                    "الرصيد": new_balance
                }
                st.session_state.transactions_db = pd.concat([st.session_state.transactions_db, pd.DataFrame([new_entry])], ignore_index=True)
                st.success(f"تم تسجيل العملية لـ {name}. الرصيد الحالي: {new_balance}")
                st.rerun()

st.write("---")

# 3. البحث وعرض كشف الحساب
search_name = st.text_input("🔍 ابحث عن اسم العميل لعرض كشف حسابه التفصيلي:")

if search_name:
    client_df = st.session_state.transactions_db[st.session_state.transactions_db["الاسم"] == search_name]
    
    if not client_df.empty:
        # الملخص العلوي (البروفايل المالي)
        current_bal = client_df["الرصيد"].iloc[-1]
        total_taken = client_df["مدين (+)"].sum()
        total_paid = client_df["دائن (-)"].sum()
        
        c1, c2, c3 = st.columns(3)
        c1.metric("إجمالي المديونية", f"{current_bal} ج.م")
        c2.metric("إجمالي ما سحبه", f"{total_taken} ج.م")
        c3.metric("إجمالي ما دفعه", f"{total_paid} ج.م")
        
        st.write(f"### سجل معاملات: {search_name}")
        st.table(client_df[["التاريخ", "البيان", "مدين (+)", "دائن (-)", "الرصيد"]])
        
        # زر التحميل لـ Excel
        csv = client_df.to_csv(index=False).encode('utf-8-sig')
        st.download_button("📥 تحميل كشف الحساب (Excel/CSV)", csv, f"statement_{search_name}.csv", "text/csv")
    else:
        st.warning("هذا الاسم غير مسجل في الدفتر.")
else:
    st.info("اكتب اسم العميل لمشاهدة رصيده التراكمي.")

st.write("---")
st.caption("دكان بلس 2026 - نظام المحاسبة الذكي")
      
