const fs = require("fs");
let arr = fs.readFileSync('./dev/stdin').toString().split('\n').map(Number);
let n = arr.shift();
let dp = new Array(n+1).fill(1);
for (let i = 1; i<n; i++) {
    for (let j = 0; j<i; j++) {
        if (arr[i] > arr[j]) {
            dp[i] = Math.max(dp[i], dp[j] + 1);
        }
    }
}
console.log(n - Math.max(...dp));