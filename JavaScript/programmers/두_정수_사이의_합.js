// [12912] 두 정수 사이의 합
function solution(a, b) {
  let answer = 0;
  if (a >= b) {
    for (let i = b; i <= a; i++) {
      answer += i;
    }
  } else {
    for (let i = a; i <= b; i++) {
      answer += i;
    }
  }
  return answer;
}

function solution(a, b) {
  let answer = 0;
  answer = ((a + b) * (Math.abs(b - a) + 1)) / 2;
  return answer;
}
