/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    if(root === null) return []
    let currentLevel = []
    let nextLevel = []
    let result = [];
    currentLevel.push(root)
    result.push([root.val])
    
    
    while(currentLevel.length) {
        let current = currentLevel.shift();
        for (let child of current.children) {
            nextLevel.push(child)          
        }
        
        if(!currentLevel.length && nextLevel.length) {
            let newResult = []
            for (let val of nextLevel) {
                newResult.push(val.val)          
            }
            result.push(newResult)
            currentLevel = nextLevel;
            nextLevel = []
        }
    }
    
    return result
    
};