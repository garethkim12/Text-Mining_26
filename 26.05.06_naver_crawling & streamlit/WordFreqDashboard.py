import os
import streamlit as st
import mylib.myTextAnalyzer as ta  
import mylib.myStreamlitVisualizer as sv
from konlpy.tag import Okt

os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-17'

st.title("다음 영화 리뷰 빈도수 분석")
datafile = r"C:\Users\user\Desktop\textmine_26\apps\WordFreqProj\data\daum_movie_review.csv"

# 1. 데이터 준비
corpus = ta.load_corpus(datafile, 'review')

# 2. 빈도수 분석
counter = ta.count_word_freq(corpus)

# 3. 시각화 출력
st.subheader("막대 그래프")
sv.visualize_barh_grapyh(counter, 20)

st.subheader("워드클라우드")
sv.visualize_wordcloud(counter, 50)