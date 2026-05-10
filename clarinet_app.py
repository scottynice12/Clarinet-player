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
    <div class="keys">
        <div class="key" data-freq="329.63">E4</div>
        <div class="key" data-freq="369.99">F#4</div>
        <div class="key" data-freq="392.00">G4</div>
        <div class="key" data-freq="440.00">A4</div>
        <div class="key" data-freq="493.88">B4</div>
        <div class="key" data-freq="523.25">C5</div>
        <div class="key" data-freq="587.33">D5</div>
        <div class="key" data-freq="659.25">E5</div>
    </div>
    <div class="status">🎵 Click keys → real clarinet sound</div>
</div>
<script>
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

    function playNote(freq) {
        if (audioCtx.state === 'suspended') {
            audioCtx.resume();
        }
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'triangle';
        osc.frequency.value = freq;
        gain.gain.value = 0.3;
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        const now = audioCtx.currentTime;
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.8);
        osc.start();
        osc.stop(now + 0.8);
    }

    document.querySelectorAll('.key').forEach(key => {
        key.addEventListener('click', () => {
            const freq = parseFloat(key.getAttribute('data-freq'));
            playNote(freq);
        });
    });

    // Unlock audio on first click anywhere
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
        
