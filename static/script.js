// login page

function login(){
    document.location.href="/loginpage";
}

// sign up page

function signup(){
    document.location.href="/signuppage";
}

// home page
function homepage(){
    document.location.href="/";
}


// user landing page

function userlanding(){
    document.location.href="/userlanding";
}

function edithabit(){
    document.querySelector(".edithabit-window").style.display = "flex";
}

function createhabit(){
    document.querySelector(".createhabit-window").style.display = "flex";
}


// function deletehabit(){
//     document.querySelector(".deletehabit-window").style.display = "flex";
// }

document.querySelector(".closeedit").addEventListener("click", function() {
    document.querySelector(".edithabit-window").style.display = "none";
});

document.querySelector(".closecreate").addEventListener("click", function() {
    document.querySelector(".createhabit-window").style.display = "none";
});

// document.querySelector(".closedelete").addEventListener("click", function() {
//     document.querySelector(".deletehabit-window").style.display = "none";
// });

class ProgressBar {
    constructor (element, initialValue = 0) {
        this.valueElem = element.querySelector(".progress-bar-value");
        this.fillElem = element.querySelector('.progress-bar-fill');

        this.setValue(initialValue);
    }

    setValue (newValue) {
        if (newValue < 0) {
            newValue = 100;
        }

        if (newValue > 100) {
            newValue = 100;
        }

        this.value = newValue;
        this.update();
    }

    update () {
        const percentage = this.value + "%";

        this.fillElem.style.width = percentage;
        this.valueElem.textContent = percentage;
    }
}

const pb1 = new ProgressBar(document.querySelector('.progress-bar'), 30);

// activating and deactivitating the delete button
document.getElementById("myBtn").disabled = true; 








// !!!Element(or document).querySelector finds FIRST element(or document) (first instance in HTML code) that matches the css selector  

// !!!querySelectorAll finds all elements (first instance in HTML code) that matches the css selector. returns in the form of a node list (basically array. i can use it as an array) which you must iterate through  


// document.querySelector(".close").addEventListener("click", function() {
//     document.querySelector(".edithabit-window").style.display = "none";
// });