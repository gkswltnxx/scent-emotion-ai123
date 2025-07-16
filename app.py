import streamlit as st
from transformers import pipeline

# 한글 감정 분석 모델 로드 (KoELECTRA 등 자동 언어 감지)
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# 감정 분석 결과 점수 → 감정 이름 변환 함수 (간단 분류)
def classify_emotion(star_rating):
    if star_rating <= 2:
        return "슬픔"
    elif star_rating == 3:
        return "중립"
    elif star_rating == 4:
        return "기쁨"
    else:  # 5점
        return "활력"

# 감정 기반 향 추천 함수
def recommend_scent(emotion):
    if emotion == "슬픔":
        return "🌧️ 감정: 슬픔\n추천 향: **라벤더** – 불안과 슬픔을 진정시켜주는 향입니다."
    elif emotion == "불안":
        return "😣 감정: 불안\n추천 향: **로즈마리가든** – 긴장을 완화하고 집중력을 높여줘요."
    elif emotion == "활력":
        return "🍊 감정: 활력\n추천 향: **헤스페리스 자몽** – 상큼하고 생기 넘치는 향입니다."
    elif emotion == "여유":
        return "😌 감정: 여유\n추천 향: **떼누아 29** – 고요하고 고급스러운 무드를 완성해요."
    elif emotion == "편안함":
        return "🌼 감정: 편안함\n추천 향: **프리지아** – 포근하고 따뜻한 감정에 어울리는 향이에요."
    elif emotion == "안정":
        return "🧺 감정: 안정\n추천 향: **클린 웜코튼** – 깨끗한 이불처럼 포근한 향입니다."
    elif emotion == "중립":
        return "🌫️ 감정: 중립\n추천 향: **화이트 머스크** – 부담 없고 깔끔한 향이에요."
    else:
        return "❓ 감정을 인식하지 못했어요. 감정을 조금 더 자세히 입력해 주세요."

# Streamlit UI
st.title("🌸 한글 감정 분석 향 추천기")
st.write("지금 당신의 기분을 한글로 입력하면 어울리는 향을 추천해드려요!")

# 사용자 입력
user_input = st.text_area("현재 기분을 자유롭게 적어주세요 (예: 오늘 좀 지치고 우울해요)")

if st.button("향 추천 받기"):
    if user_input:
        # 감정 분석 실행
        result = sentiment_analyzer(user_input)[0]
        label = result['label']
        
        # 별점(1~5) → 감정명 분류
        stars = int(label[0])  # '5 stars' → 5
        emotion = classify_emotion(stars)

        # 감정 기반 향 추천
        scent = recommend_scent(emotion)

        st.success(f"🧠 감정 분석 결과: {emotion}")
        st.info(scent)
    else:
        st.warning("먼저 기분을 입력해주세요.")