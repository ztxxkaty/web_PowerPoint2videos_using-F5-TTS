document.addEventListener("DOMContentLoaded", function () {
    // 1)音频上传
    const btnUploadAudio = document.getElementById("upload-audio");
    btnUploadAudio.addEventListener("click", uploadAudioFile);

    // 2)录制音频
    // const btnStartRecord = document.getElementById("start-record");
    // btnStartRecord.addEventListener("click", startRecording);

    // const btnStopRecord = document.getElementById("stop-record");
    // btnStopRecord.addEventListener("click", stopRecording);

    // const btnPlayRecord = document.getElementById("play-record");
    // btnPlayRecord.addEventListener("click", playRecording);

    // const btnUploadRecord = document.getElementById("upload-record");
    // btnUploadRecord.addEventListener("click", uploadRecording);

    //  3) PPT上传
    const btnUploadPPT = document.getElementById("upload-ppt");
    btnUploadPPT.addEventListener("click", uploadPPTFile);
});

// ===============================
// 音频上传
// ===============================
function uploadAudioFile() {
    const fileInput = document.getElementById("audio-file");
    const file = fileInput.files[0];

    if (!file) {
        alert("请先选择要上传的音频文件！");
        return;
    }

    const formData = new FormData();
    formData.append("audio", file);

    fetch("/upload_audio", {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.message == 'Audio uploaded successfully') {
                alert("音频上传成功！");
            } else {
                alert("音频上传失败！");
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("音频上传失败！");
        });
}

// ===============================
// 录制音频
// ===============================

// ===============================
// PPT上传
// ===============================
function uploadPPTFile() {
    const fileInput = document.getElementById("ppt-file");
    const file = fileInput.files[0];

    if (!file) {
        alert("请先选择要上传的PPT文件！");
        return;
    }

    const formData = new FormData();
    formData.append("ppt", file);

    fetch("/upload_PPT", {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.message == 'PPT uploaded successfully') {
                alert("PPT上传成功！");
            } else {
                alert("PPT上传失败！");
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("PPT上传失败！");
        });
}

    
