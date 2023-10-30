# <span style="color: #ce1403; font-weight: Bold">Django</span>

### <span style="color: #ebce14;">A simple Django project</span>

- A full-featured web application by Django

## <span style="color: #44cecc;">Tutorial's Notes</span>

### <span style="color: #03ce14;">Getting started</span>

- <span style="color: Red;">Installation Instruction</span>
  - Install python
  - install pip
  - install git
  - Add git directory to windows environment variables path
  - ![](NoteImages/1.png)
  - Create repository on GitHub (django_project)
  - Edit README.md file
  - Create ssh key by using 'ssh-keygen' on cmd or terminal
  - Open ssh-key file and copy code
  - Create a new ssh key on GitHub
  - Add Tutor as collaborator on project
  - install Django using pip
  - Check django-admin
  - Start a new project by django-admin-> 'django-admin startproject django-project'
  - change the project name temporary
  - Download project from GitHub-> 'git clone ...'
  - Copy all file from django directory to cloned directory
  - Run server for the first time
  - Open project directory in vscode and run server again (localhost ip address)
  - Adjust .gitignor file
  - Edit git config and create first git commit and push to server
  - Now Everything is OK
- <span style="color: Red;">Django</span>
  - Django is a back-end server side web framework.
  - Other backend frameworks like flask, pyramid, ...
  - Django is free, open source and written in Python.
  - Django makes it easier to build web pages using Python.
  - <span style="color: #00dd99;">Django emphasizes **reusability** of components, also referred to as **DRY** (Don't Repeat Yourself), and comes with **ready-to-use** features like login system, database connection and CRUD operations (Create Read Update Delete).</span>
  - Django is especially helpful for database driven websites
- <span style="color: Red;">How does Django Work?</span>
  - Django follows the <span style="color: Red;">MVT</span> design pattern (Model View Template).
  - ![](NoteImages/2.png)
  - Model - The data you want to present, usually data from a database. <span style="color: Red;">model.py</span>
  - View - A request handler that returns the relevant template and content - based on the request from the user. <span style="color: Red;">view.py</span>
  - Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data. <span style="color: Red;">templates</span>
  - URL - Django also provides a way to navigate around the different pages in a website <span style="color: Red;">urls.py</span>
- <span style="color: Red;">So, What is Going On?</span>
  <ol>
  <li>Django receives the URL, checks the urls.py file, and calls the view that matches the URL.</li>
  <li>The view, located in views.py, checks for relevant models.</li>
  <li>The models are imported from the models.py file.</li>
  <li>The view then sends the data to a specified template in the template folder.</li>
  <li>The template contains HTML and Django tags, and with the data it returns finished HTML content back to the browser.</li></ol>
- <span style="color: Red;">Default Files</span>
  - <span style="color: Red;">manage.py</span> : Our main file that start pur application
  - The inner directory is core of our project
  - <span style="color: Red;">**init**.py</span> : make a python package
  - <span style="color: Red;">settings.py</span> : where are we able to change some project settings
  - <span style="color: Red;">urls.py</span> : where are we set our mapping system
  - <span style="color: Red;">wsgi.py</span> : (django web server)Where are our django project library settings and we never touch it.
  - check admin page to show urls.py functionality
- <span style="color: Red;">Create App</span>
  - An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database.
  - ![](NoteImages/3.png)
  - We create an app using this command : <span style="color: orange;">"python manage.py startapp -app name- "
  - This command create a directory that contain necessary files for our blog
- <span style="color: Red;">Views</span>
  - Django views are Python functions that takes http requests and returns http response, like HTML documents.
  - A web page that uses Django is full of views with different tasks and missions.
  - We should create a view function in view.py file name <span style="color: Red;">'home'</span>
- <span style="color: Red;">Urls.py</span>
  - Create a file named <span style="color: Red;">urls.py</span> in the same folder as the views.py file
  - The urls.py file you just created is specific for the blog application
  - To use that we should copy <span style="color: blue;">path</span> import from project <span style="color: Red;">urls.py</span> file to our app <span style="color: Red;">urls.py</span> file and <span style="color: orange;">urlpatterns</span>
  - After that we should import our project view to urls.py(app) and create a route for our app home page.
  - Then we include our app <span style="color: orange;">urls.py</span> to project <span style="color: orange;">urls.py</span>
  - Django when check a patter and find one match and chops our url and send not matches part with request.
  - Run server again and check url patterns separately and check sources
  - Outline : user-url -> project-urls -> blog(app)-urls -> an empty string has been sended -> views.py -> home function -> its return a HttpResponse
  - Do same process for about page
  - Check url by changing in urls.py(pro) and check patterns blog -> blog_app
  - After change <span style="color: orange;">'blog/'</span> our project urls to <span style="color: orange;">' '</span> , our Project home page change to blog home page.
- <span style="color: Red;">Templates</span>
  - To return more complex html file we should create templates starting by create templates folder inside our blog app
  - We can't embed all html code inside **HttpRequest** method
  - Based of the Django Conventions we should create a folder inside templates folder named blog(our app name)
  - After that we should add our template files and name those based on our routes that has existed in views.py file
  - Add some Basic html code inside them
  - Now we need to add our blog application <span style="color: orange;">(in app.py)</span> to the list of our installed app <span style="color: Orange;">(in project settings.py)</span> to Django search for templates directory
  - ![](NoteImages/4.png)
  - After register our app by adding it in the project, Django search for templates, models, or anything related to our blog app inside blog directory
  - New we should define how to our route function load their specific template (also we can load and the return http request)
  - ![](NoteImages/5.png)
  - Do all things for about page as well.
- <span style="color: Red;">Passing data to Templates</span>
  - We can pass data by creating fake data and send the in dictionary form to template as third argument for render method
  - Django making template engine is something like Jinja2 that lets us to write python code inside html document
  - For writing a code block inside html doc we should use this pattern : <span style="color: Orange;">{% Our python code %}</span>
  - For accessing a variable inside html doc we should use this pattern : <span style="color: Orange;">{{ Our python variable }}</span>
  - In vscode by converting language mode to Django template helps us to write Django code easily
  - we can embed a python code (if statement) to manage our home page <span style="color: Red;">title</span>
- <span style="color: Red;">Template Inheritance</span>
  - To escape of writing duplicated code for all templates we can use template inheritance to make it easy to change common elements of all templates
  - We can do it by defining a <span style="color: Green;">base.html</span> file and make it a parent class for all other templates
  - We can import a <span style="color: Green;">block content</span> to our base.html to make a section that our child template can overwrite
  - Then we need to remove all information that is in our base.html from other templates
  - After that we need to extend the base.html codes to other templates by adding <span style="color: Red;">extend block</span> to them and a <span style="color: Red;">content block</span>
- <span style="color: Red;">Bootstrap</span>
  - We use Bootstrap to add some nice style to our website
  - Bootstrap is <span style="color: Pink;">Frontend framework</span> and we need to pass a crash course trough the internet to work with
  - By adding Bootstrap <span style="color: Red;">meta links</span> and <span style="color: Red;">javascript links</span>, we can use this libraries through the <span style="color: Red;">Content Delivery Network (CDN)</span> ability.
  - Template inheritance helps us to use bootstrap in all pages in our website
  - We need to copy Bootstrap <span style="color: Yellow;">starter meta codes</span> inside the head section of base.html file and bootstrap <span style="color: Yellow;">starter javascript code</span> at the end of this file before closing body tag
  - After that we need to warp our content block inside a <span style="color: Red;">div</span> that uses <span style="color: Yellow;">container</span> class
  - Check page source to show HTML code
  - Then we need to add some HTML code to our base.html file to make it stylish <span style="color: Red;">(header and main section)</span>
  - Then we need some custom style base on our bootstrap specific
  - We should create <span style="color: Red;">main.css</span> file inside <span style="color: Yellow;">Static /blog</span> directory in our <span style="color: Red;">app</span>
  - After copy all css codes inside main.css we need to include that into our base template by referencing it and <span style="color: Red;">load static code block</span >
  - And after that we need to create link to our static file inside head tag
  - After that we should put our article code to a specific blog so we put it in for loop of blog post in home template
  - At the end for separating our blog home of other apps home we should define url pattern in href of navigation bar to avoid hard coding(and explain name tag in url pattern)
- <span style="color: Red;">Admin Page</span>
  - Before migration creating a super user and entering to admin page is impossible
  - Explain the red error that shows after running server
  - First we should use <span style="color: Red;">makemigrations</span> command following <span style="color: Yellow;">'python manage.py'</span>
  - Second we should use migra
