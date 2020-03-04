const a = new Map()
const ar1 = [1, 2]
a.set(ar1, 'list')
ar1[1] = 3

var jj = {
  [ar1]: 1
}
console.log(jj['1,3'])
