[![Build Status](https://travis-ci.org/deevdz/final-project.svg?branch=master)](https://travis-ci.org/deevdz/final-project)

Full Stack Development Project
======

### Yoga Studio Site with Blog, Shop and Events - Full Stack Development Project for the Code Institute

This submission is part of the Fullstack Software Development diploma course offered by Code Institute.

## Overview

For my [final project](https://deevdz-final-project.herokuapp.com/) for the Code Institute I have taken inspiration from my [First Milestone Project](https://deevdz.github.io/milestone-project-1/index.html "First Milestone Project") and added features that I could only have dreamed of adding at the start of this process.

**What is this website for?** 

This Project is designed to allow users to view information and timetables for a yoga studio, to read articles from the blog and comment on articles, create an account and purchase various products from the site.

**What does it do?** 

The website provides an online presence for a yoga studio and allows users to register on it, log in and log out, to send an enquiry to the studio via the contact form and to purchase the products on offer on both the workshops page and the shop page. 

Users are also able to find out a bit about the studio, classes on offer, workshops available and read and comment on blog posts.

**How does it work?** 

The site's major functionality is to allow users to purchase gift vouchers, class packs and workshops. To be able to add items to their cart users must first register or login to the site. The final stage is to fill in some billing information (user can enter new information or use previously saved information) and enter debit/credit card details via stripe to complete the order. Users will receive an email notification of their order with instructions on how they will receive their product.

A blog section was also created which allows the user to page through multiple posts, comment on individual posts, search posts and filter posts by category or tag. Comments must be approved by the site administrator to appear on the site.

Additionally, the website allows users to submit an enquiry via the contact page. They will then get a reply to the email address they have indicated on the form, with a summary of their enquiry. Prior registration is not required to carry out this action.

## Site Demo
You can see the deployed version of the site [here](https://deevdz-final-project.herokuapp.com/).

## UX

## Features

#### Existing Features
* Responsive design ensures the website displays well on any screen size and device type.
* User authentication and authorisation - handling registration, logging in and logging out. Users who are not logged in will see Register and Log In options in the Navigation bar, but those who are logged in - will see a view orders and Log Out option instead. Administrators will be given extra options to create, update and delete posts.
* Contact form functionality allows users to fill out a form, which after submission will trigger an email to be sent to them using Gmail SMTP (and my own Gmail account). Logged in users will have the email field of the contact form automatically populated.
* Administrators have the option to Create, Update and Delete Blog posts from both the frontend and backend administration part of the site. Registered users are able to submit comments on individual blog posts. When a comment is submitted the site administrator is automatically emailed about the submission and prompted to review for approval. When a comment is approved it appears on the site. Blog posts can be searched and also filtered by category or tag.
* 





#### Future Features
* Filtering the workshops by location or month when the workshop is occuring.
* Adding a shop that also sells physical products hence adding an option for shipping cost and shipping address


## Technologies Used

* [AWS Cloud 9](https://aws.amazon.com/cloud9/) - Was used to code this project.
* [GitHub](https://github.com/) - Remote repository for all project code with git version control.
* Adobe Photoshop & Illustrator - Design, crop and compresses images used on the site.

#### Front-End Technologies

* [HTML5](https://html.spec.whatwg.org/multipage/) - The fundamental code structure for all webpages.
* [CSS3](http://www.css3.info/) - CSS3 is the iteration of the CSS standard used in the styling and formatting of Web pages.
* [jQuery 3.2.1](https://blog.jquery.com/2017/03/20/jquery-3-2-1-now-available/) - Javascript framework used to implement custom code and initialize Bootsrtap functions.
* [Bootstrap](https://getbootstrap.com/) - Bootstrap is an open source toolkit for developing with HTML, CSS, and JS. 
* [Stripe](https://stripe.com/) - The Stripe API allows individuals and businesses to make and receive debit/credit card payments over the Internet.
* [Font Awesome](https://fontawesome.com/) - Used for Website Icons
* [Line Icons](https://lineicons.com/) - Used for Website Icons
* [Google Fonts](https://fontawesome.com/) - Used for website fonts Poppins and Prata
* [Vanilla Top](https://www.npmjs.com/package/vanillatop) - Script to allow users to return to top of page
* [Google Maps API](https://cloud.google.com/maps-platform/) - Used to display location on google maps

#### Back-End Technologies

**Heroku**

* [Heroku](http://ww.heroku.com) - Hosting the deployed version of this project.
* [Heroku Postgres - PostgreSQL](https://devcenter.heroku.com/categories/postgres-basics) is one of the world's most popular relational database management systems.

**Python**

* [Python 3.6.8](https://www.python.org/downloads/release/python-368/) - is an interpreted, high-level, general-purpose programming language that has gained popularity because of its clear syntax and readability and is the language used for all backend functions of this project.
* [Django 1.11](https://docs.djangoproject.com/en/3.0/releases/1.11/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

#### Amazon Web Services

* [Amazon S3](https://aws.amazon.com/free/storage/) - Amazon Simple Storage Service is a service offered by Amazon Web Services that provides object storage through a web service interface. Used to store staticfiles and media folders and files.

Further details on all Python packages used on this project can be found in the requirements.txt file. 

<details>
<summary>CLICK HERE to expand the full requirements.txt details.</summary>
<ul>
<li>boto3==1.10.28 - The AWS SDK for Python</li>
<li>botocore==1.13.28 - Foundation for AWS-CLI command line utilities</li>
<li>Django==1.11 - Used as my Python web framework.</li>
<li>django-tinymce4-lite==1.7.4 - A tinymce editor for text areas in forms</li>
<li>django-forms-bootstrap==3.1.0 -  A form filter for using Django forms with Bootstrap</li>
<li>django-crispy-forms==1.8.0 -  A form filter for using Django forms with Crispy Forms</li>
<li>django-allauth==0.40.0 - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.</li>
<li>dj-database-url==0.5.0 - Utilizes the 12factor inspired DATABASE_URL environment variable to configure Django apps</li>
<li>django-polymorphic==2.1.2 - Use PolymorphicModel to create Products</li>
<li>django-storages==1.8 - Connects Django to S3 Buckets</li>
<li>django-taggit==0.24.0 - Is a reusable Django application for simple tagging.</li>
<li>pytz==2019.2 - Brings the Olson tz database into Python</li>
<li>chardet==3.0.4 - Universal Character Encoding Detector</li>
<li>colorama==0.3.7 - Cross-platform API to print colored terminal text from Python apps</li>
<li>docutils==0.14 - Modular system for processing documentation into useful formats</li>
<li>gunicorn==20.0.4 - A Python WSGI HTTP Server for UNIX</li>
<li>jmespath==0.9.3 - Allows you to declaratively specify how to extract elements from a JSON document</li>
<li>olefile==0.45.1 - Python package to parse, read and write Microsoft OLE2 files</li>
<li>Pillow==5.1.0 - Adds support for opening, manipulating, and saving many different image file formats</li>
<li>python-dateutil==2.6.1 - Extensions to the standard Python datetime module.</li>
<li>psycopg2-binary==2.8.3 - Python-PostgreSQL Database Adapter</li>
<li>requests==2.18.4 - Makes HTTP requests simpler and more human-friendly</li>
<li>six==1.11.0 - A Python 2 and 3 compatibility library</li>
<li>s3transfer==0.2.1 - Python library for managing Amazon S3 transfers</li>
<li>stripe==2.38.0 - Python library for Stripe’s API</li>
<li>urllib3==1.22 - Powerful, sanity-friendly HTTP client for Python</li>
</ul>
</details>


## Testing

Testing for this project has been completed using both automated and manual methods. At the Code Insititute, we are encouraged to code using Test Driven Design methods. Automatic testing has never been my strong point, but testing itself is important. For this project I have created automated tests, carried out extensive manual testing and passed the site code through validators.

### Automated Testing

### Manual Testing

### Validators

#### HTML

Both the Base HTML file and other HTML templates were passed through the [W3C Markup Validator](https://validator.w3.org/). Numerous errors were generated but this was expected as the validator is unable to process the Django templating that builds most aspects of the site. 

For the HTML that does not involve this templating, no errors were found.

#### CSS

The CSS3 code was passed through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and shows that there are no errors. A number of warnings were flagged and related to MS-Grid vendor prefixes.

#### Javascript

All Javascript code was passed through the [Esprima Syntax Validator](https://esprima.org/demo/validate.html) and was found to be syntactically valid.

#### Python

All Python code was passed through the [PEP8 Online validator](http://pep8online.com/) and is PEP8 compliant.


## Deployment



## Credits

**Acknowledgements**

* I would like to thank my tutors and mentor at the Code Institute for all their help and support during the development of this project.
* Tutorials used to aid with the creation of this project - [Just Django](https://www.justdjango.com/learning-material), [Django Tutorials](https://manascode.com/), [Django Girls](https://djangogirls.org/resources/), [Polymorphic Products](https://django-polymorphic.readthedocs.io/en/stable/) and [Django Contact Forms](https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/).
* Code referenced for google map features [Google Map - Custom Style](https://snazzymaps.com/style/134/light-dream), [Google Map - Full width on contact page](https://mdbootstrap.com/docs/jquery/javascript/google-maps/) and [Google Map - Modal Box](https://embed.plnkr.co/plunk/ZDkUYz).

**Content:**

* All content is from the existing Headford Wellbeing Centre website which was written by the owner of the site and myself.

**Images:**

* Images acquired from [BigStockPhoto.com](https://www.bigstockphoto.com/) account, [Pexels](http://pexels.com), [Pixabay](https://pixabay.com/), [Unsplash](https://unsplash.com/) and [StockSnap](https://stocksnap.io/).
* Images from Owner of Headford Wellbeing Centre

**Contact**

Created by [Deirdre van der Zee](mailto:deirdrevanderzee@gmail.com).

