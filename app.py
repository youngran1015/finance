import FinanceDataReader as fdr
import streamlit as st
import datetime

with st.sidebar :
    date = st.date_input("조회 시작일을 선택해 주세요.",datetime.datetime(2024,1,1))
    code = st.text_input('종목코드', value='',placeholder='종목코드를 입력해 주세요')
#둘다 네이터가 들어와야 가능함(날짜와 종목코드가 들어오면)
if code and date : 
    df = fdr.DataReader(code,date)
    data = df.sort_index(ascending=True).loc[:,'Close']
    tab1, tab2 = st.tabs(['차트','데이터'])

    with tab1 :
        st.line_chart(data)
    with tab2 :
        st.dataframe(df.sort_index(ascending=False))
    with st.expander('컬럼설명') :
        st.markdown('''
                    - open :시가
                    - high :고가
                    - low :저가
                    - Close :종가
                    - Adj Close :수정 종가
                    - Volumn : 거래량 ''')