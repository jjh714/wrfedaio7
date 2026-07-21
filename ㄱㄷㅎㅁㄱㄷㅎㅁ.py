import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


st.title("📐 방정식 계산기")

# 경고 문구
st.warning(
    "⚠️ 현재 버전은 y=f(x) 형태의 방정식만 지원합니다.\n\n"
    "예시: y=2*x+1, y=x^2, y=log(x)"
)


x, y = sp.symbols("x y")


# 예시 선택
example = st.selectbox(
    "예시 방정식 선택",
    [
        "직접 입력",
        "일차함수 y=2*x+1",
        "이차함수 y=x**2",
        "로그함수 y=log(x)"
    ]
)


# 선택한 예시 입력
if example == "일차함수 y=2*x+1":
    equation = "y=2*x+1"

elif example == "이차함수 y=x**2":
    equation = "y=x**2"

elif example == "로그함수 y=log(x)":
    equation = "y=log(x)"

else:
    equation = ""


# 직접 입력창
equation = st.text_input(
    "방정식 입력 (y=f(x) 형태)",
    equation
)


# 입력 검사
allowed = "xy0123456789+-*/^=().log"


if equation:

    for c in equation.replace(" ", ""):

        if c not in allowed:
            st.error(
                "❌ 사용할 수 없는 문자가 있습니다. "
                "x, y와 기본 수식만 입력하세요."
            )
            st.stop()



# x 값 입력
x_value = st.number_input(
    "대입할 x 값",
    value=1.0
)



# 계산 버튼
if st.button("계산하기"):

    try:

        if "=" not in equation:
            st.error(
                "❌ = 기호가 필요합니다."
            )
            st.stop()


        left, right = equation.split("=")


        # y=f(x) 확인
        if left.strip() != "y":

            st.error(
                "❌ 현재 버전은 y=f(x) 형태만 지원합니다."
            )
            st.stop()


        # 식 변환
        expr = sp.sympify(
            right.replace("^", "**")
        )


        # 결과 계산
        result = expr.subs(
            x,
            x_value
        )


        st.success(
            f"x={x_value} 일 때 y={result}"
        )


        # 그래프
        f = sp.lambdify(
            x,
            expr,
            "numpy"
        )


        xs = np.linspace(
            -10,
            10,
            400
        )


        ys = f(xs)


        fig, ax = plt.subplots()

        ax.plot(
            xs,
            ys,
            color="blue"
        )


        ax.scatter(
            [x_value],
            [float(result)],
            color="red"
        )


        ax.set_xlabel("x")
        ax.set_ylabel("y")

        ax.grid()


        st.pyplot(fig)


    except Exception:

        st.error(
            "❌ 방정식을 해석할 수 없습니다."
        )
