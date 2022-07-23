// [42728] k번째 수

function solution(array, commands) {
  let answer = [];
  let i = 0;
  let j = 0;
  let k = 0;
  for (let n = 0; n < commands.length; n++) {
    i = commands[n][0];
    j = commands[n][1];
    k = commands[n][2];
    let sorted = array.slice(i - 1, j).sort((a, b) => a - b);
    answer.push(sorted[k - 1]);
  }
  return answer;
}
