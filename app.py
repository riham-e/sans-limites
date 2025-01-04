from flask import Flask, request

app = Flask(__name__)
# Route pour traiter les données du formulaire
@app.route('/contact', methods=['POST'])
def contact():
    # Récupérer les données envoyées par le formulaire
    Nom = request.form['Nom']
    email = request.form['email']
    sujet = request.form['sujet']
    message = request.form['Message']
    
    # Message de confirmation personnalisé
    return f"""
    <html>
        <head>
            <style>
                /* Style pour la page */
                body {{
                    background-color: #470069; /* Couleur de fond de la page */
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    color: #fff; /* Couleur de texte blanche pour le titre */
                    text-align: center;
                }}

                /* Couleur du paragraphe */
                p {{
                    color: #000000; /* Couleur du texte du paragraphe */
                    font-size: 20px;
                }}
                
                h2 {{
                    color: #000000;
                    font-size: 40px;
                }}
                
                h1 {{
                    color: #FF01DB;
                    font-size: 40px;
                }}

                h4 {{
                    color: #FF01DB;
                    font-size: 20px;
                }}

                /* Animation de fondu pour le texte */
                .fade-in {{
                    animation: fadeIn 3s ease-in-out;
                }}

                @keyframes fadeIn {{
                    from {{
                        opacity: 0;
                    }}
                    to {{
                        opacity: 1;
                    }}
                }}

                /* Nouvelle animation de déplacement horizontal */
                .slide-in {{
                    animation: slideIn 3s ease-out;
                }}

                @keyframes slideIn {{
                    from {{
                        transform: translateX(-100%);
                        opacity: 0;
                    }}
                    to {{
                        transform: translateX(0);
                        opacity: 1;
                    }}
                }}
                
                /* Style pour afficher Merci et Nom sur la même ligne */
                .inline {{
                    display: inline;
                    color: #FF01DB; /* Couleur pour le Nom et l'email */
                }}
            </style>
        </head>
        <body>
            <div class="fade-in">
                <h2 class="slide-in"><span class="inline">Merci</span> <span class="inline">{Nom}</span></h2>
                <p class="slide-in">Nous avons bien reçu votre message.</p>
                <p class="slide-in">Demain, vous recevrez une réponse à votre réservation dans votre <h4 class="slide-in">{email}</h4>.</p>
            </div>
        </body>
    </html>
    """
if __name__ == '__main__':
    app.run(debug=True)
