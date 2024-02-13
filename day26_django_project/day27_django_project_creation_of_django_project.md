## Project Overview: News Aggregator Website
In this project, we'll create a News Aggregator Website with four key objectives:

- **Collect XML Feeds:** We'll start by fetching news articles from various XML-based RSS feeds
  - https://www.wired.com/feed/rss
  - https://www.theguardian.com/world/rss
- **Store XML Feeds:** Next, we'll store these articles in a database.
- **Remove Duplicates:** We'll implement logic to identify and remove duplicate articles.
- **Render on UI:** Finally, we'll display the articles in web interface, sorted by publication time. 

## Creating the first django project
**Step 1: Install Django**
  - First, you need to install Django. 
  - It's recommended to use a virtual environment for Python projects, including Django projects, to manage dependencies separately for each project. 
  -  Create a virtual environment:
    - `python -m venv myvenv`
  - Activate the virtual environment:
    - On Windows: `myvenv\Scripts\activate`
    - On macOS and Linux: `source myvenv/bin/activate`
  - Install Django within the virtual environment: `pip install django`

**Step 2: Create Your Django Project**
- After installing Django, you can create a new project by running:
```bash
django-admin startproject myproject
```

**Step 3: Run Your Django Project**
- Navigate into your project directory and run the development server:
```bash
cd myproject
python manage.py runserver
```
You should see output indicating the development server is running, and 
it will tell you the address to access it, usually http://127.0.0.1:8000/.

**Step 4: Access Your Project**
- Open a web browser and go to http://127.0.0.1:8000/. 
- You should see the Django welcome screen, which means your project is successfully running.
![img.png](images%2Fimg.png)
- Now press `"Ctrl+C"` to terminate the server.

## Distinction between a Django "project" and a Django "app."

### Django Project: 
- This is the entire application and its configuration. 
- When you run `django-admin startproject myproject`, it creates the project structure. 
- This includes:
  - settings for the project (`settings.py`), 
  - URL configurations (`urls.py`), and 
  - other configuration files. 

### Django Project Structure
- In your Django project directory (myproject), you'll find several files created by Django. 
- Here's what they are and their purpose:
- `__init__.py:` 
  - This empty file tells Python that the directory should be considered a Python package. 
  - It's standard in Python packages but doesn't contain any project-specific settings.
- `settings.py:` 
  - This is one of the **most crucial files**. 
  - It contains all the configuration for your Django project. It defines the following: 
    - Database configurations, 
    - installed apps, 
    - middleware, 
    - templates, and more . 
  - When you add new apps to your project, you'll often need to add them to the INSTALLED_APPS setting in this file.
- `urls.py:` 
  - This file is responsible for URL declarations for your project; 
  - it's a **"table of contents"** for your Django-powered site. 
  - It tells Django which views are to be handled by which URLs. 
  - When you create new views in your apps, you'll often link them here or in an app-specific urls.py that you include in this main one.
- wsgi.py: 
  - Stands for Web Server Gateway Interface. 
  - It's a specification for a simple and universal interface between web servers and web applications or frameworks for Python. 
  - This file helps your Django project communicate with the web server, which can be useful when deploying your project.
- asgi.py: 
  - Stands for Asynchronous Server Gateway Interface. 
  - It's a standard for how web servers communicate with asynchronous Python web applications. 
  - It's used for deploying your project in conjunction with ASGI servers, especially useful for applications that require long-lived connections like WebSockets.

### Django App: 
- An app is a web application that does something – e.g., a blog, a database of public records, or a simple poll application. 
- Each app has its own models.py, views.py, urls.py, etc. 
- You create an app within a project to handle a specific piece of functionality. 
- A project can contain multiple apps.
- Lets create a Django "app"
```bash
python manage.py startapp aggregator
```
- This command creates a new directory within your project named aggregator (or whatever you named your app), and this directory will contain the views.py file among others (models.py, tests.py, admin.py, etc.).
- Your project structure should now look something like this:

```markdown
myproject/
    manage.py
    myproject/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    aggregator/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
```
- In views.py within your app (aggregator/views.py), you can start defining views for your application. 
- For example, a simple view could look like this:
```python
# aggregator/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```

- To hook this view up to your project, you'd include it in your URL configurations. 
- You'd first add a path to your app in the project's urls.py file:

```python
# myproject/urls.py
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aggregator.urls')),  # Include your app's urls.py
]
```
- And then create a `urls.py` in your app directory (aggregator/urls.py) if it doesn't already exist, defining a URL pattern for the view:
```python
# aggregator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```
- This setup tells Django to serve the home view you defined in `views.py` when you navigate to the root URL of your project.
- Open a web browser and go to http://127.0.0.1:8000/
![img_1.png](images%2Fimg_1.png)

### Django App Structure (Aggregator)
- Within your newly created Django app, "aggregator", you'll find a set of files as well. 
- Each has a specific role:
- **views.py:** 
  - **This is the heart of the application's logic.**
  - Views handle the HTTP requests and return HTTP responses. 
  - This file defines functions or classes corresponding to different URLs specified in `urls.py`.
- `__init__.py`: 
  - This file is a Python convention that marks the directory as a Python package. 
  - It is usually empty but can be used to include package-level variables or initialization code.
- **admin.py:** 
  - This file is used to register your models with the Django admin interface, 
  - making it easier to perform create, read, update, and delete operations on your models directly from a web interface provided by Django.
- **apps.py:** 
  - Contains the configuration for your app. 
  - Here, you can include any app-specific settings.
- **models.py:** 
  - This file defines the structure of your application's data. 
  - Django uses these class definitions to create database tables using an ORM (Object-Relational Mapping) system.
  - These classes will become the database tables in your app.  
- **tests.py:** 
  - For your app's tests. Django has a built-in framework for writing and running tests.
  - You can define test classes here to test the functionality of your models, views, forms, and other parts of your app.
- **migrations/ directory:** 
  - This directory contains migrations files for your app - they are changes you make to your models.py over time (like creating a new model, or adding a field to an existing model). 
  - Django generates Python files in this directory to keep track of your database schema changes.

## What is MVC in Web Frameworks?
![img_1.png](images/mvc_1.png)
![img_2.png](images/mvc_2.png)
- MVC stands for **Model-View-Controller**. 
- It is a software design pattern commonly used for developing user interfaces that divides the related program logic into three interconnected elements. 
- This is done to separate internal representations of information from the ways information is presented to and accepted from the user.
- **Model:** 
  - The central component of the pattern. 
  - It is the application's dynamic data structure, independent of the user interface. 
  - It directly manages the data, logic, and rules of the application.
- **View:** 
  - Any representation of information such as a chart, diagram, or table. 
  - Multiple views of the same information are possible.

- **Controller:** 
  - Accepts input and converts it to commands for the model or view.

## MVC Implementation in Django
![img.png](images/mvt_1.png)
![img_4.png](images/mvt_2.png)

- Django follows a slightly modified MVC pattern, often referred to as the **MVT (Model-View-Template)** pattern.
- **Model (M):** 
  - In Django, the `models.py` file represents the Model component. 
  - It is responsible for managing data and business logic.
- **View (V):** 
  - The View component is handled by what Django calls views, defined in `views.py`. 
  - Views process user requests, interact with the model, and return the appropriate response to the user.
- **Template (T):** 
  - Django's Template is the equivalent of the Controller in MVC, but it's also a mix of View's responsibilities. 
  - Templates are HTML files that handle the presentation layer and are populated with data from the views.
- **Controller:** 
  - Django itself acts as the Controller, managing the interactions between the Model and the View/Template. 
  - It takes care of the backend processes, URL routing, and serving responses.

- Each component in the Django framework is interconnected, with `urls.py` directing HTTP requests to the appropriate view, the view interacting with the model as needed, and any response typically rendered using a template, which is then served to the client.

### Let's add a new endpoint to gather_feeds
```python
# aggregator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('gather_feed/', views.gather_feed),
]
```

```python
import feedparser
from django.http import HttpResponse, JsonResponse
import pprint
def home(request):
    return HttpResponse("Hello, Django!")

def gather_feed(request):
    # Example RSS feed
    feed_url = 'https://www.wired.com/feed/rss'
    feed = feedparser.parse(feed_url)

    # Build a simple HTML string to display the titles
    content = '<h1>Latest Wired Articles</h1>'
    for entry in feed['entries']:
        pprint.pprint(entry)
        print("")
        content += f"<p>{entry.title}</p>"
        break
    return HttpResponse(content)
```

### What is RSS feed?
This is how an item looks like from https://www.wired.com/feed/rss
```xml
<item>
<title>A Backroom Deal Looms Over Section 702 Surveillance Fight</title>
<link>https://www.wired.com/story/section-702-reform-backroom-deal/</link>
<guid isPermaLink="false">65ca42ffce0a0eda3d6718a8</guid>
<pubDate>Mon, 12 Feb 2024 19:15:40 +0000</pubDate>
<media:content/>
<description>Top congressional lawmakers are meeting in private to discuss the future of a widely unpopular surveillance program, worrying members devoted to reforming Section 702.</description>
<category>Security</category>
<category>Security / Privacy</category>
<category>Security / Security News</category>
<category>Politics / Policy</category>
<media:keywords>surveillance, privacy, FBI, NSA, congress</media:keywords>
<dc:creator>Dell Cameron</dc:creator>
<dc:publisher>Condé Nast</dc:publisher>
<dc:subject>Cloakroom & Dagger </dc:subject>
<media:thumbnail url="https://media.wired.com/photos/65ca464cb9f47e3f10ce2b7e/master/pass/Backroom-Deal-Eyed-Suspiciously-in-US-Surveillance-Fight-Security-GettyImages-1988344159.jpg" width="2400" height="1600"/>
</item>
```
- RSS, which stands for **Really Simple Syndication** or **Rich Site Summary**, is a type of web feed that allows users and applications to access updates to online content in a standardized, computer-readable format. 
- These feeds can, for example, allow a user to keep track of many different websites in a single news aggregator.

- The format of the item shown from Wired's RSS feed is indeed a standard format. 
- Here's a breakdown of the common elements in an RSS feed item:

`<title>`: The title of the content (in this case, an article).

`<link>`: The URL to the full content.

`<guid>`: A unique identifier for the item. The isPermaLink attribute indicates whether the GUID is a permanent URL or not.

`<pubDate>`: The publication date and time of the content.

`<media:content>`: This element is often used to include media like images, videos, etc., within the feed.

`<description>`: A brief summary or description of the content.

`<category>`: A tag or category associated with the content. An item can have multiple category elements.

`<media:keywords>`: Keywords associated with the item, similar to tags.

`<dc:creator>`: The author of the content.

`<dc:publisher>`: The publisher of the content.

`<dc:subject>`: The subject or theme of the content.

`<media:thumbnail>`: A URL to a thumbnail image representing the content, along with its dimensions.

