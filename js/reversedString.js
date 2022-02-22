function solution(str){
  let reversed = '';
  for(let i = 1; i <= str.length; i++){
    reversed += str[str.length - i];
  }
  return reversed;
}