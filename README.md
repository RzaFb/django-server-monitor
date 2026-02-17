# django-server-monitor

A scalable, web-based server monitoring and scheduling system built with Django and Celery.

---

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [Web Interface](#web-interface)
  - [API Endpoints](#api-endpoints)
  - [Background Tasks](#background-tasks)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [Testing & CI](#testing--ci)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

---

## Features
- **Server Health Monitoring**: Track status and uptime of registered servers.
- **Automated Periodic Checks**: Schedule health checks using Celery and Celery Beat.
- **Web API**: Query server status, add/remove servers, and view monitoring results.
- **Admin Interface**: Manage servers and results via Django admin.
- **Asynchronous Task Processing**: Run checks in the background without blocking the web app.
- **SQLite Database**: Store server info and monitoring results.
- **Extensible**: Easily add new monitoring logic or notification features.

---

## Demo
> *Screenshots and demo GIFs can be added here.*

---

## Installation

### Prerequisites
- Python 3.8+
- pip
- (Optional) Redis or RabbitMQ for Celery broker

### Clone the Repository
```bash
git clone https://github.com/yourusername/django-server-monitor.git
cd django-server-monitor
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Apply Migrations
```bash
python manage.py migrate
```

### Create Superuser (for admin access)
```bash
python manage.py createsuperuser
```

---

## Quick Start

1. **Start Django Server**
   ```bash
   python manage.py runserver
   ```
2. **Start Celery Worker**
   ```bash
   celery -A monitor_project worker --loglevel=info
   ```
3. **Start Celery Beat (for scheduled tasks)**
   ```bash
   celery -A monitor_project beat --loglevel=info
   ```
4. **Access Admin Interface**
   - Visit `http://localhost:8000/admin/` and log in with your superuser credentials.

---

## Usage

### Web Interface
- Add, edit, and delete servers to monitor.
- View server status and monitoring history.

### API Endpoints
- `GET /api/servers/` — List all monitored servers.
- `POST /api/servers/` — Add a new server.
- `GET /api/servers/<id>/` — Get status of a specific server.
- (Custom endpoints can be added in `views.py` and `urls.py`.)

### Background Tasks
- Health checks are scheduled and run automatically using Celery and Celery Beat.
- Results are stored in the database and accessible via web/API.

---

## Project Structure
```
monitor_project/
│
├── celerybeat-schedule.*        # Celery Beat schedule files
├── db.sqlite3                   # SQLite database
├── manage.py                    # Django management script
├── monitor_project/             # Django project root
│   ├── celery.py                # Celery configuration
│   ├── settings.py              # Django settings
│   ├── tasks.py                 # Celery tasks for health checks
│   ├── urls.py                  # Project URLs
│   ├── wsgi.py, asgi.py         # Server entry points
│   └── ...
├── server/                      # Django app for server monitoring
│   ├── models.py                # Database models
│   ├── views.py                 # Web/API views
│   ├── urls.py                  # App URLs
│   ├── admin.py                 # Admin interface
│   └── migrations/              # Database migrations
└── README.md                    # This file
```

---

## Configuration
- Celery broker and backend can be set in `monitor_project/settings.py`.
- Scheduled tasks are managed by Celery Beat (`celerybeat-schedule.*` files).
- Customize monitoring intervals and logic in `tasks.py`.

---

## Contributing
Contributions are welcome!
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
- Fork the repo and create your branch (`git checkout -b feature/your-feature`)
- Commit your changes (`git commit -am 'Add new feature'`)
- Push to the branch (`git push origin feature/your-feature`)
- Open a Pull Request

---

## Testing & CI
- Run tests locally:
  ```bash
  python manage.py test
  ```
- Automated tests and linting can be set up via GitHub Actions or other CI tools.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements
- [Django](https://www.djangoproject.com/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- Open source contributors

---

## Contact
For questions, suggestions, or support, please open an issue or contact [rzafrhb@gmail.com](mailto:rzafrhb@gmail.com).

---

django-server-monitor: Reliable, automated server health tracking for your infrastructure.
