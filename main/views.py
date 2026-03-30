from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, Education, ContactMessage

def get_profile():
    return Profile.objects.first()

def home(request):
    profile = get_profile()
    featured = Project.objects.filter(featured=True)[:3]
    skills_preview = Skill.objects.all()[:6]
    return render(request, 'main/home.html', {
        'profile': profile,
        'featured_projects': featured,
        'skills_preview': skills_preview,
    })

def about(request):
    return render(request, 'main/about.html', {'profile': get_profile()})

def skills(request):
    all_skills = Skill.objects.all()
    categories = {}
    for s in all_skills:
        label = dict(Skill.CATEGORY_CHOICES).get(s.category, s.category)
        categories.setdefault(label, []).append(s)
    return render(request, 'main/skills.html', {'profile': get_profile(), 'categories': categories})

def projects(request):
    return render(request, 'main/projects.html', {
        'profile': get_profile(),
        'projects': Project.objects.all(),
    })

def education(request):
    return render(request, 'main/education.html', {
        'profile': get_profile(),
        'education_list': Education.objects.all(),
    })

def contact(request):
    profile = get_profile()
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        msg = request.POST.get('message', '').strip()
        if name and email and msg:
            ContactMessage.objects.create(name=name, email=email, subject=subject, message=msg)
            messages.success(request, "Your message was sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Please fill in all required fields.")
    return render(request, 'main/contact.html', {'profile': profile})
