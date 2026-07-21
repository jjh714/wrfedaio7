import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import re


st.title("📐 방정식 계산기")


st.warning(
    "⚠️ 현재 버전은 y=f(x) 형태의 방정식만 지원합니다.\n\n"
    "예시: y=2*x+1, y=3cos(x), y=log(x)"
)


# 초기값 저장
if "equation" not in st.session_state:
    st.session_state.equation = ""

if "x_value" not in st.session_state:
    st.session_state.x_value = 1.0



x, y = sp.symbols("x y")



# 보기 목록
example = st.selectbox(
    "예시 방정식 선택",
    [
        "직접 입력",
        "일차함수 y=2*x+1",
        "이차함수 y=x^2",
        "삼차함수 y=x^3",
        "절댓값 함수 y=abs(x)",
        "루트 함수 y=sqrt(x)",
        "로그함수 y=log(x)",
        "지수함수 y=2^x",
        "사인 함수 y=sin(x)",
        "코사인 함수 y=cos(x)",
        "탄젠트 함수 y=tan(x)",
        "역비례 함수 y=1/x",
        "삼각함수 계수 예시 y=3*cos(x)"
    ]
)



# 보기 선택 시 자동 입력
if example == "일차함수 y=2*x+1":
    equation = "y=2*x+1"

elif example == "이차함수 y=x^2":
    equation = "y=x^2"

elif example == "삼차함수 y=x^3":
    equation = "y=x^3"

elif example == "절댓값 함수 y=abs(x)":
    equation = "y=abs(x)"

elif example == "루트 함수 y=sqrt(x)":
    equation = "y=sqrt(x)"

elif example == "로그함수 y=log(x)":
    equation = "y=log(x)"

elif example == "지수함수 y=2^x":
    equation = "y=2^x"

elif example == "사인 함수 y=sin(x)":
    equation = "y=sin(x)"

elif example == "코사인 함수 y=cos(x)":
    equation = "y=cos(x)"

elif example == "탄젠트 함수 y=tan(x)":
    equation = "y=tan(x)"

elif example == "역비례 함수 y=1/x":
    equation = "y=1/x"

elif example == "삼각함수 계수 예시 y=3*cos(x)":
    equation = "y=3*cos(x)"

else:
    equation = ""



# 입력창
equation = st.text_input(
    "방정식 입력 (y=f(x) 형태)",
    equation,
    key="equation"
)



# 허용 문자 검사
allowed = "xy0123456789+-*/^=().logsincoqrtab"



if equation:

    for c in equation.replace(" ", ""):

        if c not in allowed:
            st.error(
                "❌ 사용할 수 없는 문자가 있습니다."
            )
            st.stop()



# x 입력
x_value = st.number_input(
    "대입할 x 값",
    value=1.0,
    key="x_value"
)



# 버튼 배치
col1, col2 = st.columns(2)



with col1:

    calculate = st.button("🧮 계산하기")


with col2:

    reset = st.button("🔄 초기화")



# 초기화
if reset:

    st.session_state.equation = ""
    st.session_state.x_value = 1.0

    st.rerun()



# 계산
if calculate:

    try:

        if "=" not in equation:

            st.error(
                "❌ = 기호가 필요합니다."
            )
            st.stop()



        left, right = equation.split("=")



        if left.strip() != "y":

            st.error(
                "❌ 현재 버전은 y=f(x) 형태만 지원합니다."
            )
            st.stop()



        # ^ 변환
        right = right.replace("^", "**")


        # 3cos(x) -> 3*cos(x)
        right = re.sub(
            r"(\d)([a-zA-Z])",
            r"\1*\2",
            right
        )



        expr = sp.sympify(
            right,
            locals={
                "sin": sp.sin,
                "cos": sp.cos,
                "tan": sp.tan,
                "log": sp.log,
                "sqrt": sp.sqrt,
                "abs": sp.Abs
            }
        )



        result = expr.subs(
            x,
            x_value
        )



        st.success(
            f"x={x_value} 일 때 y={result}"
        )



        # 그래프
        func = sp.lambdify(
            x,
            expr,
            "numpy"
        )


        xs = np.linspace(
            -10,
            10,
            500
        )


        ys = func(xs)



        fig, ax = plt.subplots()


        ax.plot(
            xs,
            ys,
            label=equation,
            color="blue"
        )


        ax.scatter(
            [x_value],
            [float(result)],
            color="red",
            label="현재 위치"
        )


        ax.legend()

        ax.grid()

        ax.set_xlabel("x")
        ax.set_ylabel("y")


        st.pyplot(fig)



    except Exception as e:

        st.error(
            "❌ 방정식을 계산할 수 없습니다."
        )
