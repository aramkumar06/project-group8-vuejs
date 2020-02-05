
1. 영상 테이블에 칼럼 하나 추가
1) 유튜브 카테고리 - youtubeCategory - INT - NULL(foreign Key)


2. 유튜브카테고리 테이블 하나 생성
<스키마>
분류번호 -categoryNumber - INT - NN
한글카테고리 - enCategory - VARCHAR(30) - NN
영어카테고리 - koCategory - VARCHAR(30) - NN


\+ 아래 내용을 테이블에 추가

(분류번호) - (한글카테고리) - (영어카테고리)

1 - 영화/애니메이션 - Film&Animation
2 - 자동차 - Autos&Vehicles
10 - 음악 - Music
15 - 동물 - Pets&Animals
17 - 스포츠 - Sports
19 - 여행/이벤트 - Travel&Events
20 - 게임 - Gaming
22 - 인물/블로그 - People&Blogs
23 - 코미디 - Comedy
24 - 엔터테인먼트 - Entertainment
25 - 뉴스/정치 - News&Politics
26 - 노하우/스타일 - Howto&Style
27 - 교육 - Education
28 - 과학기술 - Science&Technology
29 - 비영리/사회운동 - Nonprofits&Activism