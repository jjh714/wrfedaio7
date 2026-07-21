import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


st.title("📐 방정식 계산기")


st.warning(
    "⚠️ 현재 버전은 y=f(x) 형태의 방정식만 지원합니다.\n\n"
    "예시: y=2*x+1, y=x^2, y=log(x), y=sin(x)"
)


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
        "역비례 함수 y=1/x"
    ]
)


# 선택한 방정식 자동 입력
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

elif example == "역비례 함수 y=1/x":
    equation = "y=1/x"

else:
    equation = ""


# 입력창
equation = st.text_input(
    "방정식 입력 (y=f(x) 형태)",
    equation
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



# x 값 입력
x_value = st.number_input(
    "대입할 x 값",
    value=1.0
)



if st.button("계산하기"):

    try:

        if "=" not in equation:
            st.error(
                "❌ = 기호를 입력하세요."
            )
            st.stop()


        left, right = equation.split("=")


        # y=f(x)만 지원
        if left.strip() != "y":

            st.error(
                "❌ 현재 버전은 y=f(x) 형태만 지원합니다."
            )
            st.stop()


        # 수식 변환
        expr = sp.sympify(
            right.replace("^", "**")
        )


        # 값 계산
        result = expr.subs(
            x,
            x_value
        )


        st.success(
            f"x={x_value} 일 때 y={result}"
        )


        # 그래프 생성
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
            color="blue",
            label=equation
        )


        ax.scatter(
            [x_value],
            [float(result)],
            color="red",
            label="현재 위치"
        )


        ax.legend()

        ax.set_xlabel("x")
        ax.set_ylabel("y")

        ax.grid()


        st.pyplot(fig)


    except Exception:

        st.error(
            "❌ 방정식을 계산할 수 없습니다."
        )
