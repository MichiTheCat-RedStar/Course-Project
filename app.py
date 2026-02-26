import streamlit as st
import json
import os

st.set_page_config(page_title='Аптека «Здоровье»', layout='centered')

# Основная часть
st.title('💊 Аптека «Здоровье»')
st.subheader('Забота о вашем здоровье - наша работа')
col1, col2 = st.columns(2)
with col1:
    st.markdown('''
    **О нас**  
    Мы предлагаем широкий ассортимент лекарств, медицинских изделий и товаров для здоровья.
    \n**Адрес:** г. Ростов, ул. Любая, д. 42
    \n**Телефон:** +8 800 555 35 35  
    \n**Часы работы:** Круглосуточно
    ''') # Не смотря на то, что это многострочная строка, всё равно без \n разметка билась, вероятно это особенности работы streamlit с markdown
st.markdown('---')
st.header('Регистрация для получения скидок')
with st.form('registration_form'):
    name = st.text_input('Имя')
    email = st.text_input('Email')
    phone = st.text_input('Телефон')
    submitted = st.form_submit_button('Зарегистрироваться')
if submitted:
    if not name or not email or not phone:
        st.error('Все поля обязательны для заполнения!')
    else:
        st.success('Спасибо! Вы зарегистрированы.')
        if os.path.exists('data/users.json'): # Чтение data/users.json
            with open('data/users.json', 'r', encoding='utf-8') as f:
                try: data = json.load(f)
                except json.JSONDecodeError: data = []
        else: data = []
    data.append(
        {
            "name": name,
            "email": email,
            "phone": phone
        }
    )
    with open('data/users.json', 'w', encoding='utf-8') as f: # Сохранение нового пользователя для рассылки в data/users.json
        json.dump(data, f, ensure_ascii=False, indent=4)