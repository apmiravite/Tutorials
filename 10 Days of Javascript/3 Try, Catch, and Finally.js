/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    try{
        var splitString=s.split("")
        //console.log(splitString)
        var reverse=splitString.reverse().join("")
        console.log(reverse)
    }
    catch (error){
        console.log(error.message);
        console.log(s)
    }
}
