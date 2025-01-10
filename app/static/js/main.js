let isRecording = false;
let updateInterval = 1000;
let timer;
let startTime;

function updateMetrics() {
    fetch('/metrics')
        .then(response => response.json())
        .then(data => {
            document.getElementById('cpu').textContent = `${data.cpu}%`;
            document.getElementById('ram').textContent = `${data.ram}%`;
            document.getElementById('disk').textContent = `${data.disk}%`;
            
            if (isRecording) {
                fetch('/start_recording', {
                    method: 'POST'
                });
            }
        });
}

function updateTimer() {
    const now = new Date();
    const diff = Math.floor((now - startTime) / 1000);
    const hours = Math.floor(diff / 3600).toString().padStart(2, '0');
    const minutes = Math.floor((diff % 3600) / 60).toString().padStart(2, '0');
    const seconds = (diff % 60).toString().padStart(2, '0');
    document.getElementById('timer').textContent = `${hours}:${minutes}:${seconds}`;
}

document.getElementById('recordButton').addEventListener('click', function() {
    if (!isRecording) {
        isRecording = true;
        this.textContent = 'Stop Recording';
        startTime = new Date();
        document.getElementById('timer').style.display = 'inline';
        timer = setInterval(updateTimer, 1000);
    } else {
        isRecording = false;
        this.textContent = 'Start Recording';
        document.getElementById('timer').style.display = 'none';
        clearInterval(timer);
    }
});

document.getElementById('historyButton').addEventListener('click', function() {
    const historyDiv = document.getElementById('history');
    if (historyDiv.style.display === 'none') {
        fetch('/get_history')
            .then(response => response.json())
            .then(data => {
                const tbody = document.querySelector('#historyTable tbody');
                tbody.innerHTML = '';
                data.forEach(record => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${record.timestamp}</td>
                        <td>${record.cpu}%</td>
                        <td>${record.ram}%</td>
                        <td>${record.disk}%</td>
                    `;
                    tbody.appendChild(row);
                });
                historyDiv.style.display = 'block';
            });
    } else {
        historyDiv.style.display = 'none';
    }
});

setInterval(updateMetrics, updateInterval);
updateMetrics(); 