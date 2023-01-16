/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    //return nums
    let largest_num=nums[0]
    let nextLargest=nums[0]
    for (let i in nums){
        if (nums[i]>largest_num){
            nextLargest=largest_num
            largest_num=nums[i]
        }
        if (nums[i]>nextLargest && nums[i]!=largest_num){
            nextLargest=nums[i]
        }
    }
    return nextLargest
    
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}
