document.getElementById('generate-audio').addEventListener('click', () => {
    const text = document.getElementById('arabic-text').value;

    fetch('http://127.0.0.1:5000/text_to_speech', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        console.log("File URL: ", data.file_url); // Log the file URL
        const audioPlayer = document.getElementById('audio-player');
        audioPlayer.src = data.file_url;
        document.getElementById('play-audio').style.display = 'block';
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('play-audio').addEventListener('click', () => {
    const audioPlayer = document.getElementById('audio-player');
    audioPlayer.play();
});
