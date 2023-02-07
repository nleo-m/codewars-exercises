// The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

// Examples
// "din"      =>  "((("
// "recede"   =>  "()()()"
// "Success"  =>  ")())())"
// "(( @"     =>  "))((" 


function duplicateEncode(word) {
    word = word.toLowerCase();
    let newWord = ''

    for (letter of word) {
        const specials = /[-[\]{}()*+?.,\\^$|#\s]/g
        const regex = new RegExp(`${(specials.test(letter) && '\\') || ''}${letter}`, 'g');
        const count = word.match(regex)?.length;
        if (count)
            newWord += count > 1 ? ')' : '(';
    }

    return newWord
}


// duplicateEncode('dinab');
// duplicateEncode('recede');
// duplicateEncode('success');
// duplicateEncode('(( @');
// duplicateEncode('FFwFdGFbyFT(FFFR');