// Last updated: 5/25/2025, 9:29:31 PM
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    var new_array = [];
    for (let i = 0; i<arr.length; i++){
        new_array.push(fn(arr[i],i));
    }
    console.log(new_array)
    return new_array;
};