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
        document.getElementById("message").innerHTML = `<span style="color: white; font-weight: bold;">You defeated the Boss!</span>`;
        document.getElementById("controls").style.display = "none";  // Hide attack buttons
        setTimeout(() => {
            if (data.boss_name === "bertak_boss") {
                window.location.href = "/Final_game_screen.html";  // Bertak defeated, redirect to victory page
            } else {
                window.location.href = "/portals";  // Other bosses defeated, redirect to portals
            }
        }, 3000);
        }

    // Check if the player has been defeated
    if (data.player_health <= 0) {
        document.getElementById("message").innerHTML = `<span class="bold-blue">You were defeated by the Boss. Game Over.</span>`;
        document.getElementById("controls").style.display = "none";  // Hide attack buttons
        setTimeout(() => {
            window.location.href = "/portals";
        }, 5000);
    }
}