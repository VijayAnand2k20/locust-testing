from locust import HttpUser, task, between
import random

class MyUser(HttpUser):
    wait_time = between(1, 5)
    host = "https://rweb-testing.up.railway.app"

    @task
    def my_task(self):
        self.client.get("/")
        self.client.get("/research")
        self.client.get("/am")
        self.client.get("/events/ideathon23/themes")
        self.client.get("/participant-signup")
        self.client.get("/login")