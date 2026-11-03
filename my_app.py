import streamlit as st
import time

st.title("사용자 정보")

message_placeholder = st.empty() # 미리 지정해 공간을 확보함

with st.form(key="my_infrom"):

    name = st.text_input("이름", placeholder= "이름을 입력해주세요 (예: 김현빈)").strip()
    
    str_age = st.text_input(
        "나이",max_chars=3 ,placeholder= "나이를 입력해주세요 (숫자만 입력 해주세요)"
    ).strip()

    str_age = "".join(
        digit for digit in str_age if digit.isdigit()
    )

    job = st.text_input("직업", placeholder="직업을 입력해주세요 (예: 학생)")
    
    phone_number = st.text_input(
    "전화번호",
    value="",
    max_chars=20,
    placeholder="전화번호를 입력해주세요"
    )

    phone_number = "".join(
    digit for digit in phone_number if digit.isdigit()
    )

    submitted = st.form_submit_button("제출")

if submitted:

    if not name or not str_age or not job or not phone_number:
        message_placeholder.error("모든 항목을 제대로 입력해주세요.")

    else:
        age = int(str_age)
        
        if len(phone_number) not in [10, 11]:
            message_placeholder.error("전화번호는 숫자 10개 또는 11개를 제대로 입력해주세요.")

        elif age <= 0 or age > 120:
            message_placeholder.error("제대로 된 나이를 입력해주세요")

        elif any(char.isdigit() for char in name):
            message_placeholder.error("이름에 숫자를 입력할 수 없습니다.")

        elif not all(char.isalpha() for char in name):
            message_placeholder.error("이름에 특수문자를 입력할 수 없습니다.")

        elif any(char.isdigit() for char in job):
            message_placeholder.error("직업에 숫자를 입력할 수 없습니다.")

        elif not all(char.isalpha() for char in job):
            message_placeholder.error("직업에 특수문자를 입력할 수 없습니다.")

        elif phone_number.startswith(("010", "011", "016", "017", "018", "019")) == False:
            message_placeholder.error("전화번호는 010, 011, 016, 017, 018, 019로 시작해야 합니다.")
        
        else:
            message_placeholder.info(f"이름: {name}  \n"
                                    f"나이: {age}  \n"
                                    f"직업: {job}  \n"
                                    f"전화번호: {phone_number}"
                                    )
            time.sleep(5)
            message_placeholder.empty()
    







