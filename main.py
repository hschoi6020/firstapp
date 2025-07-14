import streamlit as st

# MBTI별 추천 직업 데이터
mbti_jobs = {
    "INTJ": ["전략 기획가", "데이터 과학자", "연구원"],
    "INTP": ["이론 물리학자", "프로그래머", "기술 컨설턴트"],
    "ENTJ": ["경영 컨설턴트", "CEO", "프로젝트 매니저"],
    "ENTP": ["벤처 창업가", "마케팅 전문가", "기술 개발자"],
    "INFJ": ["상담사", "심리학자", "작가"],
    "INFP": ["시인", "예술가", "사회복지사"],
    "ENFJ": ["교사", "인사 관리자", "멘토"],
    "ENFP": ["광고 기획자", "방송인", "여행 작가"],
    "ISTJ": ["회계사", "공무원", "법률 전문가"],
    "ISFJ": ["간호사", "교사", "사회복지사"],
    "ESTJ": ["군인", "경영자", "은행원"],
    "ESFJ": ["행사 기획자", "간호사", "서비스 관리자"],
    "ISTP": ["엔지니어", "정비사", "파일럿"],
    "ISFP": ["디자이너", "요리사", "사진작가"],
    "ESTP": ["영업 사원", "응급 구조사", "모험 여행 가이드"],
    "ESFP": ["연예인", "MC", "홍보 전문가"]
}

st.title("MBTI 기반 직업 추천기")
st.write("당신의 MBTI 유형을 선택하면, 적합한 직업 3개를 추천해 드립니다.")

# MBTI 선택
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

# 버튼을 누르면 결과 출력
if st.button("직업 추천 받기"):
    recommended_jobs = mbti_jobs[selected_mbti]
    st.subheader(f"✅ {selected_mbti} 유형에 적합한 직업")
    for i, job in enumerate(recommended_jobs, 1):
        st.write(f"{i}. {job}")
