#!/usr/bin/node
const dic = require('./101-data').dic;

const total = Object.entries(dic);
const val = Object.values(dic);
const valUniq = [...new Set(val)];
const newDic = {};
for (const j in valUniq) {
  const lists = [];
  for (const k in total) {
    if (total[k][1] === valUniq[j]) {
      lists.unshift(total[k][0]);
    }
  }
  newDic[valUniq[j]] = lists;
}
console.log(newDic);
