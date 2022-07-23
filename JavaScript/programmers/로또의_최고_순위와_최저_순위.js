// [77484] 로또의 최고 순위와 최저 순위
function solution(lottos, win_nums) {
  const correct = lottos.filter((lotto) => win_nums.includes(lotto)).length;
  const zeros = lottos.filter((lotto) => lotto === 0).length;
  console.log(correct, zeros);
  let min = 7 - correct >= 6 ? 6 : 7 - correct;
  let max = min - zeros < 1 ? 1 : min - zeros;
  return [max, min];
}
