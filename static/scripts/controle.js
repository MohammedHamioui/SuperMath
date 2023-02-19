let corrans = Number(localStorage.getItem('countCorrect')) || 0;
let wrongans = Number(localStorage.getItem('countWrong')) || 0;


function controlePlus(key, value) {
    let num_a = parseInt(document.getElementById("a").innerHTML);
    let num_b = parseInt(document.getElementById("b").innerHTML);
    let c = num_a + num_b
    let ans = document.getElementById("ans").value;

    if (ans == c) {
        localStorage.setItem('countCorrect', corrans + 1);
    }
    else {
        localStorage.setItem('countWrong', wrongans + 1);
    }

    location.reload()
}

function ControleMin() {
    let num_a = parseInt(document.getElementById("a").innerHTML);
    let num_b = parseInt(document.getElementById("b").innerHTML);
    let c = num_a - num_b
    let ans = document.getElementById("ans").value;

    if (ans == c) {
        localStorage.setItem('countCorrect', corrans + 1);
    }
    else {
        localStorage.setItem('countWrong', wrongans + 1);
    }

    location.reload()
}

function ControleMaal() {
    let num_a = parseInt(document.getElementById("a").innerHTML);
    let num_b = parseInt(document.getElementById("b").innerHTML);
    let c = num_a * num_b
    let ans = document.getElementById("ans").value;

    if (ans == c) {
        localStorage.setItem('countCorrect', corrans + 1);
    }
    else {
        localStorage.setItem('countWrong', wrongans + 1);
    }

    location.reload()
}

function ControleDeel() {
    let num_a = parseInt(document.getElementById("a").innerHTML);
    let num_b = parseInt(document.getElementById("b").innerHTML);
    let c = num_a / num_b
    let ans = document.getElementById("ans").value;

    if (ans == c) {
        localStorage.setItem('countCorrect', corrans + 1);
    }
    else {
        localStorage.setItem('countWrong', wrongans + 1);
    }

    location.reload()
}

function reset(){
    localStorage.removeItem('countCorrect');
     localStorage.removeItem('countWrong');
     location.reload()
}

document.getElementById("correct_ans").innerHTML = localStorage.getItem('countCorrect');
document.getElementById("wrong_ans").innerHTML = localStorage.getItem('countWrong');