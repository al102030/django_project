# <span style="color: #ce1403; font-weight: Bold">Django</span>
### <span style="color: #ebce14;">A simple Django project</span>
* A full-featured web application by Django

## <span style="color: #44cecc;">Tutorial's Notes</span>

### <span style="color: #03ce14;">Getting started</span>

* <span style="color: Red;">Installation Instruction</span>
  * Install python
  * install pip
  * install git
  * Add git directory to windows environment variables path
  * ![](NoteImages/1.png)
  * Create repository on GitHub (django_project)
  * Edit README.md file
  * Create ssh key by using 'ssh-keygen' on cmd or terminal
  * Open ssh-key file and copy code
  * Create a new ssh key on GitHub
  * Add Tutor as collaborator on project
  * install Django using pip
  * Check django-admin
  * Start a new project by django-admin-> 'django-admin startproject django-project'
  * change the project name temporary
  * Download project from GitHub-> 'git clone ...'
  * Copy all file from django directory to cloned directory
  * Run server for the first time
  * Open project directory in vscode and run server again (localhost ip address)
  * Adjust .gitignor file
  * Edit git config and create first git commit and push to server
  * Now Everything is OK
* <span style="color: Red;">Django</span>
  * Django is a back-end server side web framework.
  * Other backend frameworks like flask, pyramid, ...
  * Django is free, open source and written in Python.
  * Django makes it easier to build web pages using Python.
  * <span style="color: #00dd99;">Django emphasizes **reusability** of components, also referred to as **DRY** (Don't Repeat Yourself), and comes with **ready-to-use** features like login system, database connection and CRUD operations (Create Read Update Delete).</span>
  * Django is especially helpful for database driven websites
* <span style="color: Red;">How does Django Work?</span>
  * Django follows the <span style="color: Red;">MVT</span> design pattern (Model View Template).
  * ![](NoteImages/2.png)
  * Model - The data you want to present, usually data from a database. <span style="color: Red;">model.py</span>
  * View - A request handler that returns the relevant template and content - based on the request from the user. <span style="color: Red;">view.py</span>
  * Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data. <span style="color: Red;">templates</span>
  * URL - Django also provides a way to navigate around the different pages in a website <span style="color: Red;">urls.py</span>
* <span style="color: Red;">So, What is Going On?</span>
  <ol>
  <li>Django receives the URL, checks the urls.py file, and calls the view that matches the URL.</li>
  <li>The view, located in views.py, checks for relevant models.</li>
  <li>The models are imported from the models.py file.</li>
  <li>The view then sends the data to a specified template in the template folder.</li>
  <li>The template contains HTML and Django tags, and with the data it returns finished HTML content back to the browser.</li></ol>
* <span style="color: Red;">Default Files</span>
  * <span style="color: Red;">manage.py</span> : Our main file that start pur application
  * The inner directory is core of our project
  * <span style="color: Red;">__init__.py</span> : make a python package
  * <span style="color: Red;">settings.py</span> : where are we able to change some project settings
  * <span style="color: Red;">urls.py</span> : where are we set our mapping system
  * <span style="color: Red;">wsgi.py</span> : (django web server)Where are our django project library settings and we never touch it.
  * check admin page to show urls.py functionality
* <span style="color: Red;">Create App</span>
  * An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database.
  * ![](NoteImages/3.png)
  * We create an app using this command : <span style="color: orange;">"python manage.py startapp -app name- "
  * This command create a directory that contain necessary files for our blog
* <span style="color: Red;">Views</span>
  * Django views are Python functions that takes http requests and returns http response, like HTML documents.
  * A web page that uses Django is full of views with different tasks and missions.
  * We should create a view function in view.py file name <span style="color: Red;">'home'</span>
* <span style="color: Red;">Urls.py</span>
  * Create a file named <span style="color: Red;">urls.py</span> in the same folder as the views.py file
  * The urls.py file you just created is specific for the blog application
  * To use that we should copy <span style="color: blue;">path</span> import from project <span style="color: Red;">urls.py</span> file to our app <span style="color: Red;">urls.py</span> file and <span style="color: orange;">urlpatterns</span>
  * After that we should import our project view to urls.py(app) and create a route for our app home page.
  * Then we include our app <span style="color: orange;">urls.py</span> to project <span style="color: orange;">urls.py</span>
  * Django when check a patter and find one match chops our url and send not matches part with request.
  * Run server again and check url patterns separately and check sources
  * Outline : user-url -> project-urls -> blog(app)-urls -> an empty string has been sended -> views.py -> home function -> its return a HttpResponse
  * Do same process for about page
  * Check url by changing in urls.py(pro) and check patterns blog -> blog_app
  * After change <span style="color: orange;">'blog/'</span> our project urls to <span style="color: orange;">''</span> , our Project home page change to blog home page.
* <span style="color: Red;">Templates</span>
  * To return more complex html file we should create templates starting by create templates folder inside our blog app 
  * We can't embed all html code inside **HttpRequest** method
  * Based of the Django Conventions we should create a folder inside templates folder named blog(our app name)
  * After that we should add our template files and name those based on our routes that has existed in views.py file
  * Add some Basic html code inside them
  * Now we need to add our blog application <span style="color: orange;">(in app.py)</span> to the list of our installed app <span style="color: Orange;">(in project settings.py)</span> to Django search for templates directory
  * ![](NoteImages/4.png)
  * New we should define how to our route function load their specific template (also we can load and the return http request)
  * ![](NoteImages/5.png)
  * Do all things for about page as well.
* <span style="color: Red;">Passing data to Templates</span>
  * We can pass data by creating fake data and send the in  dictionary form to template as third argument for render method 
  * Django making template engine is something like Jinja2 that lets us to write python code inside html document