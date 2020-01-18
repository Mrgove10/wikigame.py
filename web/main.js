var roundNumber = 1;

eel.expose(getRoundNumber);//makes it available in python
function getRoundNumber() {
    return roundNumber
}

eel.expose(addRoundNumber);//makes it available in python
function addRoundNumber() {
    roundNumber = roundNumber + 1
}


eel.expose(printInConsole);
function printInConsole(x) {
    console.log(x)
}

/**
 * Calls the python function to go to the next link
 * @param {*} index 
 */
function goToNextPage(index) {
    eel.goToNextLink(index)
}

/**
 * Calls the python fuction to go back one page
 */
function goToPrevPage() {
    eel.goToPrevLink()
}

eel.selectlink("Javascript World!");