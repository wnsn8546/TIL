import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.
    SEARCH_URL = f'https://api.themoviedb.org/3/search/movie?api_key=2493cbf091c3129450beca0dc74b2470&language=ko-KR&query={title}&page=1&include_adult=true'
    response_search = requests.get(SEARCH_URL).json()
    movie_id = ''

    for i in range(0, len(response_search.get('results'))):
        print(response_search.get('results')[i].get('title'))
        if response_search.get('results')[i].get('title') == title:
            
            movie_id = response_search.get('results')[i].get('id')
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/recommendations'
    params = {
        'api_key' : '2493cbf091c3129450beca0dc74b2470',
        'language' : 'ko-KR'
    }

    response = requests.get(BASE_URL + path, params = params).json()
    recommendations = []
    if (movie_id == ''):
        return recommendations
    else:
        for i in range(0, len(response.get('results'))):
            recommendations.append(response.get('results')[i].get('title'))

        return recommendations

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
