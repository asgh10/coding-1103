import streamlit as st


# st.form()
name = st.text_input("이름")
age = st.text_input("나이")
job = st.text_input("직업")
# 일반적으로 입력할 때마다 값이 반영되지만 st.form()으로 묶으면 제출 버튼을 누를 때 입력값들이 한꺼번에 처리된다

# -----------------------------------------------------------------------------------------------------

# with
with st.form(key="my_infrom"):
    name = st.text_input("이름")
    age = st.text_input("나이")
    job = st.text_input("직업")
# 코드를 하나의 폼으로 묶어주는 기능

#-----------------------------------------------------------------------------------------------------

# key="my_infrom"
with st.form(key="user_form"):
    name = st.text_input("이름")
    age = st.text_input("나이")
    job = st.text_input("직업")
# 여기서 user_form이라는 이름은 개발자가 직접 정할 수 있다 마치 함수처럼
# 주의점은 같은 Streamlit 앱 안에서 다른 요소와 key가 중복되지 않도록 해야 한다

# -----------------------------------------------------------------------------------------------------

# st.form_submit_button()
submit_button = st.form_submit_button("제출")
# 폼을 제출하는 버튼을 생성 ("제출") 버튼에 표시할 값

# -----------------------------------------------------------------------------------------------------
 
# submitted
# submitted는 버튼을 눌렀는지 여부를 저장하는 변수 버튼을 눌렀다면 True 안눌렀다면 False를 반환한다
# 여기서 submitted라는 변수명은 개발자가 직접 정할 수 있다

