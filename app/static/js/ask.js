const form = document.getElementById('question_submission');
const answerDiv = document.getElementById('answer')

form.addEventListener('submit', async function (event) {
    event.preventDefault();

    const formData = new FormData(form);
    answerDiv.textContent = "Thinking...";

    const response = await fetch("/ask/api", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    
    answerDiv.textContent = data.response;
});

