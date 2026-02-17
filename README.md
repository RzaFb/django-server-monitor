
# django-server-monitor

**django-server-monitor** is a robust, extensible, and production-ready web-based server monitoring and scheduling system built with Django and Celery. It is designed to help you track the health and uptime of any number of servers or endpoints, automate periodic health checks, and provide a unified interface for monitoring, management, and reporting.

This project combines the power of Django’s web framework with Celery’s distributed task queue to deliver a scalable monitoring solution. It features a user-friendly web interface, a RESTful API for integration with other systems, and a background task system for running checks and scheduled jobs asynchronously. All monitoring data is stored in a relational database (default: SQLite, but easily swappable for PostgreSQL, MySQL, etc.), and the system is easily extensible for custom checks, notifications, or reporting.

**Key capabilities include:**
- Registering and managing a list of servers or endpoints to monitor
- Automated, scheduled health checks with customizable intervals
- Real-time and historical status tracking for each server
- Web-based dashboard and Django admin for management
- REST API for integration and automation
- Asynchronous, non-blocking background task execution
- Extensible architecture for custom checks, alerting, and reporting

This project is ideal for small teams, IT administrators, or developers who need a lightweight but powerful monitoring solution that can be deployed on-premises or in the cloud, and easily adapted to new requirements.

---

## Table of Contents
- [Usage](#usage)
   - [Web Interface](#web-interface)
   - [API Endpoints](#api-endpoints)
   - [Background Tasks](#background-tasks)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Testing & CI](#testing--ci)
- [Acknowledgements](#acknowledgements)

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



3. **Start Celery Beat (for scheduled tasks)**

---

## Acknowledgements
- [Django](https://www.djangoproject.com/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- Open source contributors

---


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
