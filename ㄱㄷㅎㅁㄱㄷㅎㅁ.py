import streamlit as st

st.set_page_config(page_title="공룡 버튼", page_icon="🦖")

st.title("🦖 공룡 등장!")
st.write("아래 버튼을 눌러보세요!")

if st.button("공룡 소환하기"):
    st.balloons()
    st.markdown(
        """
        # 🦖
        ## 안녕! 나는 공룡이야!
        """
    )
    st.success("공룡이 나타났습니다!")
