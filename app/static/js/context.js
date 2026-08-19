const uploadForm = document.getElementById('context-upload-form')
const uploadButton = document.getElementById('context-upload-button')

const uploadStatus = document.getElementById('upload-status')

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

