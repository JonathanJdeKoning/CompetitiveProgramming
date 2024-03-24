/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    const sortedNums = arr.sort((a, b) => fn(a) - fn(b));
    return sortedNums
};
