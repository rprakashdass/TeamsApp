from django.db import models

class Project(models.Model):
    # status = ('Completed','Assigned','Drooped')
    project_title = models.CharField(max_length=50, default='project title')
    project_details = models.TextField()
    # status = 
    # domain = models.CharField(max_length=50)
    announced_date = models.DateTimeField("Announced Date", auto_now_add=True)
    completion_date = models.DateTimeField("Completion Date", auto_now_add=False)

    def __str__(self):
        return self.project_title

class Contributor(models.Model):
    contributor_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150, unique=True)
    country_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.contributor_name

class Team(models.Model):
    team_name = models.CharField(max_length=25)
    members = models.ManyToManyField(Contributor)
    completed_tasks = models.IntegerField(default=0)
    no_of_task_assigned = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name
    
class Task(models.Model):
    task_title = models.CharField(max_length=70)
    announced_date = models.DateTimeField("Announced Date", auto_now_add=True)
    completion_date = models.DateTimeField("Completion Date", auto_now_add=False)
    assigned_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # associated_project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title

    
# from tasks.models import Tasks
# t=Tasks(task_title='read',) 
# t