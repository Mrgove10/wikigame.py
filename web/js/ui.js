//==========
/**
 * updates the current page text
 */
eel.expose(updateCurrentPage);//makes it available in python
function updateCurrentPage(x) {
    document.getElementById("currentPage").innerHTML =
        `${x[0]} </br>
        <h6><a href="${x[1]}" target="_blank">View Wikipedia Page </a><i class="fas fa-external-link-alt"></i></h6>`
}

/**
 * Updates the current page description.
 */
eel.expose(updateCurrentPageDescription);//makes it available in python
function updateCurrentPageDescription(x) {
    document.getElementById("currentPageDesc").innerHTML = `${x}`
}
//==========
/**
 * updates the start page text
 */
eel.expose(updateStartPage);//makes it available in python
function updateStartPage(x) {
    document.getElementById("startPage").innerHTML =
        `${x[0]} </br>
        <h6><a href="${x[1]}" target="_blank">View Wikipedia Page </a><i class="fas fa-external-link-alt"></i></h6>`
}

/**
 * Updates the description of the start page
 */
eel.expose(updateStartPageDescription);//makes it available in python
function updateStartPageDescription(x) {
    document.getElementById("startPageDesc").innerHTML = `${x}`
}
//==========
/**
 * updates the goal page text
 */
eel.expose(updateGoalPage);//makes it available in python
function updateGoalPage(x) {
    document.getElementById("goalPage").innerHTML =
        `${x[0]} </br>
        <h6><a href="${x[1]}" target="_blank">View Wikipedia Page </a><i class="fas fa-external-link-alt"></i></h6>`
}

/**
 * Updates the Goal page description
 */
eel.expose(updateGoalPageDescription);//makes it available in python
function updateGoalPageDescription(x) {
    document.getElementById("goalPageDesc").innerHTML = `${x}`
}
//==========

/**
 * Updates the round number on the html page
 */
eel.expose(updateRoundNumber);//makes it available in python
function updateRoundNumber() {
    document.getElementById("roundCounter").innerHTML = "Round " + roundNumber;
}

/**
 * prints all the links as buttons
 */
eel.expose(printInPageList);//makes it available in python
function printInPageList(x) {
    document.getElementById("choiceList").innerHTML = ``
    x.forEach(print);
}
function print(element, index) {
    document.getElementById("choiceList").innerHTML +=
        `<button class=\"btn btn-primary\" onclick=\" goToNextPage(${index})\">${element}</button>`
}

/**
 * Updates the history list
 */
eel.expose(updateHistory);
function updateHistory(x) {
    document.getElementById("history").innerHTML = ``
    x.forEach(element => {
        document.getElementById("history").innerHTML += `<li>${element}</li>`
    });
}

/**
 * Show the loading modal on the screen
 */
eel.expose(showLoader);
function showLoader() {
    $('#loadingmodal').modal('show');
}

/**
 * Hides the loading modal on screen
 */
eel.expose(hideLoader);
function hideLoader() {
    $('#loadingmodal').modal('hide');
}

/**
 * Show the end page
 */
eel.expose(showVictory);
function showVictory() {
    $('#victory').modal('show');
    document.getElementById("finalRounds").innerHTML = roundNumber;
}
