import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="دكان بلس", page_icon="🏪", layout="wide")

# 2. تصميم الواجهة (CSS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stButton>button { border-radius: 15px; width: 100%; background: linear-gradient(45deg, #2e8b57, #3cb371); color: white; border: none; height: 3.5em; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 3. إدارة الحالة (Session State)
if "step" not in st.session_state:
    st.session_state.step = "register"
if "db" not in st.session_state:
    st.session_state.db = pd.DataFrame(columns=["الاسم", "المبلغ", "الموبايل", "الحالة", "التقييم"])

st.markdown("<h1 style='text-align: center; color: #2e8b57;'>👑 دكان بلس</h1>", unsafe_allow_html=True)

# --- المرحلة الأولى: بوابة الدخول ---
if st.session_state.step == "register":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.subheader("📝 سجل هويتك التجارية")
        u_name = st.text_input("الأسم الكامل")
        u_phone = st.text_input("رقم الواتساب")
        u_type = st.selectbox("نوع النشاط", ["تاجر (عرض وتحصيل)", "مشتري (بحث وتصفح)"])
        if st.button("انطلق للإمبراطورية 🚀"):
            if u_name and u_phone:
                st.session_state.u_name = u_name
                st.session_state.u_phone = u_phone
                st.session_state.u_type = u_type
                st.session_state.step = "home"
                st.rerun()
            else:
                st.error("أكمل البيانات أولاً")

# --- المرحلة الثانية: التطبيق الرئيسي ---
elif st.session_state.step == "home":
    choice = option_menu(None, ["المعرض الشامل", "دفتر الشكك", "محرك الصيد"], 
        icons=['shop', 'journal-check', 'radar'], orientation="horizontal")

    if choice == "المعرض الشامل":
        st.info(f"مرحباً {st.session_state.u_name} في المول الرقمي 🎪")
        c1, c2, c3 = st.columns(3)
        with c1:
            with st.expander("🐮 الحيوانات والأعلاف"):
                st.write("🐑 خراف\n🐄 عجول\n🌾 أعلاف")
        with c2:
            with st.expander("👕 الملابس"):
                st.write("👔 رجالي\n👗 حريمي\n👶 أطفال")
        with c3:
            with st.expander("⛽ خدمات"):
                st.write("📍 بنزين\n🔥 غاز")

    elif choice == "دفتر الشكك":
        if st.session_state.u_type == "تاجر (عرض وتحصيل)":
            n_n = st.text_input("اسم العميل")
            n_m = st.number_input("قيمة الدين", min_value=0)
            n_p = st.text_input("واتساب العميل")
            if st.button("حفظ في الخزنة 💾"):
                new_rec = pd.DataFrame([{"الاسم": n_n, "المبلغ": n_m, "الموبايل": n_p, "الحالة": "مطلوب", "التقييم": "ممتاز"}])
                st.session_state.db = pd.concat([st.session_state.db, new_rec], ignore_index=True)
                st.success("تم الحفظ")
                st.rerun()
            
            st.divider()
            st.write("### الديون المسجلة")
            st.table(st.session_state.db)
        else:
            st.warning("هذا القسم للتجار فقط.")

    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.step = "register"
        st.rerun()

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>بإشراف المهندس سيلا | دكان بلس 2026 👑</p>", unsafe_allow_html=True)
            if u_name and u_phone:
                st.session_state.update({"u_name": u_name, "u_phone": u_phone, "u_type": u_type, "step": "home"})
                st.balloons(); st.rerun()

# --- المرحلة الثانية: قلب التطبيق ---
elif st.session_state.step == "home":
    choice = option_menu(None, ["المعرض الشامل", "دفتر الشكك الذكي", "محرك الصيد (قريباً)"], 
        icons=['shop', 'journal-check', 'radar'], orientation="horizontal",
        styles={"nav-link-selected": {"background-color": "#2e8b57"}})

    # --- 1. المعرض البصري (شجري) ---
    if choice == "المعرض الشامل":
        st.info(f"مرحباً {st.session_state.u_name} | أنت الآن في المول الرقمي 🎪")
        
        # ميزة البحث (صوت/كتابة)
        search = st.text_input("🎙️ ابحث بالصوت أو اكتب (خروف، جزمة، بنزين...)", placeholder="ماذا يدور في عقلك؟")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            with st.expander("🐮 الحيوانات والأعلاف"):
                if st.button("📸 إضافة منتج حيواني (للتاجر)"): st.camera_input("صور السلعة")
                st.write("🐑 خراف عيد\n🐄 عجول تسمين\n🌾 ذرة وأعلاف مركبة")
        with c2:
            with st.expander("👕 الملابس والأزياء"):
                st.write("👔 رجالي وشبابي\n👗 حريمي ولانجري\n👶 أطفال وأحذية")
        with c3:
            with st.expander("⛽ الخدمات والبنزين"):
                st.write("📍 أقرب محطة\n🔥 غاز ومستلزمات")

    # --- 2. دفتر الشكك (قوة التاجر) ---
    elif choice == "دفتر الشكك الذكي":
        if st.session_state.u_type == "تاجر (عرض وتحصيل)":
            tab_view, tab_add = st.tabs(["📊 كشف حساب الديون", "➕ إضافة مديون جديد"])
            
            with tab_view:
                if not st.session_state.db.empty:
                    for idx, row in st.session_state.db.iterrows():
                        with st.container():
                            st.markdown(f"**👤 {row['الاسم']}** | 💰 {row['المبلغ']} ج.م | ⭐ تقييم: {row['التقييم']}")
                            
                            # ميزة "جدولة الرخامة" والواتساب
                            msg = f"تحية من *دكان بلس* 👑\nنذكركم بموعد القسط بقيمة {row['المبلغ']} ج.م لمحل {st.session_state.u_name}.\n*اليقين دائماً يكسب* ✨"
                            link = f"https://wa.me/{row['الموبايل']}?text={urllib.parse.quote(msg)}"
                            
                            col_a, col_b = st.columns(2)
                            col_a.markdown(f"[🔔 إرسال تنبيه واتساب]({link})")
                            if col_b.button(f"تصفية الحساب ✅", key=f"pay_{idx}"):
                                st.session_state.db.drop(idx, inplace=True); st.rerun()
                else: st.write("الدفتر نظيف.. لا يوجد ديون.")

            with tab_add:
                st.subheader("تسجيل مديونية جديدة")
                n_n = st.text_input("اسم العميل")
                n_p = st.text_input("واتساب العميل")
                n_m = st.number_input("قيمة الدين", min_value=0)
                n_r = st.select_slider("تقييم التزام العميل (سري للتاجر)", options=["ملاوع 😡", "متوسط 😐", "ملتزم 💎"])
                
                if st.button("حفظ في الخزنة 💾"):
                    new_rec = pd.DataFrame([{"الاسم": n_n, "المبلغ": n_m, "الموبايل": n_p, "الحالة": "مطلوب", "التقييم": n_r}])
                    st.session_state.db = pd.concat([st.session_state.db, new_rec], ignore_index=True)
                    st.success("تم الحفظ والجدولة."); st.rerun()
        else:
            st.warning("⚠️ عذراً، هذا القسم مخصص للتجار فقط لإدارة حساباتهم.")

    # --- 3. تسجيل الخروج ---
    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.step = "register"
        st.rerun()

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>بإشراف المهندس سيلا | دكان بلس 2026 👑</p>", unsafe_allow_html=True)
            if u_name and u_phone:
                st.session_state.update({"u_name": u_name, "u_phone": u_phone, "u_type": u_type, "step": "home"})
                st.balloons(); st.rerun()

# --- المرحلة الثانية: قلب التطبيق ---
elif st.session_state.step == "home":
    choice = option_menu(None, ["المعرض الشامل", "دفتر الشكك الذكي", "محرك الصيد (قريباً)"], 
        icons=['shop', 'journal-check', 'radar'], orientation="horizontal",
        styles={"nav-link-selected": {"background-color": "#2e8b57"}})

    # --- 1. المعرض البصري (شجري) ---
    if choice == "المعرض الشامل":
        st.info(f"مرحباً {st.session_state.u_name} | أنت الآن في المول الرقمي 🎪")
        
        # ميزة البحث (صوت/كتابة)
        search = st.text_input("🎙️ ابحث بالصوت أو اكتب (خروف، جزمة، بنزين...)", placeholder="ماذا يدور في عقلك؟")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            with st.expander("🐮 الحيوانات والأعلاف"):
                if st.button("📸 إضافة منتج حيواني (للتاجر)"): st.camera_input("صور السلعة")
                st.write("🐑 خراف عيد\n🐄 عجول تسمين\n🌾 ذرة وأعلاف مركبة")
        with c2:
            with st.expander("👕 الملابس والأزياء"):
                st.write("👔 رجالي وشبابي\n👗 حريمي ولانجري\n👶 أطفال وأحذية")
        with c3:
            with st.expander("⛽ الخدمات والبنزين"):
                st.write("📍 أقرب محطة\n🔥 غاز ومستلزمات")

    # --- 2. دفتر الشكك (قوة التاجر) ---
    elif choice == "دفتر الشكك الذكي":
        if st.session_state.u_type == "تاجر (عرض وتحصيل)":
            tab_view, tab_add = st.tabs(["📊 كشف حساب الديون", "➕ إضافة مديون جديد"])
            
            with tab_view:
                if not st.session_state.db.empty:
                    for idx, row in st.session_state.db.iterrows():
                        with st.container():
                            st.markdown(f"**👤 {row['الاسم']}** | 💰 {row['المبلغ']} ج.م | ⭐ تقييم: {row['التقييم']}")
                            
                            # ميزة "جدولة الرخامة" والواتساب
                            msg = f"تحية من *دكان بلس* 👑\nنذكركم بموعد القسط بقيمة {row['المبلغ']} ج.م لمحل {st.session_state.u_name}.\n*اليقين دائماً يكسب* ✨"
                            link = f"https://wa.me/{row['الموبايل']}?text={urllib.parse.quote(msg)}"
                            
                            col_a, col_b = st.columns(2)
                            col_a.markdown(f"[🔔 إرسال تنبيه واتساب]({link})")
                            if col_b.button(f"تصفية الحساب ✅", key=f"pay_{idx}"):
                                st.session_state.db.drop(idx, inplace=True); st.rerun()
                else: st.write("الدفتر نظيف.. لا يوجد ديون.")

            with tab_add:
                st.subheader("تسجيل مديونية جديدة")
                n_n = st.text_input("اسم العميل")
                n_p = st.text_input("واتساب العميل")
                n_m = st.number_input("قيمة الدين", min_value=0)
                n_r = st.select_slider("تقييم التزام العميل (سري للتاجر)", options=["ملاوع 😡", "متوسط 😐", "ملتزم 💎"])
                
                if st.button("حفظ في الخزنة 💾"):
                    new_rec = pd.DataFrame([{"الاسم": n_n, "المبلغ": n_m, "الموبايل": n_p, "الحالة": "مطلوب", "التقييم": n_r}])
                    st.session_state.db = pd.concat([st.session_state.db, new_rec], ignore_index=True)
                    st.success("تم الحفظ والجدولة."); st.rerun()
        else:
            st.warning("⚠️ عذراً، هذا القسم مخصص للتجار فقط لإدارة حساباتهم.")

    # --- 3. تسجيل الخروج ---
    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.step = "register"
        st.rerun()

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>بإشراف المهندس سيلا | دكان بلس 2026 👑</p>", unsafe_allow_html=True)
        with st.expander("🐮 الحيوانات"):
            st.write("🐑 أغنام - 🐄 مواشي")
    with col2:
        with st.expander("🦜 الطيور"):
            st.write("🐣 زينة - 🍗 أكل")
    with col3:
        with st.expander("👕 الملابس"):
            st.write("👔 رجالي - 👗 حريمي")
    with col4:
        with st.expander("🚗 السيارات"):
            st.write("🏎️ ملاكي - 🚛 نقل - 🏍️ موتوسيكلات")

else: # لوحة التاجر
    if not st.session_state.authenticated:
        st.info("🔐 منطقة محمية")
        password = st.text_input("كود التاجر", type="password")
        if st.button("فتح النظام"):
            if password == "SILA2026":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ الكود غير صحيح")
    else:
        st.success("✅ مرحباً بك في إدارة دكان بلس")
        t1, t2, t3 = st.tabs(["📓 دفتر الشكك", "➕ إدارة العملاء", "🗺️ الخرائط"])
        
        with t1:
            st.subheader("قائمة المديونيات الحالية")
            if not st.session_state.clients_db.empty:
                for index, row in st.session_state.clients_db.iterrows():
                    c1, c2, c3, c4 = st.columns([2, 1, 1, 1])
                    c1.write(f"👤 **{row['الاسم']}**")
                    c2.write(f"💰 {row['المبلغ']} ج")
                    status_color = "🟢" if row['الحالة'] == "تم السداد" else "🔴"
                    c3.write(f"{status_color} {row['الحالة']}")
                    
                    if row['الحالة'] == "مطلوب":
                        if c4.button("تأكيد السداد ✅", key=f"pay_{index}"):
                            st.session_state.clients_db.at[index, 'الحالة'] = "تم السداد"
                            st.rerun()
                    else:
                        if c4.button("إلغاء السداد ↩️", key=f"undo_{index}"):
                            st.session_state.clients_db.at[index, 'الحالة'] = "مطلوب"
                            st.rerun()
                st.divider()
            else:
                st.write("لا يوجد عملاء حالياً.")

        with t2:
            st.subheader("إضافة أو حذف عميل")
            new_name = st.text_input("اسم العميل الجديد")
            new_amount = st.text_input("المبلغ المستحق")
            if st.button("إضافة للدفتر ➕"):
                if new_name and new_amount:
                    new_entry = pd.DataFrame([{"الاسم": new_name, "المبلغ": new_amount, "الحالة": "مطلوب"}])
                    st.session_state.clients_db = pd.concat([st.session_state.clients_db, new_entry], ignore_index=True)
                    st.success(f"تمت إضافة {new_name}")
                    st.rerun()
            
            st.divider()
            st.write("🗑️ **حذف عميل نهائياً:**")
            del_index = st.number_input("أدخل رقم السطر للحذف", min_value=0, max_value=len(st.session_state.clients_db)-1, step=1)
            if st.button("حذف العميل نهائياً ❌"):
                st.session_state.clients_db = st.session_state.clients_db.drop(st.session_state.clients_db.index[del_index])
                st.rerun()

        with t3:
            st.write("📍 جارٍ العمل على محرك صيد الموردين...")

st.markdown("---")
st.caption("إدارة دكان بلس 2026")
