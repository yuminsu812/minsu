import random
import streamlit as st

# 웹 페이지 제목
st.title("🔮 YES or NO 결정 요정")
st.subheader("할까 말까 고민될 땐, 우주의 계시를 따르세요!")

st.markdown("---")

# 1. 사용자 질문 입력받기
question = st.text_input(
    "고민 중인 질문을 던져보세요:", value="오늘 야식으로 치킨 먹을까?"
)

# 2. 결정 버튼 생성
if st.button("🔮 운명의 주사위 굴리기"):
    if question:
        # '예' 또는 '아니요' 중 무작위 선택
        answer = random.choice(["YES", "NO"])

        if answer == "YES":
            st.balloons()  # 예스일 때는 축하 풍선!
            st.success("### ⭕ 네! 당장 진행하세요! 망설이지 마세요!")
        else:
            st.snow()  # 노일 때는 차분하게 식혀줄 눈 효과!
            st.error("### ❌ 아니요! 절대 안 됩니다! 참으세요!")
    else:
        st.warning("질문을 먼저 입력해 주셔야 우주가 대답해 줍니다! 😅")
