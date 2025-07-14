import streamlit as st
import plotly.graph_objects as go

# 예시: 포켓몬 인기 순위 Top 10 (가상의 순위)
pokemon_names = [
    "피카츄", "뮤츠", "이브이", "리자몽", "루기아",
    "꼬부기", "파이리", "뮤", "야도란", "라이츄"
]

popularity_scores = [98, 94, 93, 91, 89, 87, 85, 83, 80, 78]

# 제목
st.title("🔥 포켓몬 인기 순위 TOP 10")

# Plotly 막대그래프 생성
fig = go.Figure(data=[
    go.Bar(
        x=pokemon_names,
        y=popularity_scores,
        marker_color='rgb(255, 204, 102)',  # 포켓몬 느낌의 노란빛
        text=popularity_scores,
        textposition='outside'
    )
])

# 레이아웃 설정
fig.update_layout(
    title="포켓몬 인기 순위",
    xaxis_title="포켓몬 이름",
    yaxis_title="인기도 점수",
    yaxis=dict(range=[0, 100]),
    template="simple_white"
)

# Streamlit에 그래프 표시
st.plotly_chart(fig)
