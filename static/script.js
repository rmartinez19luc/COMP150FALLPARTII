let bossHealth = 100;
let playerHealth = 100;
let selectedClass = "";

function selectClass(characterClass) {
    selectedClass = characterClass;
    document.getElementById("character-class").textContent = selectedClass;

    const playerSprite = document.getElementById("player-sprite");
    playerSprite.src = `static/sprites/${characterClass.toLowerCase().replace(" ", "-")}.jpg`;

    // Hide the class selection and show the battle area
    document.getElementById("class-selection").style.display = "none";
    document.getElementById("battle").style.display = "block";
}

async function attack() {
    const response = await fetch('/cyborg_battle', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ action: 'attack' })
    });
    const data = await response.json();
    updateBattleState(data);
}

async function specialAttack() {
    const response = await fetch('/cyborg_battle', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ action: 'specialAttack' })
    });
    const data = await response.json();
    updateBattleState(data);
}

async function goBack() {
    // Go back to the class selection screen
    document.getElementById("battle").style.display = "none";
    document.getElementById("class-selection").style.display = "block";
}

function updateBattleState(data) {
    // Update the displayed boss and player health
    document.getElementById("boss-health").textContent = `Boss Health: ${data.boss_health}`;
    document.getElementById("player-health").textContent = `Player Health: ${data.player_health}`;

    // Update the battle message
    document.getElementById("message").textContent = data.message;

    // Check if the boss has been defeated
    if (data.boss_health <= 0) {
        document.getElementById("message").textContent = `You defeated the Cyborg Boss!`;
        document.getElementById("controls").style.display = "none";  // Hide attack buttons
    }

    // Check if the player has been defeated
    if (data.player_health <= 0) {
        document.getElementById("message").textContent = `You were defeated by the Cyborg Boss. Game Over.`;
        document.getElementById("controls").style.display = "none";  // Hide attack buttons
    }
}