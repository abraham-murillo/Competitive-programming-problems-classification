import Array2D from "./array2D";

const INF = 1e9;

export default function editDistance(a, b) {
  var mem = new Array2D(a.length, b.length, INF);

  function dp(i, j) {
    if (i > a.length || j > b.length)
      return INF;

    if (i === a.length)
      return b.length - j;

    if (j === b.length)
      return a.length - i;

    if (mem[i][j] >= INF) {
      var mn = INF;
      // Insert character
      mn = Math.min(mn, dp(i, j + 1) + 1);
      // Delete character
      mn = Math.min(mn, dp(i + 1, j) + 1);
      // Replace character
      mn = Math.min(mn, dp(i + 1, j + 1) + 1);
      // Skip
      if (a[i] === b[j]) {
        mn = Math.min(mn, dp(i + 1, j + 1));
      }
      mem[i][j] = mn;
    }

    return mem[i][j];
  }

  return dp(0, 0);
}