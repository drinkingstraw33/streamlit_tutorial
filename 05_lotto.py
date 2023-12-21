import random as random
import streamlit as st
import datetime

def generate_lotto():
    numbers = [i for i in range(1, 46)]
    dc_num = map(str, sorted(random.sample(numbers, k=6)))
    return ', '.join(dc_num)

st.title(":hatched_chick: 로또 생성기 :hatched_chick:")

lotto_button = st.button("로또를 생성해 주세요!")
if lotto_button:
    for i in range(1, 6):
        numbers = [i for i in range(1, 46)]
        st.subheader(f"{i}번째 당첨 번호는 :green[{generate_lotto()}]입니다!")
    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")