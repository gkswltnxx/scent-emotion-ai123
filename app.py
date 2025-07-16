import streamlit as st
from transformers import pipeline

# 감정 분석 모델 로드
sentiment_analyzer = pipeline("sentiment-analysis")

# 향 추천 함수
def recommend_scent(emotion):
    if emotion == "NEGATIVE":
        return "라벤더, 캐모마일 (진정)"
    elif emotion == "POSITIVE":
        return "레몬, 자몽 (활력)"
    else:
        return "페퍼민트, 유칼립투스 (회복)"

st.title("감정 분석 & 향 추천기")
st.write("당신의 기분에 맞는 향을 추천해드릴게요!")

# 사용자 입력
user_input = st.text_area("지금 기분을 자유롭게 입력해보세요")

if st.button("AI 분석 시작"):
    if user_input:
        result = sentiment_analyzer(user_input)[0]
        emotion = result['label']
        scent = recommend_scent(emotion)
        st.success(f"AI 감정 분석 결과: **{emotion}**")
        st.info(f"추천 향: **{scent}**")
    else:
        st.warning("먼저 감정을 입력해주세요.")
