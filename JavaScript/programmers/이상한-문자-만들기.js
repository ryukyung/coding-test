// [12930] 이상한 문자 만들기
function solution(s) {
  let arr = s.split(" ");
  let answer = "";
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      if (j % 2 !== 0) {
        answer = answer + arr[i][j].toLowerCase();
      } else {
        answer = answer + arr[i][j].toUpperCase();
      }
    }
    if (i < arr.length - 1) {
      answer = answer + " ";
    }
  }
  return answer;
}
