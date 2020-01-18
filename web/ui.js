/**
 * updates the current page text
 */
eel.expose(updateCurrentPage);//makes it available in python
function updateCurrentPage(x) {
    document.getElementById("currentPage").innerHTML =
        `<b>Current page :</b> ${x[0]} <a href="${x[1]}" target="_blank">View Wikipedia Page</a>`
}

/**
 * updates the start page text
 */
eel.expose(updateStartPage);//makes it available in python
function updateStartPage(x) {
    document.getElementById("startPage").innerHTML =
        `<b>Start page :</b> ${x[0]} <a href="${x[1]}" target="_blank">View Wikipedia Page</a>`
}

/**
 * updates the goal page text
 */
eel.expose(updateGoalPage);//makes it available in python
function updateGoalPage(x) {
    document.getElementById("goalPage").innerHTML =
        `<b>Goal page :</b> ${x[0]} <a href="${x[1]}" target="_blank">View Wikipedia Page</a>`
}

/**
 * Updates the round number on the html page
 */
eel.expose(updateRoundNumber);//makes it available in python
function updateRoundNumber() {
    document.getElementById("roundCounter").innerHTML = "Round " + roundNumber;
}

/**
 * prints all the pinks as buttons
 */
eel.expose(printInPageList);//makes it available in python
function printInPageList(x) {
    x.forEach(print);
}
function print(element, index) {
    document.getElementById("choiceList").innerHTML +=
        `<li><button class=\"btn btn-primary\" onclick=\" goToNextPage(${index})\">${element}</button></li>`
}

/**
 * clears allt he links in the page
 */
eel.expose(clearPageList);//makes it available in python
function clearPageList() {
    document.getElementById("choiceList").innerHTML = ``
}
