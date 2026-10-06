import random
import streamlit as st

# 1. 웹앱 제목 설정
st.title("🎯 취미 추천 웹앱 ><")
st.write("실내 또는 실외를 선택하고 버튼을 눌러 오늘 할 취미를 추천받아보세요!")

# 2. 취미 데이터 준비 (실내 / 실외)
indoor_hobbies = [
    "독서하기 📚",
    "영화/드라마 감상 🎬",
    "요리/베이킹 👨‍🍳",
    "홈 트레이닝 🧘",
    "그림 그리기 🎨",
    "보드게임하기 🎲",
]

outdoor_hobbies = [
    "조깅/산책하기 🏃",
    "자전거 타기 🚴",
    "사진 촬영하기 📸",
    "등산하기 ⛰️",
    "캠핑가기 🏕️",
    "러닝/플로깅 🌳",
]

# 3. 사용자 선택 UI (라디오 버튼)
location = st.radio("어디서 활동하고 싶으신가요?", ("실내", "실외"))

# 4. 추천 버튼 생성 및 결과 출력
if st.button("취미 추천받기"):
    if location == "실내":
        # 실내 목록에서 랜덤으로 하나 선택
        selected_hobby = random.choice(indoor_hobbies)
    else:
        # 실외 목록에서 랜덤으로 하나 선택
        selected_hobby = random.choice(outdoor_hobbies)

    # 결과 보여주기
    st.success(f"오늘의 추천 취미는 바로 **[{selected_hobby}]** 입니다!")