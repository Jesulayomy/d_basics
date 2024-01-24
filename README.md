<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body> 
    <h1> Django tutorial </h1>
    <p> This is a tutorial for Django thanks to Mosh, Caleb and Documentation. I covered Django basics, templating, and models</p>
    <h2> Part One </h2>
    <p> This part covered the basics of django, including the projects storefront and movies.</p>
    <ul>
    <li>Setting up</li>
    <p>To install django, first create a virtual environment for your project and activate it</p>
    <code>python3 -m venv .venv && source .venv/bin/activate</code>
    <p>Then install django using pip </p>
    <code>pip install django</code> <br />
    <li>Starting the application</li>
    <p>After installing, you can start the project in the current directory with:</p>
    <code>django-admin startproject mysite . </code>
    <p>Once the project is started, you can create migrations, start an app, add views and urls, create templates and static files, and run the server.</p>
    <code>python manage.py migrate</code> <br />
    <code>python manage.py startapp mysite</code> <br />
    <code>python manage.py runserver</code> <br />
    <p>Also remember to create models and register them to use the admin page, as well as creating a superuser</p>
    <code>python manage.py createsuperuser</code> <br />
    <li>Debugging</li>
    <p>Debugging can be done using the admin panel or error web page, or in vscode using the debugger. Setup the launch.json file and ue a different port in the args section, add breakpoints and start the debugger to monitor the application</p>
    </ul>
    <h2> Part Two </h2>
    <p>This part covered the django-rest-framework, including the project drinks that uses serialization of models to return json responses and recieve json in requests.</p>
    <ul>
    <li>Setting up</li>
    <p>To install django, first create a virtual environment for your project and activate it</p>
    <code>python3 -m venv .venv && source .venv/bin/activate</code>
    <p>Then install django and django-rest-framework using pip </p>
    <code>pip install django django-rest-framework</code> <br />
    <li>Creating the application</li>
    <p>After installing, you can start the project in the current directory with:</p>
    <code>django-admin startproject drinks . </code>
    <p>Once the project is started, start an app and add it to the settings, and make migrations</p>
    <code>python manage.py startapp drinks</code> <br />
    <p>Also create the superuser account, create the model needed and register it in the admin site</p>
    <code>python manage.py createsuperuser</code> <br />
    <code>python manage.py makemigrations</code> <br />
    <p>Create the serializers for the models using an embedded meta class</p>
    <p>Then create the views for the models, using the serializers to return json responses</p>
    <p>Then create the urls for the views, and add them to the project urls using path()</p>
    <p>Then run the server and test the api using the admin site, requests module or postman</p>
    <code>python manage.py runserver</code> <br />
    <p>The admin site can be used for managing the api.</p>
    </ul>
    <h2>Contributors</h2>
    <table>
        <tr>
            <td><img src="https://avatars.githubusercontent.com/u/113533393?s=96&v=4" alt="Jesulayomy" width="80px"></td>
        </tr>
        <tr>
            <td><a href="https://github.com/Jesulayomy">Jesulayomy</a></td>
        </tr>
    </table>    
</body>
</html>
