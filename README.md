# Hop Heaven - Milestone Project 4

[View the live project here.](https://hop-heaven.herokuapp.com/)

## Project Overview

Hop Heaven is an e-commerce craft beer website which will allow craft beer enthusiasts to browse world leading craft beers, purchase craft beers and manage there account/leave ratings on beers.

![Hop Heaven](readme_docs/images/hop-heaven.png)

## Project Goals 

* To design and develop and implement a full stack web application, with a relational database, using the Django/Python. This must have at least 2 custom models.
* Design and implement a relational data model, application features and business logic to manage, query and manipulate relational data to meet given needs in a particular real-world domain.
* Identify and apply authorisation, authentication and permission features in a full stack web application solution using django all-auth features.
* Integrate a cloud based payment system such as stripe to the project which could allow real world payments.
* Document the development process using a Git version control and deploy the application using heroku.
* Create a custom clean responsive front end design and implement to provide a distinct brand for the website to attract target users with an intuitive UI/UX.
* CRUD functionality must be included with feedback to user such as toast messages.
* Target Users for this site are craft beer enthusiasts.

## User Stories (UX)

### Viewing and Navigation

* As a User I want to be able to Understand the purpose of the site to see if im interest in the product.
* As a User I want to be able to navigate easily through the site to have ease of use.
* As a User I want to be able to view beers available through the site to make a purchase.
* As a User I want to be able to view beer details through the site to see style, country, brewery, abv, bottle size.
* As a User I want to be able to identify any special offers through the site to purchase the offer.

### Registration & User Accounts

* As a User I want to be able to easily register a user account on the site to view my personal account.
* As a User I want to be able to easily login/logout through the site to make purchases more seamless.
* As a User I want to be able to recover my password to regain access to my account.
* As a User I want to be able to have a personalised user account so I can view my order history & update delivery information.

### Sorting & Searching

* As a User I want to be able to sort the list of available beers to view by price, name, style, country & abv.
* As a User I want to be sort by style of beer to find a specific beer from a certain style of beers.
* As a User I want to be search by beer name or description to focus my search on the beer im after.
* As a User I want to be able easily see what I've searched for and the number of results.

### Purchasing and Checkout

* As a User I want to easily select the quantity to add to my cart before making a purchase.
* As a User I want to view items in my cart to be purchased to identify the total cost.
* As a User I want to be update/delete the quantity of items in my cary to make changes before purchase.
* As a User I want to easily be able to enter payment/delivery information and save my details to make further purchases easier in the future.
* As a User I want to feel like my payment is secure so I'm confident when making a purchase.
* As a User I want to view my order confirmation once purchase has been made to make sure I have not made any mistakes.
* As a User I want to be able to receive an email confirmation on order to be sure I will receive my order & it is being delivered to the correct address.

### Ratings

* As a User how do I rate a product that I have purchased?
* As a User I want to edit a rating I have previously added?
* As a User I want to delete a rating I have a previously added?
* As a user how do I view my ratings I have added to various products?
* As a user how do I get started with rating products?

### Admin & Store Management

* As the site owner I would like to be able to add a new beer so It's avaliable to purchase on the store.
* As the site owner I would like to be able to edit/update a beer to change product details.
* As the site owner I would like to be delete a beer if the item is no longer for sale.


## Design

### 1. Colour Scheme
* #C5B358 - Vegas Gold. Used in footer, header and mobile nav slider, box shadows, buttons and font that needs to stand out. This color has been used to give a premium feel to the products being purchased and allows black text to stand out.
#000000 - Black. Black has been used heavily across the site especially for the background color on bootstrap cards which allows the white text to be easily visible to read and fits the theme of the website.
#777777 - White. For the black backgrounds white has been used so the text is easily visible for the user.

### 2. Typography
* 'Bungee Shade' - Main Hop Heaven Logo. This font style has been used so the brand is distinct.
* 'Bungee' - Header/Navbar links. Fits in with the theme for the main logo and is easily visible to the user.
* 'Oswald' - All remaining content. The text of Oswald has been used for all remaining content in uppercase as its easy on the eye/clear to read. Also fits in with the premium feel to the website.

### 3. Imagery
* Home Page Image - A craft beer being poured grabs the users attention and signals the purpose of the website.
* Accounts signup/signin/register/rating pages - A background of hops fits the theme of the website.
* Hops logo image - A hops image between the logo HOP HEAVEN gives a clear brand image.
* Product/Beer imagery - Photos for each beer which are clear to the user.


### 4. Icons
* Font Awesome Icons used for a clean UX.


## WireFrames

Initial Wireframe designs made on Figma:

* [Initial - Home Page](readme_docs/wireframes/wireframe-home.jpg)
    * Finished design similar to initital wireframe. Hop Heroes & Why shop with us section left out due to time constraints.
* [Initial - Products Page](readme_docs/wireframes/wireframe-products.jpg)
* [Initial - Product Details Page](readme_docs/wireframes/wireframe-product-details.jpg)
    * Finished design similar to initital wireframe. Additional ratings section added to bottom of page for signed in user to rate the product.
* [Initial - Cart Page](readme_docs/wireframes/wireframe-product-details.jpg)
    * Finished Cart page slightly different design in a table style format.
* [Initial - Checkout Page](readme_docs/wireframes/wireframe-checkout.jpg)
    * Fnished page similar to initial design.
* [Initial - Checkout Success Page](readme_docs/wireframes/wireframe-checkout-success.jpg)
    * Fnished page similar to initial design.
* [Initial - Sign In Page](readme_docs/wireframes/wireframe-signin.jpg)
    * Fnished page similar to initial design.
* [Initial - Sign Out Page](readme_docs/wireframes/wireframe-signout.jpg)
    * Fnished page similar to initial design.
* [Initial - Sign Up Page](readme_docs/wireframes/wireframe-signup.jpg)
    * Fnished page similar to initial design.
* [Initial - Verify Page](readme_docs/wireframes/wireframe-verify.jpg)
    * Fnished page similar to initial design.
* [Initial - Profile Page](readme_docs/wireframes/wireframe-profile.jpg)
    * Fnished page similar to initial design. Additional ratings section added under order history
    to edit/delete your ratings.
* [Initial - Admin/management Page](readme_docs/wireframes/wireframe-admin.jpg)
    * Fnished page similar to initial design. 

* Other changes: Ratings Add/Edit pages not included in intitial designs. Feature added during development process. 

* All designs responsive for smaller devices.
    
## Features/Quick Guide

### Site Wide

* Responsive on all devices.
* Toasts when performing certain actions to give the user feedback.
* Search bar functionality within header to search by name/description.
* Navigation dropdown bar to select beers by style/view all in Header.
* Navigation dropdown bar to sort beers by country, abv, price & style all in Header.
* JS Fade animation for dropdown menus on hover.
* My account link in header to view profile, login, logout, signup. Superuser can access beer management.
* Cart link in header to view current shopping cart/checkout.
* Footer Social links.

### index.html 

* Opening statement explaining the purpose of the website to the user with button to start shopping.

### products.html

* Ability to sort by price, name, style, country & abv.
* Navigation buttons at top for each style of beer when viewing each/all styles.
* Back to top button - fixed on medium/large displays and centred at bottom on smaller devices.
* img wapper for beer images with opaque zoom effect.
* Rating for each beer displayed which is dynamic based on average of user ratings.
* Country Flag for each beer displayed.

### product_detail.html

* Breakdown of beer info such as style, country, brewery, abv, bottle/can size, unit price and description.
* Make you selection section to with buttons to add a quantity to your cart.
* JS included to prevent multiple submits when adding to your cart.
* Nav buttons to back to shop or view cart.
* Ratings section at bottom of details page to view current ratings/leave a rating if signed in.
* Ratings within a carousel if ratings within database.
* Ratings carousel contained within product_ratings.html template.

### cart.html

* Breakdown of your current cart in easy to read table style format with the ability to update and remove items from your cart.
* Custom JS to give some feedback to the user when updating/removing items.
* Checkout and back to shop buttons.

### checkout.html

* Breakdown of your current order summary. If a large order - order will be scrollable. Adjust order. button next to order summary if order not quite right.
* Form to fill out with details, delivery and payment information using Stripe Payments.
* Ability to save your delivery information to your profile if you have an account.

### profile.html

* Save your default delivery information.
* View your order history and past order confirmations.
* View your current ratings and edit/delete these ratings. - Ratings within a carousel.
* Ratings carousel contained within profile_ratings.html template.
* If no ratings currently button to link to products page to leave your first rating.

### Ratings Edit/Add/Delete

* Leave your ratings between 1 & 5.
* Can only access these pages if signed in.
* Can only leave one rating per product.
* Can only edit rating if user rating matched session user.
* Form validation throws an error if inputing incorrect value.
* JS included to prevent multiple submits.
* When deleting a rating pop up modal is displayed to confirm whether you want to delete your rating.

### Beer Management (Add/Edit/Delete - Admin)

* Allows the superuser to add/edit/delete beers.
* Pop up modal on deleting product to confirm.

### Root template folder.

* Default All auth templates for django all-auth features.
* Custom Toasts to give feedback to the user with success/error/info & warning alerts.
* Custom 404 & 500 error pages.

### Defensive Design Features

* Use of form & model fields with data type validation across the site. Such as the rating model having max/min value validators so you can only leave a rating between 1 & 5.
* Within the ratings views.py user can only leave one rating per beer otherwise an error will be returned via a toast message.
* Within ratings views.py user has to match current session user otherwise they will not be authorized to edit/delete that rating. 
* On the front end via django templates on the product details page the edit/delete rating buttons will also only be displayed if the user matches the current session user.
* Login Required decorators used on views across multiple apps where the user is required to be signed in to access that feature.
* Ability to add/edit/delete products only if you are a superuser.

    
### Features left to implement

* Detailed about us page on why to to shop with hop heaven.
* Favourites app to star your favourites which will display these on your profile page to make for easier purchasing.
* Monthly subsciption with beer of the month delivered to your door.
* Contact app with form to fill out to contact the site owner.
* Blog app with monthly a blog post detailing interesting craft beer news from the site owner also mentioning any exciting deals/new beers in stock.
* Pagination.

## Database Schema

### Products App

* Category Model
![category_model](readme_docs/images/category_model.png)

* **Custom Products Model**
![products_model](readme_docs/images/products_model.png)
* Size Charfield updated to Integerfield on final deployed version with  Max/Min Value Validators.

### Ratings App

* **Custom Ratings Model**
![ratings_model](readme_docs/images/rating_model.png)

### Checkout App

* Order Model
![order_model](readme_docs/images/order_model.png)

* OrderLineItem Model
![orderlineitem_model](readme_docs/images/orderlineitem_model.png)

### Profiles App

* UserProfile Model
![userprofile_model](readme_docs/images/userprofile_model.png)

### Languages 

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)
* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries, Programs, Tools Used

* [Heroku](https://heroku.com/) - Platform that enables developers to build, run, and operate applications entirely in the cloud.
* [Jquery](https://en.wikipedia.org/wiki/JQuery)
* [Django](https://www.djangoproject.com/) - High-level Python web framework that encourages rapid development and clean, pragmatic design
* [SQlite](https://www.sqlite.org/index.html) - Default database
* [PostgreSQL](https://www.postgresql.org/) - Database used for deployed version.
* [Bootstrap4](https://getbootstrap.com/) - CSS Framework
* [Google Fonts](https://fonts.google.com/) - Google Fonts imported for my project.
* [AWS Amazon S3](https://aws.amazon.com/) - Used to host static/media files.
* [Pillow](https://pypi.org/project/Pillow/2.2.1/) - Python imaging library to aid in processing image files to store in database.
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) - To enable creation, configuration and management of AWS S3.
* [Django Crispy Forms](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) - To style django forms.
* [Gunicorn](https://gunicorn.org/) - WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
* [Font Awesome](https://fontawesome.com/) - Font Awesome was used to add icons for aesthetic and UX purposes.
* [Stripe](https://stripe.com/gb) - Used to make online payments/authentication.
* [Gitpod](https://www.gitpod.io/) - The Interactive Development Envvironment to code the website. Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [Github](https://github.com/) - GitHub is used to store the projects code after being pushed from Git.
* [Figma](https://figma.com/) - This was used to create my wireframe designs for desktop/mobile formats.
* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - To assist with debugging code and assessing performance through lighthouse.
* [AmIResponsive](http://ami.responsivedesign.is/) - Used to created mock up of website.
* [FavIcon](https://favicon.io/) - Used to generate Favicon


## Testing

Testing in [test.md](/test.md) file

## Deployment 

### Running the project locally on the default SQlite database
* To clone my repository type the following into a new workspace. Alternatively you can download a zip file of my repository off my github account.
```
git clone https://github.com/lukehanson2429/hop-heaven.git
```

#### Software Requirements:
To install requirements for the project to run please run the following code in the terminal.
```
pip3 install -r requirements.txt
```
#### Run Migrations:
Run Migrations to install the database structure from the models.
```
python3 manage.py makemigrations --dry-run
python3 manage.py makemigrations 
python3 manage.py migrate --plan 
python3 manage.py migrate 
```

#### Load database from fixtures folder:
Categories & Products stored in json database. Categories must be loaded first as products are dependant on these.
```
python3 manage.py loaddata categories
python3 manage.py loaddata products
```

#### Setup an enviroment for variables
Set up your workspace environment variables for gitpod in workspace settings. My preferred method is using workspace variables and is the method I used for this project. Alternatively can be added into an env.py file and env.py included within gitignore. 

* Format as per the following in env.py for each variable:
```
os.environ.setdefault('SECRET_KEY', '<your_variable_here>')
```
* You will need to import env.py into settings.py also.


* Workspace Variables:
```
KEY = 'SECRET_KEY', VALUE = '<your_variable_here>'
KEY = 'DEVELOPMENT', VALUE = 'True'
KEY = 'STRIPE_PUBLIC_KEY', VALUE = '<your_variable_here>'
KEY = 'STRIPE_SECRET_KEY', VALUE = '<your_variable_here>'
KEY = 'STRIPE_WH_SECRET', VALUE = '<your_variable_here>'
If AWS is setup can add the following variables also to use your AWS S3 Bucket:
KEY = 'AWS_ACCESS_KEY_ID', VALUE: '<your_variable_here>'
KEY = 'AWS_SECRET_ACCESS_KEY', VALUE: '<your_variable_here>'
KEY = 'USE_AWS', VALUE: 'True'
 ```

* In settings.py add:
 ```
 SECRET_KEY = os.environ.get('SECRET_KEY', '')
 ```

#### DEBUG 
```
DEBUG = 'DEVELOPMENT' in os.environ
```

### Heroku Deployment
* Go to the [Heroku](https://www.heroku.com/) website. Register a new account  or login and create a new app.
* Setup a Heroku app within the Heroku dashboard - Type in the app name and select region closest to you.
* In your heroku app settings click on "GitHub" to connect to your repository. Type in the repository name as on GitHub. Click on "Connect".
* Search for your repo (or sign in and connect GitHub account) and select this.
* Then click "Hide Config Vars" in Heroku.
* Go to the resources tab and search for Heroku Postgres to set up database for your deployed version of your site.
* On settings.py temporarily comment out the 'SQLite and Postgres databases' section.
* Add the database URL from Heroku & migrate your models to the PostgreSQL database with: 
    ```
    python3 manage.py migrate
    ```
* Load your data from your fixtures into the POSTGRES database.
    ```
    python3 manage.py loaddata categories
    python3 manage.py loaddata products
    ```
* Create a superuser:
    ```
    python3 manage.py createsuperuser
    ```
* In settings.py delete the PostgreSQL Database section and uncomment the SQLite and PostgreSQL Databases section so you can use either database.
* Install gunicorn and freeze that to the requirements.txt file with the following commands:
    ```
    pip3 install gunicorn
    pip3 freeze --local > requirements.txt
    ```
* Create a Procfile and inside and add the following:
    ```
    web: gunicorn hop_heaven.wsgi:application
* In settings.py use an if statement so that when the app runs on Heroku, you will connect to Postgres otherwise it will connect to sqlite3:
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    ```
* Copy the variables from the variable enviroment one by one into the heroku config vars. They would be:
   ```
    KEY: 'SECRET_KEY', VALUE: “your_variable_here”
    KEY: 'DEVELOPMENT', VALUE: "True"
    KEY: 'STRIPE_PUBLIC_KEY', VALUE: "your_variable_here"
    KEY: 'STRIPE_SECRET_KEY', VALUE: "your_variable_here"
    KEY: 'STRIPE_WH_SECRET_CH', VALUE: "your_variable_here"
    KEY: 'STRIPE_WH_SECRET_SUB', VALUE: "your_variable_here"
    AWS secret keys acquired by setting up S3 Bucket:
    KEY: AWS_ACCESS_KEY_ID, VALUE: "AWS access key ID"
    KEY: AWS_SECRET_ACCESS_KEY, VALUE: "AWS secret access key"
    KEY: USE_AWS, VALUE: "True"
    Also add email variables for live emails to work:
    KEY: EMAIL_HOST_PASS, VALUE: "your_variable_here"
    KEY: EMAIL_HOST_USER, VALUE: "your_variable_here"
    ```
* Login to Heroku in the CLI and temporarity disable collectstatic, with the following command:
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app hop-heaven
    ```
* Add your Heroku app and local host to allowed hosts in settings.py.
* Push to Github, and then to Heroku main. 
* Connect your heroku app to your github repository and enable automatic deployment in your heroku app settings.

### AWS S3 bucket to host static/media files
Create an account with [AWS](www.aws.amazon.com) or login. 
* Create a new S3 bucket and uncheck 'block all public access' and acknowledge that the bucket will be public.
* Update buckets properties and activate static website hosting.
* Set the CORS configuration in the permissions tab:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
* Go to the Bucket policy tab and create a policy with the following settings:
    - Type of Policy: **"S3 Bucket Policy"**
        - Principal: **"*"**
        - Action: **"GetObject"**
        - ARN: This can be found on the Edit Bucket Policy page
        - **Add the statement**
        - **Generate the policy**
* Copy the generated policy into the Policy section on the Edit Bucket Policy page.
        - Add "/*" to the end of the resource key to ensure all files are loaded.
* Allow read public access to all list objects. 
* Create a new user group in IAM services called manage-hop-heaven
* Attach policy to the manage-hop-heaven group.
* Create new user hop-heaven-staticfiles-user and give access and add the user to the group Download the .csv file for your access keys to add to heroku config variables. 

* Install boto3 and Django storages and freeze requirements:
    ```
    pip3 install boto3
    pip3 install django-storages
    pip3 freeze > requirements.txt
    ```
* Add storages to the installed apps in the settings.py file.
* Add the following if statement:
    ```
    if 'USE_AWS' in os.environ:
        # Cache control
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=94608000',
        }
        # Bucket Config
        AWS_STORAGE_BUCKET_NAME = 'hop-heaven'
        AWS_S3_REGION_NAME = 'eu-west-2'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY_ID = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

        # Static and media files
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

        # Override static and media URLS in production
        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```
* Set USE_AWS and set it to True in heroku config variables. 
* Remove the DISABLE_COLLECTSTATIC from the variables so static files will be automatically deployed to heroku. 
* Create custom_storages.py and add:
    ```
    from django.conf import settings
    from storages.backends.s3boto3 import S#Boto3Storage

    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION 
    ```
* Add, commit and push these changes. Static files will now be hosted within your AWS S3 Bucket. 
* Add a new media folder to your bucket and upload your media files.
* Update your stripe webhook end point with your deployed heroku checkout wh url.


## Credits

### Content

* [Website inspired from beerhawk](https://www.beerhawk.co.uk/)
* Beer info/descriptions from ratebeer.com/untappd.com


### Code

* Boutique Ado Mini project a helpful guide to this project.
* W3C schools/stack overflow.


### Media 

* [Logo png from pngwing.com](https://www.pngwing.com/en/free-png-scjji)
* All remaining images for site obtained from usplash.com.

### Acknowledgements

* Tutor support at code institute/Slack community.
* My mentor Brian Macharia with his very helpful feedback while developing this project.
