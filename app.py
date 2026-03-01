import streamlit as st
import json
import os

st.set_page_config(page_title='Аптека «Здоровье»', page_icon="💊", layout='centered')
os.makedirs("data", exist_ok=True)
PASSWORD = 'qwerty' # макетная часть для отображения информации разработчика, показывает как мог бы выглядить пароль на настоящем сайте

# Основная часть
menu = st.sidebar.radio('Страницы', ['Макет', 'О проекте'])

if menu == 'Макет': # Макет
    st.title('💊 Аптека «Здоровье»')
    st.subheader('Забота о вашем здоровье - наша работа')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
        **О нас**  
        Мы предлагаем широкий ассортимент лекарств, медицинских изделий и товаров для здоровья.
        \n**Адрес:** г. Ростов, ул. Любая, д. 42
        \n**Телефон:** 8 800 555 35 35  
        \n**Часы работы:** Круглосуточно
        ''') # Не смотря на то, что это многострочная строка, всё равно без \n разметка билась, вероятно это особенности работы streamlit с markdown
    with col2:
        st.image("data/img/1.jpg", caption="Наша аптека")
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
            if not '@' in email: # Валидатор
                st.error('В Email должна быть указана почта!')
            elif len(phone) < 11 or len(phone) > 13:
                st.error('В телефоне должна быть указано от 11 до 13 цифр!')
            elif len(name) > 32:
                st.error('Имя не должно быть длиннее 32 символов!')
            elif len(email) > 32:
                st.error('Почта не должна быть длиннее 32 символов!')
            else:
                if os.path.exists('data/users.json'): # Чтение data/users.json
                    with open('data/users.json', 'r', encoding='utf-8') as f:
                        try: data = json.load(f)
                        except json.JSONDecodeError: data = []
                else: data = []
                data.append({
                        "name": name,
                        "email": email,
                        "phone": phone})
                with open('data/users.json', 'w', encoding='utf-8') as f: # Сохранение нового пользователя для рассылки в data/users.json
                    json.dump(data, f, ensure_ascii=False, indent=4)
                st.success('Спасибо! Вы зарегистрированы.')

elif menu == 'О проекте': # О проекте
    st.title('Информация о курсовом проекте')
    st.markdown('''
        В основном тут представлена информация из `readme.md` файла
        
        Перед вами одностраничный сайт-визитка для аптеки, включающий форму регистрации пользователей.  
        Разработан в рамках курсового проекта.
                
        - **Telegram**: [@TeaTechnology](https://t.me/TeaTechnology)
        - **GitHub**: [MichiTheCat-RedStar](https://github.com/MichiTheCat-RedStar)
        - **Itch.io**: [michi-the-cat](https://michi-the-cat.itch.io)
                
        - **Репозиторий:** [Course-Project](https://github.com/MichiTheCat-RedStar/Course-Project)
                
        ---
        ''')
    with st.form('admin_password'):
        password = st.text_input('Пароль')
        submitted = st.form_submit_button('Войти')
    if submitted:
        if password == PASSWORD:
            st.success('Пароль верный.')
            if os.path.exists('data/users.json'):
                with open('data/users.json', 'r', encoding='utf-8') as f:
                    try: data = json.load(f)
                    except json.JSONDecodeError: data = []
            else: data = []
            st.markdown(f'''
                ## информация для разработчика:
                        
                ### `users.json`
                python:
                ```python
                {data}
                ```

                таблица:
                ''')
            st.dataframe(data)
        else:
            st.error('Неверный пароль!')