import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="LoveFit Diet Mate",
    page_icon="💕",
    layout="wide"
)

# -----------------------------
# 음식 데이터
# -----------------------------
FOODS = {
    "닭가슴살 🍗": {"cal": 165, "carb": 0, "protein": 31, "fat": 3.6},
    "고구마 🍠": {"cal": 128, "carb": 30, "protein": 2, "fat": 0.2},
    "바나나 🍌": {"cal": 89, "carb": 23, "protein": 1.1, "fat": 0.3},
    "계란 🥚": {"cal": 78, "carb": 0.6, "protein": 6, "fat": 5},
    "샐러드 🥗": {"cal": 50, "carb": 10, "protein": 2, "fat": 0.5},
    "현미밥 🍚": {"cal": 216, "carb": 45, "protein": 5, "fat": 1.8},
    "연어 🍣": {"cal": 208, "carb": 0, "protein": 20, "fat": 13},
    "아보카도 🥑": {"cal": 160, "carb": 9, "protein": 2, "fat": 15},
    "견과류 🥜": {"cal": 170, "carb": 6, "protein": 6, "fat": 15},
    "치킨 🍗": {"cal": 320, "carb": 10, "protein": 25, "fat": 20},
    "피자 🍕": {"cal": 285, "carb": 36, "protein": 12, "fat": 10},
    "햄버거 🍔": {"cal": 354, "carb": 29, "protein": 17, "fat": 18},
    "떡볶이 🌶️": {"cal": 280, "carb": 58, "protein": 5, "fat": 2},
}

# -----------------------------
# 세션 상태
# -----------------------------
if "food_log" not in st.session_state:
    st.session_state.food_log = []

# -----------------------------
# 헤더
# -----------------------------
st.title("💕 LoveFit Diet Mate")
st.caption("오늘의 식단이 내일의 자신감을 만듭니다")

st.info(
    "건강한 자기관리는 연애 자신감의 시작! "
    "오늘 먹은 음식을 기록하고 영양 밸런스를 확인해보세요 💖"
)

# -----------------------------
# 음식 추가
# -----------------------------
st.subheader("🍽️ 음식 기록")

col1, col2, col3 = st.columns([3,1,1])

with col1:
    selected_food = st.selectbox(
        "음식 선택",
        list(FOODS.keys())
    )

with col2:
    quantity = st.number_input(
        "수량",
        min_value=1,
        max_value=20,
        value=1
    )

with col3:
    st.write("")
    st.write("")

    if st.button("추가"):
        st.session_state.food_log.append(
            {
                "음식": selected_food,
                "수량": quantity
            }
        )
        st.success("추가 완료!")

# -----------------------------
# 기록 표시
# -----------------------------
st.subheader("📋 오늘 먹은 음식")

if len(st.session_state.food_log) == 0:
    st.warning("아직 기록된 음식이 없습니다.")
else:

    rows = []

    total_cal = 0
    total_carb = 0
    total_protein = 0
    total_fat = 0

    for item in st.session_state.food_log:
        food = item["음식"]
        qty = item["수량"]

        data = FOODS[food]

        cal = data["cal"] * qty
        carb = data["carb"] * qty
        protein = data["protein"] * qty
        fat = data["fat"] * qty

        total_cal += cal
        total_carb += carb
        total_protein += protein
        total_fat += fat

        rows.append(
            [
                food,
                qty,
                cal
            ]
        )

    df = pd.DataFrame(
        rows,
        columns=["음식", "수량", "칼로리"]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    if st.button("전체 기록 삭제"):
        st.session_state.food_log = []
        st.rerun()

    st.divider()

    # -----------------------------
    # 영양 분석
    # -----------------------------
    st.subheader("📊 영양 분석")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("총 칼로리", f"{total_cal:.0f} kcal")
    c2.metric("탄수화물", f"{total_carb:.1f} g")
    c3.metric("단백질", f"{total_protein:.1f} g")
    c4.metric("지방", f"{total_fat:.1f} g")

    macro_sum = total_carb + total_protein + total_fat

    if macro_sum > 0:

        carb_ratio = total_carb / macro_sum * 100
        protein_ratio = total_protein / macro_sum * 100
        fat_ratio = total_fat / macro_sum * 100

        ratio_df = pd.DataFrame(
            {
                "비율": [
                    carb_ratio,
                    protein_ratio,
                    fat_ratio
                ]
            },
            index=[
                "탄수화물",
                "단백질",
                "지방"
            ]
        )

        st.bar_chart(ratio_df)

    st.divider()

    # -----------------------------
    # 식단 평가
    # -----------------------------
    st.subheader("🤖 오늘의 식단 코치")

    advice = []

    if total_protein >= 60:
        advice.append("💪 단백질 섭취가 좋아요!")
    else:
        advice.append("🍗 단백질을 조금 더 늘려보세요.")

    if total_fat > total_protein:
        advice.append("🥲 지방 비중이 조금 높아요.")

    if total_cal <= 1800:
        advice.append("✨ 칼로리 관리가 잘 되고 있어요.")
    else:
        advice.append("⚠️ 칼로리가 조금 높은 편이에요.")

    healthy_foods = [
        "닭가슴살 🍗",
        "고구마 🍠",
        "샐러드 🥗",
        "연어 🍣",
        "아보카도 🥑"
    ]

    healthy_count = sum(
        1
        for item in st.session_state.food_log
        if item["음식"] in healthy_foods
    )

    if healthy_count >= 3:
        advice.append(
            "🌟 균형 잡힌 식단을 선택하고 있어요!"
        )

    for a in advice:
        st.write(a)

    st.success(
        "💖 건강한 습관은 매력을 더욱 빛나게 합니다!"
    )

# -----------------------------
# 하단
# -----------------------------
st.divider()

st.markdown(
    """
### 💌 Love Message

건강한 식습관은 단순히 체중 관리가 아니라
자신감을 높여주는 최고의 자기관리입니다.

오늘도 한 걸음 더 멋진 나를 만들어보세요 ✨
"""
)
