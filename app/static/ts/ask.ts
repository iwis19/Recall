import { requireElement } from "./shared/dom";

const askForm = requireElement<HTMLFormElement>('#ask-form');
const answerOutput = requireElement<HTMLDivElement>('#answer-output');
const submitButton = requireElement<HTMLInputElement>('#ask-submit-button');

askForm.addEventListener("submit", async function (event) {
    /*
    a form has built in browser behavior, so when submitted, the browser:

    - reads form fields
    - sends them using action and method
    - navigates or reloads the resulting page
    */
    event.preventDefault();

    const formData = new FormData(askForm);

    let loadingDotCount = 0;
    const defaultLoadingText = "Thinking";

    function incrementDot() {
        loadingDotCount = loadingDotCount % 3 + 1;
        answerOutput.textContent = `${defaultLoadingText}${".".repeat(loadingDotCount)}`;
    }

    incrementDot();
    const dotInterval = setInterval(incrementDot, 500);
    submitButton.disabled = true;

    try {
        const response = await fetch("/ask/api", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        answerOutput.textContent = response.ok ? data.response : data.error;
    } catch {
        answerOutput.textContent = "Could not reach the server."
    } finally {
        clearInterval(dotInterval)
        loadingDotCount = 0
        submitButton.disabled = false;
    }

});
