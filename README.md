Make sure you have Python 3.14 and Flask installed

text
pip install flask
Locate the folder where clarinet_app.py is saved

If you downloaded it or saved it manually, remember where (e.g., Documents\my_projects\clarinet_app.py).

Open File Explorer and go to that folder.

Open a terminal in that folder

Windows: Click the address bar in File Explorer, type cmd, and press Enter.

Mac/Linux: Right-click inside the folder → "Open in Terminal".

Run the app

text
python clarinet_app.py(file you name it)
Open your browser and go to:

example text
http://13490234
(that's your own computer – the number is the port number Flask uses)

Click the white keys – each one plays a different clarinet‑like note.

To stop the server
Press Ctrl + C in the terminal.

Notes
The first click on the page also "unlocks" audio (browser security rule).

If you don't hear sound, check your computer's volume.

Troubleshooting
"Port something already in use" – close other Flask apps or change the port in clarinet_app.py (last line: app.run(debug=True, port=something)).

No keys appear – hard refresh the page (Ctrl + F5).

That should cover it. Want me to add a note about using cd in the terminal instead of File Explorer for advanced users?

