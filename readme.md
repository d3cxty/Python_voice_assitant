<h1>AI-Enhanced Voice-Activated Command Launcher</h1>

<h2>What is this project?</h2>
<p>This is a simple voice assistant I made with Python. It listens to what you say and does things like:</p>
<ul>
    <li>Open Notepad</li>
    <li>Open a web browser (like Chrome)</li>
    <li>Open YouTube</li>
    <li>Open Calculator, Paint, or File Explorer</li>
    <li>Play music (using Windows Media Player)</li>
    <li>Shut down your computer (be careful!)</li>
    <li>Say "Hello" back to you</li>
</ul>
<p>I’m new to programming, so this is a learning project for me! It uses <code>speech_recognition</code> to hear your voice and <code>nltk</code> to understand what you mean.</p>

<h2>How does it work?</h2>
<ol>
    <li>The program listens to your voice using your microphone.</li>
    <li>It turns your voice into words (like "open notepad").</li>
    <li>It uses <code>nltk</code> to break the words apart and figure out what you want (like "open" is the action and "notepad" is the thing).</li>
    <li>It does the action (like opening Notepad on your computer).</li>
</ol>

<h2>What you need to run this</h2>
<ul>
    <li>A computer with Windows (it uses Windows commands like <code>start notepad</code>).</li>
    <li>A microphone (so it can hear you).</li>
    <li>Internet (it uses Google’s Speech API to understand your voice).</li>
    <li>Python installed (I’m using Python 3.13.2).</li>
</ul>

<h2>How to set it up</h2>
<ol>
    <li>
        <p><strong>Install Python</strong>:</p>
        <p>If you don’t have Python, download it from <a href="https://www.python.org/downloads/">python.org</a> and install it.</p>
        <p>Make sure to check "Add Python to PATH" during installation.</p>
    </li>
    <li>
        <p><strong>Clone or download this project</strong>:</p>
        <p>If you’re using GitHub, click the green "Code" button and download the ZIP, or clone it with:</p>
