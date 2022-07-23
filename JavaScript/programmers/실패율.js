// [42889] 실패율
function solution(N, stages) {
  let result = [];
  let notClear = stages.length;
  for (let i = 1; i <= N + 1; i++) {
    let clear = stages.filter((n) => n === i).length;
    result.push([i, clear / notClear]);
    notClear -= clear;
  }
  result.pop();
  result = result.sort((a, b) => b[1] - a[1]);
  return result.map((a) => a[0]);
}
