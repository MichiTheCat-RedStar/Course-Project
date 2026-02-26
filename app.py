import json
import os
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Аптека «Здоровье»", layout="centered")

if True:
    st.title("💊 Аптека «Здоровье»")
    st.subheader("Забота о вашем здоровье — наша работа")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **О нас**  
        Мы предлагаем широкий ассортимент лекарств, медицинских изделий и товаров для здоровья.

        **Адрес:** г. Ростов, ул. Любая, д. 42
        **Телефон:** +8 800 555 35 35  
        **Часы работы:** Круглосуточно
        """)

    st.markdown("---")
    st.header("Регистрация для получения скидок")

    with st.form("registration_form"):
        name = st.text_input("Имя")
        email = st.text_input("Email")
        phone = st.text_input("Телефон")
        submitted = st.form_submit_button("Зарегистрироваться")