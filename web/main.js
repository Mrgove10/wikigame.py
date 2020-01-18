var roundNumber = 1;

eel.expose(getRoundNumber);//makes it available in python
function getRoundNumber() {
    return roundNumber
}

eel.expose(addRoundNumber);//makes it available in python
function addRoundNumber() {
    roundNumber = roundNumber + 1
}

eel.expose(printInPageSting);//makes it available in python
function printInPageSting(x) {
    document.getElementById("mainbody").innerHTML = x;
}

eel.expose(printInConsole);
function printInConsole(x) {
    console.log(x)
}

eel.expose(printInPageList);//makes it available in python
function printInPageList(x) {
    x.forEach(print);
}
function print(element, index) {
    document.getElementById("choiceList").innerHTML +=
        `<li><button class=\"btn btn-primary\" onclick=\" goToNextPage(${index})\">${element}</button></li>`
}

eel.expose(updateCurrentPage);//makes it available in python
function updateCurrentPage(x) {
    document.getElementById("currentPage").innerHTML =
        `<b>Current page :</b>${x[0]} <a href="${x[1]}" target="_blank">View Wikipedia Page</a>`
}

eel.expose(updateStartPage);//makes it available in python
function updateStartPage(x) {
    document.getElementById("startPage").innerHTML =
        `<b>Start page :</b> ${x[0]} <a href="${x[1]}" target="_blank">View Wikipedia Page</a>`
}

eel.expose(updateGoalPage);//makes it available in python
function updateGoalPage(x) {
    document.getElementById("goalPage").innerHTML =
        `<b>Goal page :</b> ${x[0]} <a href="${x[1]}" target="_blank">View Wikipedia Page</a>`
}

eel.expose(updateRoundNumber);//makes it available in python
function updateRoundNumber(x) {
    document.getElementById("roundCounter").innerHTML = "Round " + x;
}

function goToNextPage(currentpage, index) {
    eel.goToNextLink(currentpage, index)
}

function goToPrevPage() {
    eel.goToPrevLink()
}

eel.selectlink("Javascript World!");