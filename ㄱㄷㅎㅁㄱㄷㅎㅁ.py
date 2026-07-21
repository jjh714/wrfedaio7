import streamlit as st

st.set_page_config(page_title="움직이는 공룡", page_icon="🦖")

st.title("🦖 움직이는 공룡")

st.write("버튼을 누르면 공룡이 달립니다!")

if st.button("공룡 출발!"):
    st.balloons()

    st.markdown("""
    <style>
    .ground {
        position: relative;
        width: 100%;
        height: 150px;
        border-bottom: 4px solid green;
        overflow: hidden;
    }

    .dino {
        position: absolute;
        font-size: 70px;
        left: -100px;
        bottom: 10px;
        animation: run 5s linear forwards;
    }

    @keyframes run {
        from {
            left: -100px;
        }
        to {
            left: 100%;
        }
    }
    </style>

    <div class="ground">
        <div class="dino">🦖</div>
    </div>
    """, unsafe_allow_html=True)

    st.success("공룡이 달리고 있습니다! 🦖")
