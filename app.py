import streamlit as st

# 감정 키워드별 향 매핑 데이터
scent_categories = {
    "스트레스 완화 및 진정": {
        "keywords": ["스트레스", "불안", "긴장", "짜증", "힘듦", "지침","힘들고","짜증나고","민감해","민감"],
        "scents": ["라벤더", "일랑일랑", "화이트자스민 & 민트", "히노끼"],
        "effect": "불안과 스트레스를 해소하고 감정의 균형을 맞추는 데 도움을 줘요."
    },
    "기분 전환 및 활력 증진": {
        "keywords": ["우울", "기분 전환", "기쁘다", "상쾌함", "에너지", "활기","우울해","우울하고","행복","행복해","행복하고","상쾌해"],
        "scents": ["헤스페리데스 자몽", "프리지아", "화이트머스크"],
        "effect": "기분을 상쾌하게 만들어 활력을 주고 우울감을 해소하는 데 효과적이에요."
    },
    "정신적 집중 및 피로 회복": {
        "keywords": ["집중", "피곤", "피로", "무기력", "멍함", "졸림","졸려","졸리고","지침","지쳤어","지쳤음","슬픔","슬퍼","슬픈","공허해","공허함","공허"],
        "scents": ["로즈마리가든", "자몽"],
        "effect": "집중력을 높이고 피로를 해소해 머리를 맑게 해줘요."
    },
    "청량감 및 상쾌함": {
        "keywords": ["답답", "상쾌", "혼란", "복잡", "리프레시", "환기","답답해","답답하고","안좋음"],
        "scents": ["클린웜코튼", "화이트자스민 & 민트"],
        "effect": "신선한 향이 마음을 정리하고 기분을 환기시켜줘요."
    },
    "감정적 안정 및 균형": {
        "keywords": ["혼란", "감정 기복", "불안정", "슬픔", "마음의 평화", "고요함","초조함","초조해","초초한 것 같아"],
        "scents": ["떼누아29", "일랑일랑", "화이트머스크"],
        "effect": "감정을 차분하게 해주고 정서적인 안정을 도와줘요."
    }
}

# 감정 키워드 매칭 함수
def match_emotion_to_scent(user_input):
    result = []
    lowered_input = user_input.lower()
    
    for category, data in scent_categories.items():
        for keyword in data["keywords"]:
            if keyword in lowered_input:
                result.append((category, data["scents"], data["effect"]))
                break  # 한 번 매칭되면 중복 피하기 위해 break
    
    return result

# Streamlit 앱 UI
st.title("🌿 기분에 따라 향기 추천해드려요!")
st.write("현재 느끼는 기분이나 상태를 입력하면, 그에 맞는 향을 추천해드릴게요.")

user_input = st.text_area("예: 요즘 스트레스를 많이 받고 피곤해요. 상쾌함이 필요해요!")

if st.button("향 추천 받기"):
    if user_input.strip():
        matches = match_emotion_to_scent(user_input)
        if matches:
            st.success("💡 추천 결과:")
            for category, scents, effect in matches:
                scent_list = ", ".join(scents)
                st.markdown(f"**🧘 {category}**\n\n- 향기 추천: `{scent_list}`\n- 효과: {effect}\n")
        else:
            st.warning("해석 가능한 감정 키워드가 없어요. 좀 더 구체적으로 입력해 주세요!")
    else:
        st.warning("먼저 감정을 입력해 주세요.")
