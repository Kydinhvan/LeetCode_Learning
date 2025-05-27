// Last updated: 5/27/2025, 1:21:10 PM
/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    const result = await promise1;
    const result2 = await promise2;
    return new Promise((resolve, reject) => resolve(result+result2));
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */