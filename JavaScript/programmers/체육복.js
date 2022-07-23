// [42862] 체육복
function solution(n, lost, reserve) {
  let answer = 0;
  let have = new Array(n).fill(1); // n만큼 1로 채워서 초기화
  for (let i = 0; i < lost.length; i++) {
    have[lost[i] - 1]--;
    // 잃어버린 것에 -1을 해서 0을 만든다
  }
  for (let i = 0; i < reserve.length; i++) {
    have[reserve[i] - 1]++;
  } // 여벌이 있다면 +1을 해서 2를 만든다
  for (let i = 0; i < have.length; i++) {
    if (have[i] === 0) {
      // 유니폼이 없으면 앞뒤 학생이 줄 수 있다
      if (have[i - 1] === 2) {
        // 앞 사람이 2개일 때
        have[i]++;
        have[i - 1]--;
      } else if (have[i + 1] === 2) {
        // 뒷 사람이 2개일 때
        have[i]++;
        have[i + 1]--;
      }
    }
    if (have[i] >= 1) {
      // 체육을 들을 수 있는 사람(원래 있고, 받은 사람)
      answer++;
    }
  }
  return answer;
}
