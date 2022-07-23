// [12922] 수박수박수박수박수박수?

function solution(n) {
  let answer = "";
  for (let i = 0; i < n; i++) {
    answer += i % 2 === 0 ? "수" : "박";
  }
  return answer;
}
function solution(n) {
  return "수박".repeat(n).substring(0, n);
}

// repeat() 메서드는 문자열을 주어진 횟수만큼 반복해 붙인 새로운 문자열을 반환합니다.
// substring() 메소드는 string 객체의 시작 인덱스로 부터 종료 인덱스 전 까지 문자열의 부분 문자열을 반환합니다.
