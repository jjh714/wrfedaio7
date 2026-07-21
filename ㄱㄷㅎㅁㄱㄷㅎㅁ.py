import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.title("📐 방정식 계산기")

x, y = sp.symbols("x y")


# 보기 메뉴
example = st.selectbox(
    "예시 방정식 선택",
    [
        "직접 입력",
        "일차함수 y=2*x+1",
        "이차함수 y=x**2",
        "로그함수 y=log(x)",
        "원의 방정식 (x-2)^2+(y-1)^2=9"
    ]
)


# 예시 자동 입력
if example == "일차함수 y=2*x+1":
    equation = "y=2*x+1"

elif example == "이차함수 y=x**2":
    equation = "y=x**2"

elif example == "로그함수 y=log(x)":
    equation = "y=log(x)"

elif example == "원의 방정식 (x-2)^2+(y-1)^2=9":
    equation = "(x-2)^2+(y-1)^2=9"

else:
    equation = ""


equation = st.text_input(
    "방정식 입력 (x와 y만 사용 가능)",
    equation
)


# 허용 문자 검사
allowed = "xy0123456789+-*/^=().log"

if equation:
    for c in equation.replace(" ", ""):
        if c not in allowed:
            st.error("❌ x와 y를 제외한 문자는 사용할 수 없습니다.")
            st.stop()


# 값 입력
x_value = st.number_input("x 값 입력", value=1.0)


if st.button("계산하기"):

    try:
        # y=f(x) 형태
        if "=" in equation:

            left, right = equation.split("=")

            if left.strip() == "y":

                expr = sp.sympify(
                    right.replace("^", "**")
                )

                result = expr.subs(x, x_value)

                st.success(
                    f"x={x_value}일 때 y={result}"
                )


                # 그래프
                f = sp.lambdify(x, expr, "numpy")

                xs = np.linspace(-10,10,400)
                ys = f(xs)

                fig, ax = plt.subplots()
                ax.plot(xs,ys)
                ax.grid()

                ax.set_xlabel("x")
                ax.set_ylabel("y")

                st.pyplot(fig)


            else:
                st.info(
                    "현재 버전은 y=f(x) 형태를 지원합니다."
                )


        else:
            st.error("= 기호가 필요합니다.")


    except Exception as e:
        st.error(
            "방정식을 해석할 수 없습니다."
        )
