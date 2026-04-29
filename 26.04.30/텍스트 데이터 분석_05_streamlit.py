import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
from wordcloud import WordCloud


st.title("Hello, Streamlit World")\

name = "GeunHa"

st.title(f"hello, {name}~~~~~ Welcome to Streamlit World!!!")

df = pd.DataFrame({
    'A': [1,2,3,4],

    'B': [10,20,30,40]
})


# 실습 내용 중 time 함수를 사용 하여 문구 변화 인터페이스 구현
@st.cache_data
def change_text():
    text = st.title('텍스트 변할 겁니다')
    time.sleep(2) 
    text.info('2초가 지났습니다.')

change_text()
# st.columns(2)를 사용하여 화면 가로 영역을 2개의 칸(열)으로 분할
col1, col2 = st.columns(2)

# 첫 번째 열(왼쪽) 영역 설정
with col1:
    st.subheader("버튼 및 선택 위젯")
    
    # 1. st.button: 클릭 시 True를 반환, 아니면 False
    # 클릭하는 순간에만 아래 success 메시지가 나타납니다.
    if st.button('버튼'):
        st.success('clicked button') # 초록색 성공 알림창 표시

    st.button('Go to gallery')

    # 2. st.radio: 여러 옵션 중 하나만 선택 가능
    # 사용자가 선택한 항목의 텍스트(예: '신경망')가 ml_method 변수에 저장됩니다.[cite: 1]
    ml_method = st.radio(
        "머신러닝 방법",
        ('신경망', '랜덤포레스트', 'SVM')
    )
    # 선택된 결과를 파란색 정보창에 실시간으로 표시
    st.info(f"나의 선택 : {ml_method}")

    # 3. st.checkbox: 체크 여부를 True/False로 반환[cite: 1]
    is_tokenized = st.checkbox('토큰화')
    if is_tokenized:
        st.write("토큰화가 활성화되었습니다.")
# ================================================================================================================
# 두 번째 열(오른쪽) 영역 설정
with col2:
    st.subheader("리스트 및 수치 위젯")

    # 4. st.selectbox: 드롭다운 형태의 단일 선택 메뉴[cite: 1]
    # 리스트 중에서 하나를 선택하면 그 값이 sb_method에 할당됩니다.[cite: 1]
    sb_method = st.selectbox(
        "머신러닝 방법 선택(단일)",
        ['SVM', '랜덤포레스트', '신경망'],
        key='sb' # 위젯의 고유 키 (중복 방지용)
    )
    st.write(f"선택된 방법: {sb_method}")

    # 5. st.multiselect: 여러 개를 동시에 선택할 수 있는 위젯[cite: 1]
    # 결과값은 선택된 항목들의 '리스트(List)' 형태로 반환됩니다.[cite: 1]
    ms_methods = st.multiselect(
        "머신러닝 방법 선택(다중)",
        ['랜덤포레스트', '신경망', 'SVM'],
        default=['랜덤포레스트', '신경망'] # 앱 시작 시 기본으로 선택되어 있을 항목들
    )
    st.write(f"선택된 리스트: {ms_methods}")

    # 6. st.slider: 숫자를 드래그하여 선택[cite: 1]
    # 인자 순서: (라벨, 최소값, 최대값, 기본값)[cite: 1]
    weight = st.slider('가중치', 0, 10, 5)
    st.warning(f"가중치 : {weight}") # 주황색 경고 스타일 알림창 표시

    # 7. st.text_input & st.number_input: 문자열과 숫자 직접 입력[cite: 1]
    # 입력한 값이 즉시 변수에 저장되어 프로그램에서 활용 가능합니다.[cite: 1]
    user_text = st.text_input("메시지를 입력하세요")
    user_number = st.number_input("숫자를 입력하세요", value=0)
# ================================================================================================================
# 8. st.form을 사용하여 입력창들을 그룹화합니다.
# 이미지와 같이 테두리가 있는 박스 형태가 자동으로 생성됩니다.
with st.form(key='user_input_form'):
    st.subheader("사용자 입력 폼")
    
    # 이름 입력: st.text_input
    name = st.text_input("이름")
    
    # 나이 입력: st.number_input (기본값 1 설정)
    age = st.number_input("나이", min_value=1, value=1)
    
    # 약관 동의: st.checkbox
    agreement = st.checkbox("약관에 동의합니다")
    
    # 제출 버튼: st.form_submit_button
    submitted = st.form_submit_button(label='제출')

# 9. 버튼을 눌렀을 때만 결과가 화면에 나타나도록 설정합니다.
if submitted:
    # 이름과 나이를 한 줄에 출력
    st.write(f"이름: {name}, 나이: {age}")
    
    # 약관 동의 여부에 따른 메시지 출력
    if agreement:
        st.success("약관에 동의했습니다.")
    else:
        st.error("약관에 동의하지 않았습니다.")
# ================================================================================================================
#사이드바 영역 설정
with st.sidebar:
    st.title('설정') #사이드바 제목

    #사이드바 안에 폼 생성
    with st.form("sidebar_form"):
        #이름 입력 칸
        st.text_input("이름을 입력하세요")
        # 나이 슬라이더 
        age = st.slider("나이", 0, 120, 32)

        # 색상 선택 드롭다운
        color = st.selectbox("좋아하는 색상을 선택하세요", ["빨강","파랑","초록","노랑", "금색", "검정"])

        #폼 제출 버튼 (FORM 사용 시 필수)
        submitted = st.form_submit_button("적용")

#메인 화면 출력 결과
if submitted:
    st.write(f"### 입력 결과")
    st.write(f"이름 {name}")
    st.write(f"나이 {age}")
    st.write(f"선택한 색상 {color}")

# ================================================================================================================

# 1. 샘플 데이터 준비
data = {
    'Python': 50,
    'Streamlit': 45,
    'Data': 30,
    'Visualization': 35,
    'Analysis': 25,
    'Machine Learning': 40
}
df = pd.Series(data)

st.title("텍스트 데이터 분석 시각화")

# 사이드바에서 시각화 종류 선택
view_type = st.sidebar.radio("시각화 선택", ["가로 막대 그래프", "워드클라우드"])

if view_type == "가로 막대 그래프":
    st.subheader("단어 빈도수 - Bar Chart")
    
    # --- 이미지의 Matplotlib 구조 적용 ---
    # 1. 도화지(fig)와 축(ax) 생성
    fig, ax = plt.subplots()
    
    # 2. matplotlib 명령어로 그래프 그리기 (가로 막대)
    ax.barh(df.index, df.values, color='skyblue')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Keywords')
    
    # 3. 스트림릿에 그래프 출력
    st.pyplot(fig)

elif view_type == "워드클라우드":
    st.subheader("주요 키워드 - Wordcloud")
    
    # 워드클라우드 객체 생성 및 데이터 생성
    wc = WordCloud(background_color="white", width=800, height=400).generate_from_frequencies(data)
    
    # --- Matplotlib 구조를 사용하여 출력 ---
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation='bilinear')
    ax.axis("off") # 축 숨기기
    
    # 스트림릿에 출력[cite: 1]
    st.pyplot(fig)
