// Last updated: 1/22/2026, 12:12:30 PM
/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
var promisePool = async function(functions, n) {
    let p_count = 0;
    const promise_await_1by1 = async () => {
        if (p_count>= functions.length) return; // exceed pool limit
        const fn = functions[p_count++]; // post incre
        await fn(); 
        await promise_await_1by1(); // recursively await till done
    }
    
    const pool = Array(n).fill().map(promise_await_1by1);

    await Promise.all(pool) // Wait all tasks
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */

