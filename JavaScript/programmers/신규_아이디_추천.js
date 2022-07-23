function solution(new_id) {
  let result = new_id
    .toLowerCase()
    .replace(/[^a-z0-9-_.]/gi, "")
    .replace(/[.]{2,}/gi, ".")
    .replace(/^[.]|[.]$/gi, "");
  // 소문자를 위해 toLowerCase
  // 1번 replace : 제외하고 전부 빼주세요,
  // 2번 replace : .이 2개 이상이면 빼세요
  // 3번 replace : 오점 2개로 끝나면 지우시오 -> 이어서 오기X, 마지막에X라서
  if (result === "") result = "a"; // 공백을 받으면 a를 넣어라
  if (result.length > 15) {
    result = result.substring(0, 15);
    // 글자수가 15글자 초과 시 앞에 15글자만 받고 버려라
    result = result.replace(/[.]$/gi, "");
    //   마지막에 .으로 끝나면 지워라
  }
  while (result.length < 3) {
    result += result[result.length - 1];
    // 만약 3글자 이하라면 반복해라
  }
  return result;
}
