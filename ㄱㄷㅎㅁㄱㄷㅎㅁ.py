import streamlit as st

st.set_page_config(page_title="점프하는 공룡", page_icon="🦖")

st.title("🦖 점프하는 공룡")
st.write("버튼을 누르면 공룡이 점프하며 달립니다!")

if st.button("공룡 출발!"):
    st.balloons()

    st.markdown("""
    <style>
    .stage {
        position: relative;
        width: 100%;
        height: 220px;
        overflow: hidden;
        background: linear-gradient(#87CEEB 75%, #7CFC00 75%);
        border-radius: 10px;
        border: 2px solid #888;
    }

    .ground {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 8px;
        background: green;
    }

    .dino {
        position: absolute;
        left: -80px;
        bottom: 8px;
        font-size: 70px;
        animation:
            run 8s linear forwards,
            jump 0.7s ease-in-out infinite;
    }

    @keyframes run {
        from { left: -80px; }
        to   { left: 105%; }
    }

    @keyframes jump {
        0%, 100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-70px);
        }
    }
    </style>

    <div class="stage">
        <div class="dino">🦖</div>
        <div class="ground"></div>
    </div>
    """, unsafe_allow_html=True)

    st.success("공룡이 점프하며 달리고 있습니다! 🦖")
