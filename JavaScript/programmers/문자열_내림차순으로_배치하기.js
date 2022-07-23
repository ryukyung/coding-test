// [12917] 문자열 내림차순으로 배치하기
function solution(s) {
  let answer = "";
  let lowercase = s.replace(/[A-Z]/g, "").split("").sort().reverse().join("");
  let uppercase = s.replace(/[a-z]/g, "").split("").sort().reverse().join("");
  return (answer = lowercase + uppercase);
}

function solution(s) {
  return s.split("").sort().reverse().join("");
}
