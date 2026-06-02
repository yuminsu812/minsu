
import streamlit as st
from google import genai

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="연애상담 챗봇",
    page_icon="💕",
    layout="centered"
)

st.title("💕 연애상담 챗봇")
st.caption("Gemini 2.5 Flash Lite 기반")

# -----------------------------
# API 키 확인
# -----------------------------
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("GEMINI_API_KEY가 설정되지 않았습니다.")
    st.stop()

# -----------------------------
# Gemini 클라이언트 생성
# -----------------------------
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Gemini 초기화 오류: {e}")
    st.stop()

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "안녕하세요 😊\n\n"
                "연애 고민, 썸, 이별, 재회, 고백, 커플 갈등 등 "
                "무엇이든 편하게 이야기해 주세요."
            )
        }
    ]

# -----------------------------
# 기존 대화 출력
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# 사용자 입력
# -----------------------------
user_input = st.chat_input("고민을 입력하세요...")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("생각 중..."):

            try:

                # 최근 대화 기록 활용
                history_text = ""

                for m in st.session_state.messages[-10:]:
                    role = "사용자" if m["role"] == "user" else "상담사"
                    history_text += f"{role}: {m['content']}\n"

                prompt = f"""
당신은 따뜻하고 공감 능력이 높은 연애상담 전문가입니다.

규칙:
1. 사용자를 존중한다.
2. 현실적인 조언을 제공한다.
3. 과도한 단정은 하지 않는다.
4. 답변은 친절하고 이해하기 쉽게 작성한다.

대화 기록:
{history_text}

상담 답변:
"""

                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=prompt
                )

                answer = response.text

            except Exception as e:
                answer = f"""
죄송합니다. 응답 생성 중 오류가 발생했습니다.

오류 내용:
{e}
"""

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# -----------------------------
# 대화 초기화
# -----------------------------
st.divider()

if st.button("🗑️ 대화 초기화"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "새로운 상담을 시작해볼까요? 😊"
        }
    ]
    st.rerun()
