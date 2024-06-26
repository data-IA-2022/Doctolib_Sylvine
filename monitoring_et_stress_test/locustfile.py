from locust import HttpUser, task, constant, between
import locust

''' 
pour lancer le serveur Locust à partir de ce script:
locust -f locustfile.py --host http://localhost:8000 --users 1000 --spawn-rate 1
'''

class MyUser(HttpUser):
    wait_time = constant(1)
    # connexion de l'utilisateur
    def on_start(self):
        self.login()

    def login(self):
        # login to the application
        response = self.client.get('/login/')
        csrftoken = response.cookies['csrftoken']
        self.client.post('/login/',
                         {'username': 'M01', 'motDePasse': 'M01'},
                         headers={'X-CSRFToken': csrftoken})
        
    @task()
    def my_task(self):
        # self.client.get("/accueil")
        self.client.get("/tableVisualisation")


