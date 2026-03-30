from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    tagline = models.CharField(max_length=220)
    bio = models.TextField()
    career_goals = models.TextField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=100, blank=True, default="Philippines")
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    profile_photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    def __str__(self): return self.name
    class Meta: verbose_name = "Profile"

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('web', 'Web Technologies'),
        ('database', 'Databases'),
        ('cs', 'CS Fundamentals'),
        ('tools', 'Tools & Software'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    proficiency = models.IntegerField(default=80)
    order = models.IntegerField(default=0)
    def __str__(self): return self.name
    class Meta: ordering = ['order', 'name']

class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    technologies = models.CharField(max_length=250)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    def __str__(self): return self.title
    def tech_list(self): return [t.strip() for t in self.technologies.split(',')]
    class Meta: ordering = ['order', 'title']

class Education(models.Model):
    school = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    field_of_study = models.CharField(max_length=100, blank=True)
    year_start = models.IntegerField()
    year_end = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    def __str__(self): return f"{self.degree} – {self.school}"
    def year_range(self): return f"{self.year_start} – {self.year_end if self.year_end else 'Present'}"
    class Meta: ordering = ['-year_start']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    def __str__(self): return f"From {self.name} ({self.email})"
    class Meta: ordering = ['-sent_at']
