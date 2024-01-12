# app.py
'''
Script de monitoring d'un site / application web.
Paramétrage des métriques à monitirer, des seuils et envoi d'alerte mail et discord
Variables d'environnement crées dans .env

'''

import mlflow
import requests
import time
import smtplib
import os
import psutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import schedule

# chargement des variables d'environnement depuis le fichier dotenv
load_dotenv()

# Configuration des seuils d'alerte (à ajuster selon vos besoins)
THRESHOLD_RESPONSE_TIME = 1  # en secondes
THRESHOLD_ERROR_RATE = 0.05  # 5%
THRESHOLD_CPU_UTILIZATION = 80  # en pourcentage
THRESHOLD_MEMORY_UTILIZATION = 80  # en pourcentage
THRESHOLD_STORAGE_UTILIZATION = 80  # en pourcentage


# Affectation des variables d'environnement
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")


# COnfiguration MLflow
# set l'uri pour envoyer le modele
mlflow.set_tracking_uri(uri="http://127.0.0.1:8080") 
mlflow.set_experiment("Monitoring de mon app")


# Fonction d'envoi de notification sur serveur Discord
def send_alert_discord(subject, body):
    payload = {
        "content": f"**{subject}**\n{body}"
    }
    requests.post(DISCORD_WEBHOOK_URL, json=payload)


# Fonction d'envoi de message sur serveur Gmail
def send_alert_email(subject, body):
    # Configuration du message
    message = MIMEMultipart()
    message['From'] = SMTP_USERNAME
    message['To'] = EMAIL_RECEIVER
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    
    # Connexion au serveur SMTP
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    
    # Authentification avec le nom d'utilisateur et le mot de passe d'application
    server.login(SMTP_USERNAME, SMTP_PASSWORD)

    # Envoi du message
    server.sendmail(SMTP_USERNAME, EMAIL_RECEIVER, message.as_string())

    # Fermeture de la connexion
    server.quit()


# Fonction de monitoring d'une source
def monitor_website(url):
    # rajouter authentification ici

    session = requests.Session()
    # print(session)
    response = session.get("http://127.0.0.1:8000/login/")
    csrf_token = response.cookies["csrftoken"]
    # print(response)

    data = {
        "username": "M01",
        "motDePasse": "M01", 
        'csrfmiddlewaretoken' : csrf_token
    }

    response = session.post("http://127.0.0.1:8000/login/", data=data)
    # print(response.url)





    # print("-----")
    # Récupérer le CSRF token de la route login
    # response = requests.get("http://127.0.0.1:8000/login/")
    # csrf_token = response.cookies.get("csrftoken")
    # print(csrf_token)

    # # Envoyer une requête POST avec les données de connexion
    # data = {
    #     "username": "M01",
    #     "motDePasse": "M01"
    # }
    # response = requests.post("http://127.0.0.1:8000/login/", data=data, headers={"X-CSRFToken": csrf_token})

    start_time = time.time()
    
    # Test envoi alerte
    # send_alert_discord("MLOps", "Monitoring en cours ... ")
    # send_alert_email("MLOps", "Monitoring en cours ... ")

    try:
        REDIRECT_URL = url
        response = session.get(REDIRECT_URL)
  
        # print(url)
        # print(response.url)
        # title = response.text.split("<title>")[1].split("</title>")[0]
        # print(title)
        # print(response)
        response_time = time.time() - start_time

        # Log des métriques avec MLflow
        mlflow.log_metric("response_time", response_time)

        # Vérification des seuils d'alerte
        if response_time > THRESHOLD_RESPONSE_TIME:
            send_alert_discord(":warning: Alerte - Temps de réponse élevé", f"Le temps de réponse est élevé : {response_time} secondes")
            # send_alert_email("Alerte - Temps de réponse élevé", f"Le temps de réponse est élevé : {response_time} secondes")
        
        # Mesurer le taux d'erreur
        if response.status_code != 200:
            mlflow.log_metric("error_rate", 1)
        else:
            mlflow.log_metric("error_rate", 0)
        
        # Mesurer la disponibilité
        mlflow.log_metric("availability", 1)

        # Mesurer la bande passante
        bandwidth = len(response.content) / (response_time * 1024)  # en Ko/s
        mlflow.log_metric("bandwidth", bandwidth)

        # Mesurer l'utilisation des ressources
        cpu_utilization = psutil.cpu_percent()
        memory_utilization = psutil.virtual_memory().percent
        storage_utilization = psutil.disk_usage('/').percent

        mlflow.log_metric("cpu_utilization", cpu_utilization)
        mlflow.log_metric("memory_utilization", memory_utilization)
        mlflow.log_metric("storage_utilization", storage_utilization)        

                # Vérification des seuils d'alerte
        if cpu_utilization > THRESHOLD_CPU_UTILIZATION:
            send_alert_discord(":warning: Alerte - utilisation CPU élevée", f"L'utilisation du CPU est élevée : {cpu_utilization} ")
            # send_alert_email("Alerte - Temps de réponse élevé", f"Le temps de réponse est élevé : {response_time} secondes")
        
    # Alerte si connexion impossible
    except Exception as e:
        send_alert_discord(":warning: Alerte - Erreur de requête HTTP", f"Erreur lors de la requête HTTP : {e}")
        # send_alert_email("Alerte - Erreur de requête HTTP", f"Erreur lors de la requête HTTP : {e}")
        print(f"Erreur lors de la requête HTTP : {e}")

def monitor_mlflow():
    print("Monitoring django app ...")
    mlflow.start_run()
    monitor_website(url = "http://127.0.0.1:8000/tableVisualisation/")
    mlflow.end_run()


schedule.every(10).seconds.do(monitor_mlflow)

while True:
    schedule.run_pending()
    time.sleep(1)



