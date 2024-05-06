# Installation et paramétrage des outils de monitoring et résolution de test :
Suivre les indications dans le document `Annexe livrable E5.odt`. 


# Pour lancer le monitoring et le stress test une fois l'installation effectuée :
Dans des terminaux différents (penser à bien activer l'envt virtuel dans chacun d'eux), lancer respectivement:

- Application Django :
```bash
python3 manage.py runserver
```

- Serveur Prometheus :
```bash
./prometheus –config.file=prometheus.yml
```

- Serveur Grafana :
```bash
sudo /bin/systemctl start grafana-server
```

- Locust (outil de stress test qui swarme l'application selon des tâches définies et réalise quelques mesures)
```bash
locust -f locustfile.py --host http://localhost:8000 --users 1000 --spawn-rate 1
```
Accéder à http://localhost:8089 dans un navigateur pour accéder à l'interface du serveur.
Pour lancer un stress test, cliquer sur 'start swarming'. Il est possible de modifier le nb d'utilisateurs et le spawn rate. Ne pas modifier l'host.