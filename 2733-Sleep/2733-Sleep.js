// Last updated: 5/27/2025, 3:42:26 PM
/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    let fn = new Promise((resolve,reject)=>{
        setTimeout(() =>{
            resolve("Time out");
        },millis)
    })
    return fn;
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */