let bossHealth = 100;
let selectedClass = "";

function selectClass(characterClass) {
    selectedClass = characterClass;
    document.getElementById("character-class").textContent = selectedClass;

    // Change the player sprite based on the selected class
    const playerSprite = document.getElementById("player-sprite");
    playerSprite.src = `sprites/${characterClass.toLowerCase().replace(" ", "-")}.png`;

    // Hide the class selection and show the battle area
    document.getElementById("class-selection").style.display = "none";
    document.getElementById("battle").style.display = "block";
}

function attack() {
    const damage = Math.floor(Math.random() * 10) + 5;
    bossHealth -= damage;
    updateBattleState(`You attacked the Cyborg for ${damage} damage!`);
}

function specialAttack() {
    const damage = Math.floor(Math.random() * 20) + 10;
    bossHealth -= damage;
    updateBattleState(`You used a special attack and dealt ${damage} damage!`);
}

function updateBattleState(message) {
    document.getElementById("boss-health").textContent = `Boss Health: ${bossHealth}`;
    document.getElementById("message").textContent = message;

    if (bossHealth <= 0) {
        document.getElementById("message").textContent = `You defeated the Cyborg Boss!`;
        document.getElementById("controls").style.display = "none";
    }
}
