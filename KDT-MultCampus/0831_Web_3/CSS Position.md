# CSS Position

- 문서 상에서 요소의 위치를 지정
- static : 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
  1. relative : 상대 위치
     - 자기 자신의 static 위치를 기준으로 이동 ( normal flow 유지)
  2. absolute : 절대 위치
     - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
     - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 브라우저 화면 기준으로 이동)
  3. fixed : 고정 위치
     - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
     - 부모 요소와 관계없이 viewport를 기준으로 이동
       - 스크롤 시에도 항상 같은 곳에 위치함
  4. sticky : 스크롤에 따라 static -> fixed로 변경
     - 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성

## Flex

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축
  - main axis (메인 축)
  - cross axis (교차 축)
- 구성 요소
  - Flex Container (부모요소)
  - Flex Item (자식 요소)

Flex Container (부모 요소)

- flexbox 레이아웃을 형성하는 가장 기본적인 모델
- Flex Item들이 놓여있는 영역
- display  속성을 flex 혹은 inline-flex로 지정

Flex Item (자식 요소)

- 컨테이너에 속해 있는 컨텐츠(박스)

### Flex 속성

- 배치 설정
  - flex-direction
  - flex-wrap
- 공간 나누기
  - justify-content (main axis)
  - align-content (cross axis)
- 정렬
  - align-items (모든 아이템을 cross axis 기준으로)
  - align-self (개별 아이템)