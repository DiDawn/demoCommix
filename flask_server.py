from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Interface ultra-simple avec un champ de saisie
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<body>
    <h2>Outil de Diagnostic Réseau (Ping)</h2>
    <form method="GET">
        Adresse IP : <input type="text" name="address">
        <input type="submit" value="Tester">
    </form>
    <pre>{{ output }}</pre>
</body>
</html>
'''

@app.route('/')
def index():
    address = request.args.get('address')
    output = ""
    if address:
        # LA FAILLE : On concatène directement l'entrée utilisateur dans une commande shell
        # Exemple de ce qui sera exécuté : "ping -c 1 127.0.0.1"
        command = f"ping -c 1 {address}"
        output = os.popen(command).read() 
    
    return render_template_string(HTML_TEMPLATE, output=output)

if __name__ == '__main__':
    # On lance le serveur en local sur le port 5000
    app.run(host='127.0.0.1', port=5000, debug=True)
