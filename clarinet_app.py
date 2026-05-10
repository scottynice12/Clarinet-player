from flask import Flask

app = Flask(__name__)

HTML_CODE = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Flask Clarinet</title>
    <style>
        body { background: #0a0c15; font-family: sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
        .clarinet { background: #1e2235; padding: 30px; border-radius: 48px; }
        .keys { display: flex; gap: 12px; flex-wrap: wrap; justify-content: center; }
        .key { background: #f4f6fc; width: 70px; height: 200px; border-radius: 20px; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 20px; font-weight: bold; font-size: 1.2rem; cursor: pointer; box-shadow: 0 6px 0 #8f9bb3; transition: 0.05s linear; }
        .key:active { transform: translateY(4px); box-shadow: 0 2px 0 #6b7a97; }
        .status { color: #ccddf8; text-align: center; margin-top: 20px; }
    </style>
</head>
<body>
<div class="clarinet">
    <div class="keys" id="keys"></div>
    <div class="status">🎵 Click keys → clarinet-like square wave (no internet needed)</div>
</div>
<script>
    // Create audio context (will be resumed on first click)
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

    // Frequency mappings for clarinet range (E4 to E5)
    const noteFreq = {
        'E4': 329.63,
        'F#4': 369.99,
        'G4': 392.00,
        'A4': 440.00,
        'B4': 493.88,
        'C5': 523.25,
        'D5': 587.33,
        'E5': 659.25
    };
    const labels = ['E4', 'F#4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5'];

    function playNote(freq) {
        if (audioCtx.state === 'suspended') {
            audioCtx.resume();
        }
        // Create oscillator and gain (for envelope)
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'triangle'; // clarinet-like (triangle is softer than square)
        osc.frequency.value = freq;
        gain.gain.value = 0.3;
        
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        
        // Quick envelope: fade out after 0.6 seconds
        const now = audioCtx.currentTime;
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.8);
        
        osc.start();
        osc.stop(now + 0.8);
    }

    const container = document.getElementById('keys');
    labels.forEach(label => {
        const btn = document.createElement('div');
        btn.className = 'key';
        btn.innerText = label;
        btn.onclick = () => playNote(noteFreq[label]);
        container.appendChild(btn);
    });

    // Unlock audio on any user gesture
    document.body.addEventListener('click', () => {
        if (audioCtx.state === 'suspended') audioCtx.resume();
    });
</script>
</body>
</html>'''

@app.route('/')
def clarinet():
    return HTML_CODE

if __name__ == '__main__':
    app.run(debug=True)
