import streamlit as st
from transformers import pipeline

# 감정 분석 모델 (멀티 감정에 가까운 성격)
sentiment = pipeline("text-classification", model="Jinuuuu/KoELECTRA_fine_tunning_emotion", top_k=3)

# 감정 → 향 매핑
scent_map = {
    "angry": ("분노 😡", "프리지아 – 따뜻한 위로를 주는 향"),
    "anxious": ("불안 😣", "로즈마리가든 – 긴장을 풀고 안정감을 주는 향"),
    "embarrassed": ("당황 😳", "클린 웜코튼 – 정돈된 감정을 돕는 포근한 향"),
    "happy": ("행복 😊", "헤스페리스 자몽 – 상쾌하고 즐거운 분위기의 향"),
    "heartache": ("상처 💔", "라벤더 – 상처받은 마음을 감싸주는 진정 향기"),
    "sad": ("슬픔 😢", "화이트 머스크 – 조용하고 중립적인 위로의 향")
}

# 향 추천 함수
def recommend_scents(results):
    recommended = []
    used_labels = set()
    for r in results:
        label = r['label']
        if label not in used_labels and label in scent_map:
            emotion_kor, scent_info = scent_map[label]
            recommended.append(f"🧠 감정: **{emotion_kor}**\n추천 향: {scent_info}")
            used_labels.add(label)
    return "\n\n".join(recommended)

# UI
st.title("🌈 복합 감정 기반 향기 추천기")
st.write("지금 기분을 자유롭게 입력해 주세요. AI가 여러 감정을 분석하고 어울리는 향을 추천해 드릴게요.")

text = st.text_area("예: 오늘은 기쁘면서도 조금 불안하고 당황스러워요...")

if st.button("AI 향기 추천"):
    if text.strip():
        results = sentiment(text)[0]  # top_k=3 결과 반환됨
        scent_output = recommend_scents(results)
        st.success(scent_output)
    else:
        st.warning("먼저 감정을 적어주세요!")