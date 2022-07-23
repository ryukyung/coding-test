// [17681] (1차) 비밀지도
function solution(n, arr1, arr2) {
  let result = [];
  for (let i = 0; i < n; i++) {
    const change2 = (arr1[i] | arr2[i]).toString(2);
    let space = [];
    for (let j = change2.length - n; j < change2.length; j++) {
      if (change2[j] === "1") {
        space.push("#");
      } else {
        space.push(" ");
      }
    }
    result.push(space.join(""));
  }
  return result;
}
