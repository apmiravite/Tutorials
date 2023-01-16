function getLetter(s) {
    let letter;
    // Write your code here
    switch(true){
        case 'aeiou'.includes(s[0]):
            letter="A"
            break;
        case 'bcdfg'.includes(s[0]):
            letter="B"
            break;
        case 'hjlkm'.includes(s[0]):
            letter="C"
            break;
        default:
            letter="D"
            break;
    }
    return letter;
}


function main() {
    const s = readLine();
    
    console.log(getLetter(s));
}
