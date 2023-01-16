/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    const unique = (value, index, self) => {
        return self.indexOf(value) === index
    }
    
    const uniqueNums = nums.filter(unique)
    
    uniqueNums.sort()
    let i=uniqueNums.length
    return(uniqueNums[i-2])
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}
