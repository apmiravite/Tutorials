function getDayName(dateString) {
    // Write your code here
    const days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    let dayName = days[new Date(dateString).getDay()]
    return dayName;
}
