
function solution(new_id) {
  const answer = new_id
  .toLowerCase()
  .replace(/[^\w-_.]/g, '') // A-Za-z0-9 - _ .을 제외한 애들을 ''로.
  .replace(/\.+/g, '.')     // 한 개 이상의 .이 연속되면 
  .replace(/^\.|\.$/g, '')  // 시작^이 .이거나(\.) 끝$이 .인 경우
  .replace(/^$/, 'a')  // 시작도 끝도 없다. 비어있다.
  .slice(0, 15).replace(/\.$/, '')

  return answer.padEnd(3, answer[answer.length - 1]);
}
