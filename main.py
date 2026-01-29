from js import document
import random

def check(event=None):
    output = document.getElementById("output")
    message = document.getElementById("message")
    team = document.getElementById("team")

    reg = document.querySelector('input[name="registered"]:checked')
    med = document.querySelector('input[name="medical"]:checked')
    grade = document.getElementById("grade").value

    output.style.display = "block"
    message.innerText = ""
    team.innerText = ""

    if reg is None or reg.value != "yes":
        message.innerText = "Please register online."
        return

    if med is None or med.value != "yes":
        message.innerText = "Please secure a medical clearance."
        return

    if grade == "" or int(grade) < 7 or int(grade) > 10:
        return

    teams = [
        "Blue Bears",
        "Red Bulldogs",
        "Yellow Tigers",
        "Green Hornets"
    ]

    assigned = random.choice(teams)

    message.innerText = "Congratulations!"
    team.innerText = "its your now a part of " + assigned


document.getElementById("checkBtn").addEventListener("click", check)
