import streamlit as st

st.set_page_config(page_title="دكان بلس - الدخول", page_icon="👑")

st.markdown("<h1 style='text-align: center; color: #2e8b57;'>👑 دكان بلس</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.subheader("📝 تسجيل الدخول")
    phone = st.text_input("رقم الواتساب")
    account_type = st.radio("نوع الحساب", ["تاجر", "مشتري"])
    
    if st.button("دخول المنظومة"):
        if phone:
            st.session_state.u_phone = phone
            st.session_state.u_type = account_type
            st.success("تم الدخول.. اختر القسم من القائمة الجانبية ⬅️")
        else:
            st.error("برجاء إدخال الرقم")

st.info("💡 بعد الدخول، ستظهر لك الأقسام في القائمة الجانبية حسب نوع حسابك.")
