# -*- coding: utf-8 -*-
"""
Created on Mon May 12 14:49:56 2025

@author: Utilisateur
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def accueil():
    return "<h1>Bienvenue sur mon site Flask !</h1><p>C'est simple et stylé 😎</p>"

@app.route('/about')
def about():
    return "<h1>À propos</h1><p>Voici un site Flask créé pour apprendre le développement web !</p>"



if __name__ == '__main__':
    app.run(debug=True)


