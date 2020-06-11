import pandas as pd

# 샘플 데이터프레임 생성
inventors = pd.DataFrame({
    'name': ['Nikola Tesla', 'Thomas Edison', 'Henry Ford'],
    'born': ['1856/07/10', '1847/02/11', '1863/07/30'],
    'died': ['1943/01/07', '1931/10/18', '1947/04/07'],
    'age': [86, 84, 83]
})

# 매개 변수로 저장할 파일 이름을 전달합니다.
# inventors.to_excel('inventors1.xlsx')

# 이제 인덱스는 저장되지 않습니다.
# inventors.to_excel('inventors2.xlsx', index=False)
inventors.to_excel('inventors3.xls', index=False)
