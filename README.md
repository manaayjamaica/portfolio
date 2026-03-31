# Jamaica Mana-ay — Personal Portfolio Website

A dynamic personal portfolio built with **Django**, featuring a warm amber parchment design and full-width scroll sections.

🌐 **Live Site:** https://jamaicamanaay.pythonanywhere.com  
📁 **GitHub Repo:** https://github.com/jamaicamanaay/portfolio

---

## Features
- **Home** — Full-width hero with profile photo, skill strip, featured projects & CTA
- **About** — Personal background, career goals, quick-info card
- **Skills** — Categorized skills with gradient progress bars (Programming, Web, CS, Tools)
- **Projects** — Numbered list layout with 4 projects, tech tags & GitHub links
- **Education** — Card-based academic timeline
- **Contact** — Contact form (saves to DB) + social links
- **Django Admin** — Full admin panel for all content
- **Responsive** — Mobile-friendly pill nav that collapses to a drawer

---

## Tech Stack
| Layer | Technology |
|-------|------------|
| Backend | Python 3, Django |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite (dev) / MySQL (prod) |
| Hosting | PythonAnywhere |
| Version Control | GitHub |

---

## Local Setup

```bash
# 1. Clone
git clone https://github.com/jamaica-mana-ay/portfolio.git
cd jamaica_portfolio

# 2. Virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# 3. Install
pip install -r requirements.txt

# 4. Database
python manage.py makemigrations
python manage.py migrate

# 5. Admin user
python manage.py createsuperuser

# 6. Run
python manage.py runserver
---

## PythonAnywhere Deployment

### 1. Create account — username: `jamaicamanaay`
### 2. Open Bash console & clone
```bash
git clone https://github.com/manaayjamaica/portfolio.git
mkvirtualenv --python=/usr/bin/python3.10 venv
cd jamaica_portfolio
pip install -r requirements.txt
```
### 3. Web tab → Manual config → Python 3.10
- Source code: `/home/jamaicamanaay/portfolio`

### 4. Edit WSGI file
```python
import sys, os
path = '/home/jamaicamanaay/portfolio'
if path not in sys.path: sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_project.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
### 5. Static files (Web tab)
| URL | Directory |
|-----|-----------|
| `/static/` | `/home/jamaicamanaay/jamaica_portfolio/staticfiles` |
| `/media/` | `/home/jamaicamanaay/jamaica_portfolio/media` |

```bash
python manage.py collectstatic
python manage.py migrate
python manage.py createsuperuser
```
### 6. Reload → Live at https://jamaica_mana-ay.pythonanywhere.com

