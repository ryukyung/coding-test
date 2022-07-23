// [42840] 모의고사
function solution(answers) {
  let result = [];
  const student1 = [1, 2, 3, 4, 5];
  const student2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  const one = answers.filter(
    (x, i) => x === student1[i % student1.length]
  ).length;
  const two = answers.filter(
    (x, i) => x === student2[i % student2.length]
  ).length;
  const three = answers.filter(
    (x, i) => x === student3[i % student3.length]
  ).length;
  const max = Math.max(one, two, three);

  if (one === max) {
    result.push(1);
  }
  if (two === max) {
    result.push(2);
  }
  if (three === max) {
    result.push(3);
  }
  return result;
}
// lookup table 해보기
