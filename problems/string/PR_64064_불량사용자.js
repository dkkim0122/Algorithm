function solution(user_id, banned_id) {
  let visit = []
  let set = new Set()

  function makeList(idx, count, str) {
    if (count === banned_id.length) {
      let arr = str.split(" ");
      arr.shift();
      arr.sort()
      let newstr = arr.join("")
      set.add(newstr)
    }

    if (idx >= user_id.length) return;

    for (let i = idx; i < banned_id.length; i++) {
      for (let j = 0; j < user_id.length; j++) {
        if (visit[j]) continue;

        if (!check(banned_id[i], user_id[j])) continue;

        visit[j] = 1;
        makeList(i + 1, count + 1, str + " " + user_id[j]);
        visit[j] = 0;
      }
    }
  }

  makeList(0, 0, "");
  return set.size;
}

function check(str, ban) {
  if (str.length !== ban.length) return false;
  for(let i = 0; i < ban.length; i++) {
    if (ban[i] !== "*" && ban[i] !== str[i]) return false;
  }
  return true;
}
