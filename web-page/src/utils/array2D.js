export default function Array2D(rows, cols, defaultValue = 0) {
  var arr = new Array(rows)
  for (var i = 0; i < rows; i++) {
    arr[i] = new Array(cols)
    for (var j = 0; j < cols; j++) {
      arr[i][j] = defaultValue;
    }
  }
  return arr;
}