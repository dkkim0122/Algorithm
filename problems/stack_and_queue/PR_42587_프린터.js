function solution(priorities, location) {
  const value = priorities.map((priority, index) => {
    return {
      priority: priority,
      index: index,
    };
  });

  let stack = [];

  while (value.length) {
    const val = value.shift();
    const notMaxVal = value.some((other) => other.priority > val.priority);
    if (notMaxVal) value.push(val);
    else stack.push(val);
  }

  const answer = stack.findIndex((val) => val.index === location);
  return answer + 1;
}
