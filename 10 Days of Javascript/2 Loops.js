/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    
    for(let i=0;i<=s.length;i++){
        if ('aeiou'.includes(s[i])){
            console.log(s[i])
        }
    }
    
    for(let i=0;i<=s.length;i++){
        if ('bcdfghjklmnpqrstvwxyz'.includes(s[i])){
            console.log(s[i])
        }
    }
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}
