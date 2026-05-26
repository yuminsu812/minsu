import random
import streamlit as st

# 웹 페이지 제목과 설명
st.title("💡 결정 장애 해결사 (Decision Maker)")
st.subheader("선택지 때문에 머리가 아프신가요? 제가 골라드릴게요!")

st.markdown("---")

# 1. 사용자에게 선택지 입력받기 (기본값 제공)
options_input = st.text_input(
    "고민 중인 후보들을 쉼표(,)로 구분해서 입력해주세요:",
    value="짜장면, 짬뽕, 마라탕, 돈까스, 햄버거",
)

# 2. 결정 버튼 생성
if st.button("🧙‍♂️ 하늘의 계시 받기"):
    # 입력된 텍스트를 쉼표 기준으로 자르고, 앞뒤 공백 제거
    choices = [item.strip() for item in options_input.split(",") if item.strip()]

    if choices:
        # 리스트에서 무작위로 하나 선택
        selected = random.choice(choices)

        # 화면 효과와 결과 출력
        st.balloons()  # 화면에 풍선이 날아다니는 효과!
        st.success(f"🎯 오늘의 선택은 바로 **[{selected}]** 입니다! 더 이상 고민하지 마세요!")
    else:
        st.warning("앗! 선택지를 입력해 주셔야 골라드릴 수 있어요! 😅")
