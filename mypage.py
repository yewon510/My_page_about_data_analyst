import streamlit as st

st.set_page_config(page_title='yewon project', layout = 'wide', initial_sidebar_state='expanded', menu_items={'Get help': 'https://docs.streamlit.io', 'About': '# 이것은 헤더. \n - 마크다운 문법 지원 \n - [네이버](https://naver.com)'})

st.title('# 데이터 애널리스트를 소개합니다 :)')

st.sidebar.success('위의 목록에서 Demo를 선택해주세요')

st.markdown(
    '''
    **데이터 애널리스트에 대해 알아봅시다. 
    **왼쪽의 사이드바에서 원하는 데모를 선택해주세요
    
    ### 데이터 애널리스트 채용 공고를 확인해 보세요
    - [카카오페이] (https://kakaopay.career.greetinghr.com/o/112078)
    
    ### 수료증 이수 과정을 확인해 보세요
    - [구글 이수 과정] (https://grow.google/intl/ko_kr/data-analytics-certified-course/)
    '''
)

page = st.sidebar.selectbox('페이지 선택', ['필요한 역량', '직종 별 연봉'])

if page == '필요한 역량':
    st.title('필요한 역량')
    st.markdown(
    ''' 
    # 데이터 애널리스트란?
    # 데이터 애널리스트는 조직이 더 나은 비즈니스 의사결정을 할 수 있도록 데이터를 사용해 돕는 역할을 한다. 이들은 비즈니스 성과를 예측하고 개선하고자 컴퓨터 프로그래밍, 수학, 통계 등의 기법들을 사용해 데이터로부터 결론을 이끌어낸다.
    # 데이터 애널리스트는 주로 조직이 보유한 정형 데이터를 처리한다. 고객, 비즈니스 프로세스, 경제와 관련된 데이터를 바탕으로 보고서, 대시보드 생성, 시각화 작업 등을 수행한다. 나아가 시니어 매니저들과 경영진에게 인사이트를 전달해 의사결정 과정을 돕는다. 
    # 또한 데이터 애널리스트는 재고, 물류, 운송 비용, 시장 조사, 이윤, 매출 등 다양한 유형의 데이터를 취급한다. 이들은 이 데이터를 활용해 기업의 시장 점유율 예측, 제품 가격 책정, 판매 시기 조율, 운송 비용 최적화 등의 작업을 할 수 있도록 도움을 준다. 
    # '''
    )

else:
    import pandas as pd
    st.header('# ANNUAL INCOME')
    df = pd.DataFrame({'position' : ['애널리틱스 매니저', '비즈니스 애널리스트', '데이터 아키텍트'], 'income' : ['96,396$', '61,091$', '119,242$']})
    st.dataframe(df)