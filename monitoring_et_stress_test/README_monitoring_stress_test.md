# Pour lancer le monitoring et le stress test:

Dans 4 terminaux différents (penser à bien activer l'envt virtuel dans chacun d'eux), lancer respectivement:

- Application Django :
`python3 manage.py runserver`

- Serveur MLFlow pour logger les métriques mesurées :
`mlflow server --host 127.0.0.1 --port 8080`
Accéder à http://localhost:8080 dans un navigateur pour accéder à l'interface du serveur

- Script de monitoring (mesure les métriques, les envoie vers mlflow, envoie une alerte via un bot discord si les mesures deviennent trop élevées ):
`python3 monitoring_et_stress_test/monitor_and_alert_main.py`

- Locust (outil de stress test qui swarme l'application selon des tâches définies et réalise quelques mesures)
`locust -f locustfile.py --host http://localhost:8000 --users 1000 --spawn-rate 1`
Accéder à http://localhost:8089 dans un navigateur pour accéder à l'interface du serveur.
Pour lancer un stress test, cliquer sur 'start swarming'. Il est possible de modifier le nb d'utilisateurs et le spawn rate. Ne pas modifier l'host.