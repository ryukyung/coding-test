// [12903] 가운데 글자 가져오기

function solution(s) {
  let answer = "";
  if (s.length % 2 == 0) {
    answer = s[s.length / 2 - 1] + s[s.length / 2];
  } else {
    answer = s[(s.length - 1) / 2];
  }
  return answer;
}

function solution(s) {
  if (s.length % 2 == 0) {
    return s.substr(s.length / 2 - 1, 2);
  } else {
    return s.substr(s.length / 2, 1);
  }
}
