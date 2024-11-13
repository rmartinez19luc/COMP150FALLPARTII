function startTriviaGame() {
  const questions = [
    { question: "What was the capital of Ancient Egypt?", answer: "Thebes" },
    { question: "Which Greek philosopher taught Alexander the Great?", answer: "Aristotle" },
    { question: "Who was the king of the Ancient Greek gods?", answer: "Zeus" }
  ];

  let currentQuestion = questions[Math.floor(Math.random() * questions.length)];
  document.getElementById("question").textContent = currentQuestion.question;
  window.correctAnswer = currentQuestion.answer.toLowerCase();
}

function checkAnswer() {
  const userAnswer = document.getElementById("answer").value.toLowerCase();
  const feedback = document.getElementById("feedback");

  if (userAnswer === window.correctAnswer) {
    feedback.textContent = "Correct! You've solved the trivia.";
  } else {
    feedback.textContent = "Incorrect. Try again!";
  }
}


function startGuessingGame() {
  window.secretNumber = Math.floor(Math.random() * 10) + 1;
  document.getElementById("guess-feedback").textContent = "";
}

function makeGuess() {
  const userGuess = parseInt(document.getElementById("guess").value);
  const feedback = document.getElementById("guess-feedback");

  if (userGuess === window.secretNumber) {
    feedback.textContent = "Correct! You've guessed the number!";
  } else if (userGuess < window.secretNumber) {
    feedback.textContent = "Too low! Try again.";
  } else {
    feedback.textContent = "Too high! Try again.";
  }
}


let reactionTimeout;
let startTime;

function startReactionGame() {
  document.getElementById("reaction-button").style.display = "none";
  document.getElementById("reaction-feedback").textContent = "";
  reactionTimeout = setTimeout(() => {
    document.getElementById("reaction-button").style.display = "block";
    startTime = Date.now();
  }, Math.floor(Math.random() * 3000) + 1000);  // Appears randomly between 1-4 seconds
}

function checkReaction() {
  const reactionTime = Date.now() - startTime;
  document.getElementById("reaction-feedback").textContent = `Your reaction time is ${reactionTime} ms!`;
  document.getElementById("reaction-button").style.display = "none";
}


function initializeMemoryGame() {
  // Setup cards and randomize positions here
}

function checkForMatch(card1, card2) {
  // Check if selected cards match
}
