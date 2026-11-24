// 버그 찾기 대회: 평균 별점과 최근 기록 (버그 3개)
// 힌트: 시작 번호, 빈 목록, 정렬 방향
function averageStars(records) {
  let sum = 0;
  for (let i = 1; i < records.length; i++) {
    sum = sum + records[i].stars;
  }
  return sum / records.length;
}

function latestFirst(records) {
  // 날짜가 최근인 기록이 앞에 오게
  return records.sort((a, b) => a.date > b.date ? 1 : -1);
}
