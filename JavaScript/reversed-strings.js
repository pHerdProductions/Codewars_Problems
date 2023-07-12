// Function to reverse a string
function solution(str){
  let ans = '';

  // For loop starting from the end of the string -> beginning
  for (let i = str.length - 1; i >= 0; i--) {
    ans += str[i];
  }
  
  return ans;
}

// Clever code version
function solution(str){
  return str.split('').reverse().join('');
}
