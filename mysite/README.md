# A simple todo app

This is a simple todo app built fully with Django.

## Installation

Clone the repository and navigate to the project directory:
    
```bash
git clone https://github.com/Jesulayomy/d_basics.git
cd d_basics/mysite/
```

Create a virtual environment and install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Apply migrations and create a super user account, then run the server:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
. . .

python manage.py runserver
> Watching for file changes with StatReloader
> Performing system checks...

> System check identified no issues (0 silenced)
```


## Deployment

Deployed on a digtal ocean server with nginx and gunicorn

### Specifications
- Ubuntu 22.04
- Python 3.10
- Nginx nginx/1.18.0

### Nginx configuration

Configure the server block in the `/etc/nginx/sites-available/mysite` file as in mysite.conf

```nginx
server {
	listen 80;
	server_name todos.example.com;

	location = /favicon.ico { access_log off; log_not_found off; }

	location / {
		include proxy_params;
		proxy_pass http://<YOUR_SERVER_PRIVATE_IP>:<PORT=8009>/;
	}
}
```

Activate the server block and restart nginx:

```bash
sudo ln -s /etc/nginx/sites-available/mysite /etc/nginx/sites-enabled
sudo systemctl restart nginx
```

> Because nginx and django cannot easily append a route as in example.com/todo/ because when rendering, redirecting to a route will not append the /todo/ path to the url, the only option is to use a subdomain as in todos.example.com. Or change my mind.

<!-- github.com/jesulayomy/d_basics/blob/main/mysite/mysite.conf#L2-L4 -->

### Gunicorn configuration
Modify the gunicorn configuration file in the `mysite/gunicorn.py` file as in gunicorn.py

```python
command = '/full/path/to/project/.venv/bin/gunicorn'
pythonpath = '/full/path/to/project/mysite'
bind = 'IP:PORT'
# IP can be 0.0.0.0, localhost or the server's private ip
```

Then run the gunicorn server with the configuration file:

```bash
gunicorn --access-logfile access.log \ 
    --error-logfile error.log \ 
    -c mysite/gunicorn.py mysite.wsgi &
```

Server is now running and can be accessed from todos.example.com


## Usage
The simple todo app allows for users to create their own todo lists and manage or monitor their tasks. It is a simple app that can be used by anyone to keep track of their daily activities.

### Features
- User Registration
- User Login
- User Logout
- Create a todo list
- Add a task to a todo list
- Mark a task as done
- Task reset

### Upcoming features
- Edit a task
- Delete a task
- Delete a todo list
- Edit a todo list
- Shared todo lists
- Due dates


## Contributing
Pull requests are welcome for minor changes. For major changes, please open an issue first or contact me directly to discuss what you would like to change.
