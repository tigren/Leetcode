/**
* @param {number[]} nums
* @param {number} target
* @return {number[]}
*/
var twoSum = function(nums, target) {

    var obj = {};

    for (var i = 0; i < nums.length; i++){
        if(nums[i] in obj){
            obj[nums[i]].push(i + 1);
        }
        else {
            obj[nums[i]] = [i + 1];
        }
    }

    for (var i = 0; i < nums.length; i++){
        if (target - nums[i] in obj){
            if (target - nums[i] == nums[i]){
                if (obj[nums[i]].length > 1){
                    return [obj[nums[i]][0], obj[nums[i]][1]];
                }
            }
            else{
                return [obj[nums[i]][0], obj[target - nums[i]][0]];
            }
        }
    }
};
