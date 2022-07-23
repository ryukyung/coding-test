// [12931] 자릿수 더하기

function solution(n) {
  let answer = 0;
  let str = n.toString().split("");
  for (let i = 0; i < str.length; i++) {
    answer += parseInt(str[i]);
  }
  return answer;
}
