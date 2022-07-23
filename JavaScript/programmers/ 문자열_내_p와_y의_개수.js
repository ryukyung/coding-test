// [12916]문자열 내 p와 y의 개수

function solution(s) {
  let change = s.toLowerCase();
  let p = change.split("p").length;
  let y = change.split("y").length;
  return p == y ? true : false;
}
function solution(s) {
  let change = s.toUpperCase();
  let p = change.split("P").length;
  let y = change.split("Y").length;
  return p == y ? true : false;
}
