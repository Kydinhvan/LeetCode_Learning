// Last updated: 5/27/2025, 3:42:23 PM
/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    // catch reject or then for resolve
    return async function(...args) {
        let promise = new Promise((resolve, reject) => {
            setTimeout(() =>{
                reject('Time Limit Exceeded');
            },t);
            return fn(...args).then(resolve).catch(reject);
        }) 
        return promise;

    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */