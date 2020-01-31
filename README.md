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

Documentation for the initial planning process can be [found here](https://github.com/deevdz/final-project/blob/master/planning/Yoga%20Studio%20Website%20-%20Initial%20Thoughts.pdf)

#### User Stories

* As a user - I am immediately aware what the nature of the site is and its purpose
* As a user - I can navigate through the site by various means i.e. Feature Slider, Navigation dropdown, homepage links
* As a user - I can browse the site without being a logged in user
* As a user - I can create a user profile, and log in and out
* As a user - I can view information about the studio, on classes and timetables
* As a user - I can view workshops being run and details of these workshops
* As a user - I can book and pay for a place on a workshop
* As a user - I can purchase gift vouchers and class packs
* As a user - I can receive an email confirming my order
* As a user - I receive an error message if I am unable to login or register
* As a user - I receive an error message if there is an issue purchasing a product
* As a user - I am able to access the site on mobile or tablet and have a similar experience as a desktop device
* As a user - I can read blog posts and comment on the post if I am a logged in user
* As a user - I can filter blog posts by category or post tag
* As a user - I can see the number of approved comments associated with a blog post
* As a user - I can see how many times a blog post has been viewed
* As a user - I can view previous orders I have made.
* As a user - I am able to page through blog posts if there are more than 4 posts
* As a user - I am able to contact the site administrator through a contact form and may or may not be a logged in user
* As an administrator - I can add, update and delete blog posts
* As an administrator - I can approve comments to display on the site
* As an administrator - I can receive an email about successful site orders
* As an administrator - I can receive an email when a new comment has been submitted to the site

#### Typography

Research was carried out on complimentary fonts and [Poppins](https://fonts.google.com/specimen/Poppins) and [Prata](https://fonts.google.com/specimen/Prata) were chosen for the site.

#### Colour Scheme and Logo

The studio is an established business so I am using the existing logo which I designed many years ago. I also have taken the existing colour scheme but extended it with the help of the [Coolors](https://coolors.co/392f23-7ab5a7-99b8d1-cecccc-9d6381) colour generator.

#### Wireframes

The wireframes for this site were generated using Adobe Illustrator. Wireframes for the site can be found in the folder [planning > wireframes](https://github.com/deevdz/final-project/tree/master/planning/wireframes).

## Features

#### Existing Features
* Responsive design ensures the website displays well on any screen size and device type.
* __Homepage slider__ was created which allows the site administrator to add slides through the administration section of the site. This feature allows the administrator to add a title and subtitle, slider image, text that will be displayed on the button, the link for the button and the alignment of the text. The administrator also has the option to leave the slide as a draft or publish to the site.
* __User authentication and authorisation__ - handling registration, logging in and logging out. Users who are not logged in will see Register and Log In options in the Navigation bar, but those who are logged in - will see a view orders and Log Out option instead. Administrators will be given extra options to create, update and delete posts. User Authentication was carried out using the [AllAuth app](https://django-allauth.readthedocs.io/en/latest/installation.html).
* __Contact form__ functionality allows users to fill out a form, which after submission will trigger an email to be sent to them using Gmail SMTP (and my own Gmail account). Logged in users will have the email field of the contact form automatically populated.
* __Blog__ Administrators have the option to Create, Update and Delete Blog posts from both the frontend and backend administration part of the site. Registered users are able to submit comments on individual blog posts. When a comment is submitted the site administrator is automatically emailed about the submission and prompted to review for approval. When a comment is approved it appears on the site. Blog posts can be searched and also filtered by category or tag. Pagination is in place and 4 posts are displayed per page. Tags are generated using the [django-taggit app](https://django-taggit.readthedocs.io/en/latest/)
* __Product Pages__ - both a shop page and a workshop page was established on the site. Products were created using polymorphism. This allows the products to share common features but also allow products, in this case the workshops/events to have different product fields than other products. Workshops/Events have date and time fields, location of the event and the number of available places at this event.
* __Cart and Checkout functionality__ - the Cart app stores the information of each product that is added to it and displays a cart total. Users can increase, decrease and remove items from the cart. In relation to workshops there is a check in place to see if there are enough places available on the workshop. The Checkout app also stores this information and displays a total but additionally sends the user to a Stripe form to enter payment details. On successfully completing their order users can view their order and any preious orders. 
* __Error Pages__ The site features custom error pages for both 404 and 500 errors.


#### Future Features
* __Workshops/Events__ Filtering the workshops by location or month when the workshop is occuring.
* __Products and Checkout__ Adding a shop that also sells physical products hence adding an option for shipping cost and shipping address
* __Administration Dashboard__ Show a graphical representation of product sales.
* __Social Login__ Offer users the option to signup and login to the site via social media accounts.

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

#### Installed Apps

* [django-taggit](https://django-taggit.readthedocs.io/en/latest/) - is a reusable Django application designed to make adding tagging to your project easy and fun.
* [AllAuth](https://django-allauth.readthedocs.io/en/latest/overview.html) - Supports multiple authentication schemes (e.g. login by user name, or by e-mail), as well as multiple strategies for account verification (ranging from none to e-mail verification).

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
</summary>
</details>


## Testing

Testing for this project has been completed using both automated and manual methods. At the Code Insititute, we are encouraged to code using Test Driven Design methods. Automated testing has never been my strong point, but testing itself is important. For this project I have created automated tests, carried out extensive manual testing and passed the site code through validators.

### Automated Testing

Each app has their own tests created using Django TestCase class. All views, forms and pages were tested as much as possible using unit tests. In all, 24 tests were written. All tests pass successfully.

Travis-CI integration has been completed and also shows all tests completing successfully, with the project showing as "build: passing".

### Manual Testing

In conjunction with the automated testing the website was constantly tested during the development process. Browser developer tools were used to test HTML, CSS, JavaScript and responses from the server. Extensive manual testing has been completed to check that the site performs as it should in different environments and in different browsers.

<details>
<summary>Click to see details of manual testing below.</summary>
<h5>Homepage</h5>
<ul>
<li>Click on logo or Home and verify that home page appears.</li>
<li>Click on navigation links and confirm they are going to the correct pages</li>
<li>If user is not logged in “Login/Register” is displayed in the navigation (dropdown from user icon) and clicking this link will bring you to the login page.</li>
<li>If user is logged in, the user will see the following options in the user dropdown - Username, My Orders and Logout option. If user who is logged in is a site administrator they will see an extra option to create a blog post.</li>
<li>Ensure slider displaying slides that are published and the correct information as entered by the administrator.</li>
<li>Click on links in three boxes and ensure they are going to the correct pages.</li>
<li>That three blog posts display with the correct information. Ensure that only published blog posts display and are ordered with the most recent posts displaying first.</li>
<li>Ensure that a workshop is displaying in the event section with the correct information and links. Confirmed that only future events display (past events are ignored) and that the event that is displayed is randomised.</li>
<li>Confirmed that the social links in the footer open in a new browser window and go to the correct links. Check that the Find Us link in the footer opens a map in a lightbox to the correct location.</li>
<li>Confirmed that the email signup links to a mailchimp account.</li>
</ul>
<h5>About Page</h5>
<ul>
<li>Confirmed that the images in the masonary gallery were opening to a lighbox. This lighbox can be paged through using arrows and exited using the x symbol.</li>
</ul>
<h5>Static Pages including classes and timetables</h5>
<ul>
<li>Confirmed that page links are working and pages are responsive.</li>
</ul>
<h5>Workshops Page</h5>
<ul>
<li>Confirmed that the correct workshops are displaying on the page with the correct details. Checked that only workshop products are displaying on this page. Only future workshops display on this page. If a workshop is in the past it no longer displays.</li>
<li>Checked that the workshop summaries are linking to the correct workshop details page</li>
<li>Verified that the correct number of remaining places available on workshops are displayed. Display changes depending on if there are places remaining or if the workshop s sold out</li>
</ul>
<h5>Workshop Details Page</h5>
<ul>
<li>Confirmed that the correct information and image is displaying on the page </li>
<li>Checked that the "Add to Cart" button only displays if there are places remaining on the workshop.</li>
<li>Confirmed that clicking the add to cart button adds one workshop to the cart. </li>
<li>Add to Cart button is replaced with a Sold Out button if no places are remaining and confirmed that the user cannot add a sold out event to the cart</li>
</ul>
<h5>Blog Page</h5>
<ul>
<li>Confirmed that the correct information and images are displaying on the page. That 4 blog posts display per page when 4 or more blog posts are available. That only published blog posts display. That posts are ordered by most recent post first.  </li>
<li>Clicked through to blog posts and confirmed that links are correct</li>
<li>Used the search function to search posts and confirmed that results were correct</li>
<li>Confirmed that category counts were correct and that clicking on categories displays posts filtered by category</li>
<li>Checked that pagination links were working correctly.</li>
</ul>
<h5>Blog Post Page</h5>
<ul>
<li>Confirmed that the correct details and images were displaying for each individual blog post</li>
<li>Checked that the blog post views increased for each view and that the correct number of comments were displayed</li>
<li>Clicked on category and tag links and confirmed they redirected to the correct pages</li>
<li>Verified that the search section in the sidebar is working as expected</li>
<li>If user is logged in as an administrator they are given extra buttons on blog posts to allow them to update the post and delete the post</li>
<li>Confirmed that changes made in the update post form occurred</li>
<li>Confirmed that clicking the delete post button removes the post</li>
<li>Checked that the next post and previous post links go to the correct posts</li>
<li>Checked that comments were displaying as expected. Only logged in users can add a comment to the blog. When a comment is added a message is displayed to the user informing them that the comment has been put forward for approval. An email is sent to the site administrator prompting them to review the comment. Only when the comment is set to approved will it appear on the site.</li>
</ul>
<h5>Contact Page</h5>
<ul>
<li>Confirmed that the correct map location is displaying</li>
<li>Contact Form - if user not logged in they are required to enter Name, Email and Message. Confirmed that the email was sent and received. If user logged in the email address field is prepopulated. Sent a test email and confirmed that is worked as expected.</li>
</ul>
<h5>Shop Page</h5>
<ul>
<li>Check that the correct products are displaying under the correct headings - Gift Vouchers or classes. Make sure that if there are no products available to purchase under one of these headings that a suitable error message is displayed.</li>
<li>Check that the add to cart button works as expected ie the correct information and price is added to the cart and that only logged in users can view the cart.</li>
</ul>
<h5>Account Pages</h5>
<ul>
<li>I have used the AllAuth App for my account management. I have confirmed that the sign up, login, logout, forgotten password, verifying account are all working as expected.</li>
</ul>
<h5>Cart Page</h5>
<ul>
<li>Confirmed that a user can only view the cart if they are a registered logged in user.</li>
<li>Checked that product quantaties can be increased and decreased. Also confirmed that workshop products can only be increased where the places are available. Confirmed that products can to removed from the cart.</li>
<li>Verified that the correct products displayed in the cart when the add to cart button is clicked. Confirmed that the totals for products were correct</li>
<li>Confirmed that the correct messages are displaying regarding adding, removing from the cart, or if the cart is empty</i>
<li>Checked that the buttons to proceed to checkout and return to shop go to the correct pages</li>
</ul>
<h5>Checkout Page</h5>
<ul>
<li>Confirmed that the correct details have come through from the Cart Page.</li>
<li>If user has a pre-existing address this is displayed and can be used for the order or the user can update the address and proceed with the updated version.</li>
<li>If the user is newly registered they are prompted to add a billing address which is saved to the users account.</li>
<li>Confirmed that the Proceed to payment brings you to the next page where you are prompted to enter your card details via a stripe popup</li>
<li>On the pay with Stripe page confirmed that clicking the pay with card button opens a lightbox to enter payment details via stripe. Confirmed that the correct amount is being charged.</li>
<li>Confirmed that a successful order empties the shopping cart, sends a confirmation email with order details to both user and site administrator, that in the case of workshops that the places available are decreased by the correct amount</li>
<li>Users are given the option to view all their orders and this lists all the users orders with the quantity and product ordered displayed</li>
</ul>
<h5>Error Pages</h5>
<ul>
<li>Try going to <a href="https://deevdz-final-project.herokuapp.com/test" target="_blank">https://deevdz-final-project.herokuapp.com/test</a> and observe the custom 404 error.</li>
<li>Confirmed that there was a working link back to the homepage and that links in the navigation are working on the 404 error page.</li>
</ul>
<h5>Issues and Fixes</h5>
<ul>
<li>Issue - had the search function working on the blog posts and then introduced the category count in the sidebar and found that the search was no longer working. Fix - Discovered that the order of the urls in the urls.py file is important. Once I updated the order of the urls my search worked again.</li>
<li>Issue - Polymorphic Products, I wanted to include an available number of places on workshop products. This caused issues when I wanted to decrease places on purchase for the other product types. Fix - introduced a product type dropdown and then checked the product type. If the product type is workshop then decrease the places available by the correct amount. If the product type is not workshop then ignore the places available decrease and move on with the order.</li>
<li>Issue - Removing items from the cart - I found that if I had more than one of a product type in the cart I had issues removing it from the cart. Fix - the remove from cart trashcan icon is only displayed when there is one of a product in the cart.</li>
<li>Issue - Comment counts. I wanted each post to display the number of comments that were associated with a blog post but my count was incorrect as it was counting all comments (including comments from other posts). Fix - Set up a get_comments property in the blog model that returned a count of only the comments associated with the post. I also introduced the approval system for comments as prior to this all comments were automatically displayed which could lead to inappropriate comments and/or spam.</li>
<li>Issue - Shop display on mobiles. I found that the products in the shop weren't displaying as I hoped on mobile devices. Fix - I used Javascript to atler classes based on the screen size.
</ul>
</summary>
</details>


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

Having choosen Cloud9 as my IDE, the following steps were carried out:

* Install Python3 and Django to run the application.
* Create project - yogastudio
* Cloud9 included in the list of ALLOWED_HOSTS in staging settings, later heroku url will be added to ALLOWED_HOSTS
* Add run command to bashrc file 
* Create git repository - Initialise the repository, add files not required to the gitignore file. Carry out a `git add` and `git commit - "Initial Commit" `.
* Set up templates and static folders
* Create a env.py file containing the following environmental variables (add env.py file to the gitignore list):
 ```
STRIPE_PUBLISHABLE - Used solely to identify your account with Stripe; it isn't secret.
STRIPE_SECRET - Can perform any API request to Stripe without restriction.
DATABASE_URL - Remote PostgreSQL database link if using a remote database.
SECRET_KEY - Standard secret key, any value.
EMAIL_ADDRESS - to send correspondence from the site.
EMAIL_PASSWORD - authenticate email account.
AWS_ACCESS_KEY_ID - AWS user credentials.
AWS_SECRET_ACCESS_KEY - AWS S3 credentials.
```
* Generate a requirements.txt file so Heroku can install the required dependencies to run the app. `sudo pip3 freeze --local > requirements.txt`. The contents of the requirements.txt is referenced above.
* Python package gunicorn was installed
* Create a Procfile to tell Heroku what type of application is being deployed, and how to run it. `web: gunicorn yogastudio.wsgi:application`
* Create a new app on Heroku to host and run the site
* In Heroku go to resources and add a Postgres Database
* Retrieve the Postgres DB url and add to the env.py on cloud9
* In the settings.py file update the DB details to look at the DB hosted on Heroku
* This is followed by migrations `python3 manage.py makemigrations` and `python3 manage.py migrate` to  create tables on heroku database.
* Create a super user on the new DB `python3 manage.py createsuperuser`
* In Heroku, connect newly created app to the correct github repository.
* Set up config vars that are currently stored in our env.py file on Heroku.
* Create a bucket on Amazon S3, set up the appropriate permissions, groups, users and policies.
* In Cloud9 install the following: django-storages and boto3. `sudo pip3 install django-storages`, `sudo pip3 install boto3`, 
* Create a custom_storages.py file and add static file settings and media storage information to the setting.py file.
* Run `python3 manage.py collectstatic`
* Add DISABLE_COLLECTSTATIC with the value of 1 to the Config Variables on Heroku
* Enable automatic deploys from github to heroku.
* On completion of the project debug mode was set to False in the settings.py file.
 


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

