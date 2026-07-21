import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="숲속의 동물 인연",
    page_icon="🐾"
)

# 게임 데이터
animals = [
    {
        "name": "늑대 루루 🐺",
        "image": "🐺",
        "story": "깊은 숲에서 길을 잃은 당신 앞에 늑대 루루가 나타났다."
    },
    {
        "name": "고양이 나나 🐱",
        "image": "🐱",
        "story": "작은 고양이 나나가 당신의 곁으로 다가왔다."
    },
    {
        "name": "여우 코코 🦊",
        "image": "🦊",
        "story": "신비로운 여우 코코가 숲의 비밀을 알려준다."
    }
]


# 초기 상태
if "love" not in st.session_state:
    st.session_state.love = 0

if "day" not in st.session_state:
    st.session_state.day = 0

if "animal" not in st.session_state:
    st.session_state.animal = 0

if "ending" not in st.session_state:
    st.session_state.ending = ""


# 제목
st.title("🌲 숲속의 동물 인연 🌲")
st.write("동물 친구와 친해져 최고의 엔딩을 만들어 보세요!")


animal = animals[st.session_state.animal]


# 캐릭터 표시
st.markdown(
    f"""
    <div style="text-align:center;font-size:100px;">
    {animal["image"]}
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader(animal["name"])
st.write(animal["story"])


# 상태 표시
st.info(
    f"❤️ 호감도 : {st.session_state.love}\n\n"
    f"📅 만남 횟수 : {st.session_state.day}"
)


# 엔딩 전 선택지
if st.session_state.ending == "":

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🍎 먹이 주기"):
            st.session_state.love += 3
            st.session_state.day += 1

    with col2:
        if st.button("🎵 노래 불러주기"):
            st.session_state.love += 2
            st.session_state.day += 1

    with col3:
        if st.button("🏃 도망가기"):
            st.session_state.love -= 2
            st.session_state.day += 1


    # 캐릭터 변경
    if st.session_state.day == 1:
        st.session_state.animal = 1

    elif st.session_state.day == 2:
        st.session_state.animal = 2


    # 엔딩 판정
    if st.session_state.day >= 3:

        if st.session_state.love >= 8:
            st.session_state.ending = (
                "💚 해피 엔딩!\n\n"
                "동물 친구와 평생 함께하게 되었다!"
            )

        elif st.session_state.love >= 3:
            st.session_state.ending = (
                "🙂 친구 엔딩!\n\n"
                "숲속에서 계속 만나는 좋은 친구가 되었다."
            )

        else:
            st.session_state.ending = (
                "💔 배드 엔딩...\n\n"
                "동물 친구는 조용히 숲으로 돌아갔다."
            )


# 엔딩 출력
else:

    st.success(st.session_state.ending)

    if st.button("🔄 다시 시작"):
        st.session_state.love = 0
        st.session_state.day = 0
        st.session_state.animal = 0
        st.session_state.ending = ""
        st.rerun()
