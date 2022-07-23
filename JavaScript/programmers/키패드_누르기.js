// [67256] 키패드 누르기
// 방법2 -> https://velog.io/@le12352/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%82%A4%ED%8C%A8%EB%93%9C-%EB%88%84%EB%A5%B4%EA%B8%B0-Javascript
// 객체 공부하고 나서 해석해보기
function solution(numbers, hand) {
  // 위치 찾는 함수
  function findKey(key) {
    let keypad = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      ["*", 0, "#"],
    ];
    for (let i = 0; i < 4; i++) {
      for (let j = 0; j < 3; j++) {
        if (keypad[i][j] === key) {
          return [i, j];
        }
      }
    }
  }
  var answer = "";
  let left = "*";
  let right = "#";
  for (let i of numbers) {
    if (i === 1 || i === 4 || i === 7) {
      answer += "L";
      left = i;
    } else if (i === 3 || i === 6 || i === 9) {
      answer += "R";
      right = i - 2;
    } else {
      let r = findKey(right);
      let l = findKey(left);
      let middle = findKey(i);
      // 손과 키패드의 거리
      let rr = Math.abs(r[0] - middle[0]) + Math.abs(r[1] - middle[1]);
      let ll = Math.abs(l[0] - middle[0]) + Math.abs(l[1] - middle[1]);
      if (rr === ll) {
        // 거리가 같다면 오른손잡이 -> 'R', 왼손잡이 -> 'L'
        hand === "right"
          ? ((right = i), (answer += "R"))
          : ((left = i), (answer += "L"));
      } else if (rr > ll) {
        // 오른손의 거리가 멀다면
        answer += "L";
        left = i;
      } else {
        // 왼손의 거리가 멀다면
        answer += "R";
        right = i;
      }
    }
  }
  return answer;
}
// 반복가능한 객체에 대해서 반복하고 각 개별 속성값에 대해 실행되는 문이 있는 사용자 정의 반복 후크를 호출하는 루프 생성
// for (variable of iterable){ statment }
