# 3판 「영화관으로 간 생성형 AI 실습」 바이브 코딩 실습 자료

바로 열기: https://yeonu69.github.io/GenerativeAI_HandsOn/v3/

책의 실습은 AI에게 직접 요청해 만드는 것이 먼저이고, 여기 파일은 막혔을 때 비교해 보는 예시 답안입니다.

| 장 | 제목 | 길잡이 | 예시 파일 |
|---|---|---|---|
| 1 | 바이브 코딩이란? | [ch01.html](ch01.html) | `ch01/my-movie.html` |
| 2 | AI에게 요구 사항 말하기 | [ch02.html](ch02.html) | `ch02/요구사항카드.md`, `ch02/byeolbit_v1.html` |
| 3 | 정적 웹페이지: 우리 영화관 소개 | [ch03.html](ch03.html) | `ch03/skeleton.html`, `ch03/index.html` |
| 4 | 움직이는 웹페이지 | [ch04.html](ch04.html) | `ch04/index.html`, `ch04/quiz.html`, `ch04/popcorn.html`, `ch04/broken.html` |
| 5 | 기억하는 웹앱 | [ch05.html](ch05.html) | `ch05/diary.html` |
| 6 | 여러 페이지와 배포 | [ch06.html](ch06.html) | `ch06/byeolbit/index.html`, `ch06/byeolbit/style.css` |
| 7 | 믿을 수 있게 만들기: 환각·버그·테스트 | [ch07.html](ch07.html) | `ch07/fee-buggy.html`, `ch07/fee.html`, `ch07/average.js`, `ch07/average-answer.js` |
| 8 | 시뮬레이터 만들기 | [ch08.html](ch08.html) | `ch08/sir.html`, `ch08/buzz.html`, `ch08/perceptron.html` |
| 9 | 관객 데이터 분석 | [ch09.html](ch09.html) | `ch09/byeolbit2026.csv`, `ch09/analysis.py`, `ch09/weekly_report.py` |
| 10 | 소리와 영상이 있는 웹: 예고편 상영관 | [ch10.html](ch10.html) | `ch10/trailer.html`, `ch10/video/trailer.ko.vtt`, `ch10/샷프롬프트_예시.md` |
| 11 | 서버와 데이터: 예매와 매점 주문 | [ch11.html](ch11.html) | `ch11/booking.html`, `ch11/snack.html`, `ch11/board.html`, `ch11/ranking.html`, `ch11/schema.sql` |
| 12 | AI를 품은 웹앱 | [ch12.html](ch12.html) | `ch12/recommend.html`, `ch12/server-function/recommend.js`, `ch12/테스트질문세트.md` |
| 13 | 세상에 내놓기 전에 | [ch13.html](ch13.html) | `ch13/about.html`, `ch13/종합점검표.md` |
| 14 | 에이전트와 함께 만들기 | [ch14.html](ch14.html) | `ch14/robot-sim/robot.html`, `ch14/robot-sim/tests.html`, `ch14/robot-sim/AGENTS.md`, `ch14/작업지시서.md` |
| 기말 | 「우리 동네 영화관」 | [final.html](final.html) | 6장 사이트 + 13장 점검표 |

## 지켜 둔 원칙
- 모든 데이터·주소·전화번호는 수업용 가상입니다(별빛극장).
- API 키는 어떤 파일에도 없습니다. 12장 서버 함수는 환경 변수 `AI_API_KEY`에서만 읽습니다.
- 11장 예매·주문·랭킹은 브라우저 안의 **연습용 가짜 서버**로 동작합니다. 실제 서비스는 `ch11/schema.sql`로 만듭니다.
- 10장 예고편 영상(mp4)은 저장소에 없습니다. 직접 만든 영상을 `ch10/video/trailer.mp4`로 넣으세요.
- 포스터는 CSS로 그린 예시입니다. 남의 그림·캐릭터·로고를 쓰지 않았습니다.
