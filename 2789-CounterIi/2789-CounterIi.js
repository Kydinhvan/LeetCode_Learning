// Last updated: 5/25/2025, 9:29:32 PM
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    var init_init = init;
    return {
        increment: function() {
            return ++init;
        },
        decrement: function() {
            return --init;
        },
        reset: function() {
            init = init_init
            return init
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */