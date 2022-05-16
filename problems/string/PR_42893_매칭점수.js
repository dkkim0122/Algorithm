function solution(word, pages) {
  var answer = 0;
  word = word.toLowerCase();
  const REG_WORD = /[\d|\W]/; // 숫자이거나 단어(알파벳, 숫자)가 아닌(특수문자) 애들을 기준으로 단어들을 나누고, word와 일치하는 애들을 찾는다.
  const REG_URL = /<a href="https:\S*/gi;
  const META_URL = "meta property"; // 이 친구가 들어있는 tag를 고를 것.
  const pageInfo = new Map(); // key: url => value:[basic_score, outer_links, link_score, [links] ]

  pages.forEach((page, idx) => {
    const tags = page.split("\n");
    const urlIdx = tags.findIndex((el) => el.includes(META_URL));
    const url = tags[urlIdx].match(/"https:\S*[^/>]/gi)[0]; // https: 뒤에 공백만 아닌 모든 글자 계속 반복되면 그것 다 가져오기

    // body내의 매칭 시작
    const body_start = tags.findIndex((el) => el === "<body>");
    const body_end = tags.findIndex((el) => el === "</body>");
    const body = tags.slice(body_start + 1, body_end);

    const basic_score = body
      .flatMap((str) => str.split(REG_WORD))
      .filter((str) => str.toLowerCase() === word).length;

    // 배열 중에 null이 아닌 친구들만 고르기 .filter(e => e)
    // string을 index 별로 자르기 string.substr(startIdx, endIdx), endIdx는 포함 안 함
    const outer_links = body
      .flatMap((str) => str.match(REG_URL))
      .filter((e) => e)
      .map((str) => str.substr(8, str.length).split(">")[0]);
    pageInfo.set(url, { basic_score, outer_links, idx, score: 0 });
  });

  for (const [page, info] of pageInfo) {
    const link_score = info.basic_score / info.outer_links.length;
    info.score += info.basic_score;

    for (const link of info.outer_links) {
      const value = pageInfo.get(link);
      if (value) {
        value.score += link_score;
      }
    }
  }

  const result = [];
  for (const [page, info] of pageInfo) {
    result.push(info.score);
  }

  const max = Math.max(...result);

  return result.findIndex((val) => val === max);
}
