// Given: an array containing hashes of names
// Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

// Example:
// list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
// returns 'Bart, Lisa & Maggie'

// list([ {name: 'Bart'}, {name: 'Lisa'} ])
// returns 'Bart & Lisa'

// list([ {name: 'Bart'} ])
// returns 'Bart'

// list([])
// returns ''

function list(names){
    let arr = [];

    if(names.length > 1){
        for(let i = 0, n; i < names.length; i++){
            if(i+1 == names.length){
                n = '& ' + names[i]['name'];
            } else if(i + 1 == names.length - 1){
                n = names[i]['name'] + ' ';
            } else{
                n = names[i]['name'] + ', ';
            }
            arr.push(n);
        }
    } else {
        arr.push(names[0]['name']);
    }

    return arr.join('');
}