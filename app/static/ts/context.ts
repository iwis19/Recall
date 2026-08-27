import { requireElement } from "./shared/dom";

const uploadForm = requireElement<HTMLFormElement>('#context-upload-form');
const uploadButton = requireElement<HTMLInputElement>('#context-upload-button');
const uploadStatus = requireElement<HTMLDivElement>('#upload-status');

fetch("/context/warmup", {
    method: "POST"
}).then(function (response) {
    if (!response.ok) {
        console.error("Unable to warmup embedding function");
    } else {
        console.log("Successfully warmed up embeddings");
    }
}).catch(function (error){
    console.error("Could not reach warmup endpoint", error);
});

uploadForm.addEventListener('submit', function() {

    const defaultUploadingText = "Uploading";
    let uploadingDotCount = 0;

    function incrementDot() {
        uploadingDotCount = uploadingDotCount % 3 + 1;
        uploadStatus.textContent = `${defaultUploadingText}${".".repeat(uploadingDotCount)}`;
    }
    
    incrementDot()
    const dotInterval = setInterval(incrementDot, 500);
    uploadButton.disabled = true;

});

