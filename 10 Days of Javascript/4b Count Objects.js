/*
 * Return a count of the total number of objects 'o' satisfying o.x == o.y.
 * 
 * Parameter(s):
 * objects: an array of objects with integer properties 'x' and 'y'
 */
function getCount(objects) {
    var same=0
    for (let i in objects){
        if (objects[i].x==objects[i].y){
            same=same+1
        }
    }
    return same
}
