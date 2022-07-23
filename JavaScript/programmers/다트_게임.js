function solution(dartResult) {
  const answer = [];
  let result = 0;
  let numberBox = 0; //temp
  for (let i = 0; i < dartResult.length; i++) {
    if (dartResult[i] >= 0 && dartResult[i] <= 9) {
      if (dartResult[i] == 1 && dartResult[i + 1] == 0) {
        // js는 10이 아닌 1과 0을 받기 때문에 확인할 때 1, 0을 따로 받아야 함
        numberBox = 10;
        i++;
      } else {
        numberBox = dartResult[i];
      }
    } else if (dartResult[i] === "S") {
      answer.push(numberBox);
    } else if (dartResult[i] === "D") {
      answer.push(Math.pow(numberBox, 2));
    } else if (dartResult[i] === "T") {
      answer.push(Math.pow(numberBox, 3));
    } else if (dartResult[i] === "#") {
      answer[answer.length - 1] *= -1;
    } else if (dartResult[i] == "*") {
      answer[answer.length - 1] *= 2;
      answer[answer.length - 2] *= 2;
    }
  }
  for (let i = 0; i < answer.length; i++) {
    result += Number(answer[i]);
  }
  return result;
}
