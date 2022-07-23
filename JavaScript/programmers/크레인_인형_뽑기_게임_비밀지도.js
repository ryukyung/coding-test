function solution(board, moves) {
  let result = 0;
  let move = 0;
  let basket = [];

  for (let i = 0; i < moves.length; i++) {
    for (let j = 0; j < board.length; j++) {
      if (board[j][moves[i] - 1] !== 0) {
        if (move === board[j][moves[i] - 1]) {
          result += 2;
          if (basket.length > 0) {
            basket.pop();
            move = basket[basket.length - 1];
          } else {
            move = 0;
          }
        } else {
          basket.push(board[j][moves[i] - 1]);
          move = board[j][moves[i] - 1];
        }
        board[j][moves[i] - 1] = 0;
        break;
      }
    }
  }
  return result;
}
