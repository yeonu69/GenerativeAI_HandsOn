// 정답 예시
function averageStars(records) {
  if (records.length === 0) return null;          // 버그 2: 빈 목록이면 0÷0 = NaN
  let sum = 0;
  for (let i = 0; i < records.length; i++) {      // 버그 1: 0번부터 세야 첫 기록이 빠지지 않음
    sum = sum + records[i].stars;
  }
  return sum / records.length;
}

function latestFirst(records) {
  // 버그 3: 최근이 앞에 오려면 큰 날짜가 앞(내림차순). 원본 배열을 바꾸지 않게 복사해서 정렬
  return [...records].sort((a, b) => b.date.localeCompare(a.date));
}

// 테스트
const t = [{stars: 5, date: "2027-03-14"}, {stars: 3, date: "2027-10-01"}, {stars: 4, date: "2027-09-30"}];
console.assert(averageStars([]) === null, "빈 목록");
console.assert(averageStars([{stars: 5}]) === 5, "한 건");
console.assert(averageStars(t) === 4, "세 건");
console.assert(latestFirst(t)[0].date === "2027-10-01", "최근이 앞");
console.log("테스트 끝(실패가 없으면 아무 경고도 나오지 않습니다)");
