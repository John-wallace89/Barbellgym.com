<h1 style="text-align: center">The Barbellgym.com </h1>

![hero image screenshot](media/barbellgym_responsive_ms4.JPG)

This is my submission for Milestone project 4 for Code Institute. The Barbellgym.com is a site for existing and new members of the Barbell Gym to
get information, purchase merchandise and send enquiries on classes and personal training. The goal for this site is to be used to generate income
for the owner of the Barbell Gym and a 'one stop shop' for all new an existing members. 

Live project: [https://thebarbellgym.herokuapp.com/]

### User Experience (UX) ###

* User Story 1 - As a customer, I land on the hompeage of the site and It's clear what the business is.
* User Story 2 - As a customer I can navigate easily to any section of the site regardless of where I am or what device I am using.s
* User Story 3 - As a customer I can easily access the Contact Us page and social media channels through the Footer of the page.
  UPDATE - Was decided a footer was having too much of an impact on design, and access to socila links was provided through contact
  us page.
* User Story 4 - As the business owner, I provide customers with a clear and consistent UX in-keeping with the Barbell Gym brand.
* User Story 5 - As a user, I can easily access the different products available from the Barbell shop.
* User Story 6 - As a user, if applicable, I can choose the colour and size of my product before adding to the basket.
  UPDATE - Colour options no longer required
* User Story 7 - As a user, I am notified when I have successfully added a product to the basket and the quantity of products added is shown next to the basket icon.
* User Story 8  - As a user I can submit my enquiry about a class or PT session.
  UPDATE - Business decision to direct customers towards social channels
* User Story 9 - As an Admin/Superuser I can edit or delete a product.
  UPDATE - added functionality allows user to add/edit/delete a product, class or personal trainer
* User Story 10 - As a customer, when I go to the basket page I can see the the products I have added to basket and overall total of my order.
* User Story 11 - As a customer I can remove a specific item from my basket.
* User Story 12 - As a customer I can adjust the quantity of specific items in my cart.
* User Story 13 - As a customer I can remove all items from my basket with one click.
* User Story 14 - As a customer, I can proceed to the checkout page from the basket review page.
* User Story 15 - As a customer I can choose to save my payment details for next time I make an order.
* User Story 16 - As a customer, through the contact us page I can access the business'  social media accounts and their location on google maps.
* User Story 17 - As a user, I can sign into my account which gives me access to my order history and payment details.
* User Story 18 - As a user, If i'm not signed up I can register for an account.
* User Story 19 - As a customer when I am signed in, I can access my order history, and see my previous orders.


### Design ###

* Colour scheme - The colour scheme is black and white matching the brand and ethos of the business.

* Typography - the 'Big Shoulders Stencil Text' font is used as it is bold, easy to read and suits the military old school
feel of the brand.

* Imagery - The Barbell Gym logo nd images from the gym are shown throughout the site to draw attention as the business' distinctive features. Background images include images
from the gym and classes to provide an insight to users of what the gym looks like, can be seen throughout various pages of the site. Images of the products
were used to show what the products looked like.

* WireFrames:
Desktop and Mobile wireframes - [https://marvelapp.com/prototype/2c593h96]

* Entity relationship diagram

![Barbell Gym db diagram](media/bbgym_data_schema.jpg)

There are 6 models set up in Django DB
    
    Users
    UserProfiles
    Emails
    Orders
    Order line item
    Categories
    Products
    Classes
    Personal Trainers

* The sign in/registration/verification functionality is provided by the built-in Django Allauth,
  Integrated set of Django applications addressing authentication, registration, account management
  as well as 3rd party (social) account authentication. more here - [https://django-allauth.readthedocs.io/en/latest/]
* When a user registers, they provide their own username, password and email-address, which is then used to login,
  once email is verified. The email is assigned to the User id. once logged in this creates a session. The session id
  is then used to permit/restrict access for that user. i.e. if the user has Superuser access (granted by an admin) then
  they will have access to the Class, Product and PT management options in the menu. If not they will only be able to see their profile.
* In their UserProfile, they will be able to access their delivery information if they have opted to save it when placing an order and
  any orders they have placed. the user will be able to see order number, order details (products, sizes quantity, order date) and order total.
  There is a function to update their delivery information which should pre-populate the delivery address form when the next order is placed.
* Once an order has been placed, an email confirmation will be sent to the email address either pre-populated from the UserProfile Id if the
  info has been saved, or whichever email address is submitted to the order form.
* The orders are comprised of Order line-items which attaches itself to the order id and provides details on each product, the quantity, the sizes
  ordered and the price.
* The information in the OrederLine item depends on the products selected. The order_line_item is generated when the product id are called from
  the basket. The product id will determine the name of the product, whether or not that product has sizes, the availble sizes in that product and the price.
  There is also a in_stock boolean field that allows the admin to push products out of stuck, which prevents customers from adding it to their basket.
* The products are placed into categories, adn each catgeory id detrmines which product is in that category. This allows groups of products to be searched
  together and helps with customer navigation of the site.
* The Classes and Personal trainer model is part of the training app and are services provided by the Barbell gym, they do not relate to any other model.
* If a user has Superuser access they can access the management elements of the nav bar. This allows them to add products, classes and personal trainers to the site.
  They can also access the edit and delete functionality for any of the instances of the aformentioned models, by targeting the id of that instance. The edit function
  takes the user to a form which is pre-populated with the existing instances details which can then be altered.

* Features:
    * Responsive layout on mobile and tablet
    * Collapsible nav bar for mobile view
    * Authentication (Login/Register/email verification functionality)
    * Search
    * Defensive programming
    * Integrated with Stripe to take payments
    * Sends out confirmation emails through gmail
    * Inbuilt feedback system to keep user informed

### Technologies: ###

* Languages - 
HTML5
CSS3
JS
Python

* Frameworks/libraries/programs - 
  https://favicon.io/favicon-converter/ - Used to create logo for title.

  https://fonts.google.com/ - used for font design.

  https://www.rawpixel.com/image/2337562/free-illustration-png-frame-black-texture - Used for background image.

  Django - https://www.djangoproject.com/ to run site on and use of Jinja templating and builtin functionality (e.g. allauth).

  Bootstrap - https://getbootstrap.com/ Used for responsiveness and design of site,
  used to implement responsive header

  Heroku - https://www.heroku.com/ cloud based platform used to deploy the Barbell planner.

  Free formatter - https://www.freeformatter.com/css-beautifier.html used to beautify CSS3 code.

  W3C markup Validator - https://validator.w3.org/ to check HTML formatting.

  JS Hint - https://jshint.com/ - to test JQuery formatting.

  db diagram - https://dbdiagram.io/ - to create entity relationship diagram

  

### Testing

The W3C Markup Validator, W3C CSS, JSHint PEP8 online Validator Services were used to validate the project pages to ensure
there were no syntax errors.

* [W3C Markup validator](https://validator.w3.org/#validate_by_input)
  1 error were found across multiple pages: - 'unclosed element div'. Fix - added in missing closing tag
  1 error found across all pages 'Duplicate id' Fix - this has not been addressed as the id appears on the
  page source for 2 different html pages and is required for the drop-down element of the nav-bar.
  1 error found at checkout page 'for attribute for label element must be id of non-hidden form'
    Fix - this has been left as id is present in the form, checkout.html, line 92.
  1 error found across training pages - 'p element no allowed as child of h5 in this context'
    Fix - removed surrounding tags from templating logic that includes 'linebreaks' as this
    automatically generates paragraph tags.

* [W3C CSS validator](https://jigsaw.w3.org/css-validator/validator) No errors were returned from the CSS validator

* [JSHint](https://jshint.com/) 1 error against 2 pages 'Missing semi-colon'. Fix - added missing semi-colon.

* [PEP8 online](http://pep8online.com/checkresult) 1 error 'line too long >79' Fix - This has been left as changing
  this would impact the readability/function of the code.

### Testing user stories ###

* User Story 1 - As a customer, I land on the hompeage of the site and It's clear what the business is.
  As you land on the homepage of the barbellgym site, there is a large logo and welcome message and the options on the site.

  ![Dashboard screenshot](media/screenshots/user_story_1.JPG)
  ![Dashboard screenshot mob](media/screenshots/user_story_1_mob.JPG)

* User Story 2 - As a customer I can navigate easily to any section of the site regardless of where I am or what device I am using.
  As a user there are clear links on the dashboard for desktop and mobile and dropdown menus for wuicker access to specific areas.

  ![Navigation screenshot](media/screenshots/user_story_2.JPG)
  ![Navigation screenshot](media/screenshots/user_story_2_mob.JPG)

* User Story 3 - As a customer I can easily access the Contact Us page and social media channels through the Footer of the page.
  SEE ABOVE - user story no longer valid.
* User Story 4 - As the business owner, I provide customers with a clear and consistent UX in-keeping with the Barbell Gym brand.
  Design is consistent throughout the site with the Barbell gym colours and logo.
* User Story 5 - As a user, I can easily access the different products available from the Barbell shop.
  By clicking on the Barbell shop nav item, I can access specific categories of products, all products and I can also search for products
  using the search bar in the nav.

  ![Product through nav screenshot](media/screenshots/user_story_5.JPG)
  ![Product through search screenshot](media/screenshots/user_story_5_search.JPG)
  ![Product through search mob screenshot](media/screenshots/user_story_5_mob.JPG)

* User Story 6 (UPDATED) - As a user, if applicable, I can choose the size of my product before adding to the basket.
  By clicking on the product I am taken to the product detail page where I can select size and quantity.

  ![Size selector screenshot](media/screenshots/user_story_6.JPG)
  ![Size selector mobile screenshot](media/screenshots/user_story_6_mob.JPG)

* User Story 7 - As a user, I am notified when I have successfully added a product to the basket and the quantity of products added is shown next to the basket icon.
  When I click on add to basket, i'm presented with a message with the details of what i've added to the basket and the option to proceed to checkout.

  ![Add to basket notification](media/screenshots/user_story_7.JPG)
  ![Add to basket notification tablet](media/screenshots/user_story_7_tablet.JPG)

* User Story 8  - As a user I can submit my enquiry about a class or PT session.
  See above - User Story Invalid
* User Story 9 - As an Admin/Superuser I can add, edit or delete a product, class or PT.
  As a superuser or admin, if i am logged in I can easily create, edit and delete classes, products or Pt's within the website.
  ![Add class screenshot](media/screenshots/user_story_9_add_class.JPG)
  ![Add product screenshot](media/screenshots/user_story_9_add_product.JPG)
  ![Add pt screenshot](media/screenshots/user_story_9_add_pt.JPG)
  ![Delete class screenshot](media/screenshots/user_story_9_delete_class.JPG)
  ![Delete product screenshot](media/screenshots/user_story_9_delete_product.JPG)
  ![Delete pt screenshot](media/screenshots/user_story_9_delete_pt.JPG)
  ![Edit class screenshot](media/screenshots/user_story_9_edit_class.JPG)
  ![Edit product screenshot](media/screenshots/user_story_9_edit_product.JPG)
  ![Edit pt notification](media/screenshots/user_story_9_edit_pt.JPG)
  ![Delete product success message](media/screenshots/user_story_9_delete_product_success_msg.JPG)
  ![Edit product success message](media/screenshots/user_story_9_edit_product_success_msg.JPG)

* User Story 10 - As a customer, when I go to the basket page I can see the the products I have added to basket and overall total of my order.
  When I navigate to the basket page I can see the products in my basket - and i'm presented with a notification of how to collect my order
  if I proceed.

  ![Warning message at basket](media/screenshots/user_story_10.JPG)
  ![Basket view](media/screenshots/user_story_10_basket.JPG)
  ![Basket view mob](media/screenshots/user_story_10_basket_mob.JPG)

* User Story 11 + 13 - As a customer I can remove a specific item from my basket.
  As a user when I click remove below a specific item, it will remove the total number of that product
  ![Remove from basket success msg](media/screenshots/user_story_11.JPG)

* User Story 12 - As a customer I can adjust the quantity of specific items in my cart.
  When i'm in the basket page, I can use the plus or minus for to alter the quantity of my product,
  then click update which will update my basket.

  ![Update from basket success msg](media/screenshots/user_story_12.JPG)

* User Story 14 - As a customer, I can proceed to the checkout page from the basket review page.
  As a customer I can click on secure checkout and I'm taken to the checkout page.

  ![Checkout page screenshot](media/screenshots/user_story_14.JPG)
  ![Checkout page screenshot mob](media/screenshots/user_story_14_mob.JPG)


* User Story 15 - As a customer I can choose to save my payment details for next time I make an order.
  As a customer, as long as I have created an account my details can be saved against my User Profile
  for the next time I order, and they can be viewed in my profile.

  ![Save details for payment next time](media/screenshots/user_story_14_mob.JPG)

* User Story 16 - As a customer, through the contact us page I can access the business'  social media accounts and their location on google maps.
  As a customer, when I land on the contact us page I can access all the social media platforms associated with the business and I'me also provided
  a location of the gym.

  ![Contact Us screenshot](media/screenshots/user_story_16.JPG)
  ![Contact Us screenshot mob](media/screenshots/user_story_16_mob.JPG)

* User Story 17 + 18 - As a user, I can sign into my account which gives me access to my order history and payment details.
  Once I have registered and account and verified my email address for the site, I can log in and access my profile
  ![Sign in screenshot mob](media/screenshots/user_story_17_mob.JPG)
  ![Sign in screenshot](media/screenshots/user_story_17.JPG)
  ![Sign up screenshot](media/screenshots/user_story_17_register.JPG)

* User Story 19 - As a customer when I am signed in, I can access my order history, and see my previous orders.
  Given I have signed in as a customer I can access my profile, whenre my delivery details are stored and they can
  be updated and I can view my order history.

  ![My profile screenshot](media/screenshots/user_story_19.JPG)
  ![My profile screenshot mob](media/screenshots/user_story_19_mob.JPG)

* Additional functionality - As an admin/superuser - I can mark products as out of stock to prevent customers from
  buying them and providing customer experience.
  ![Stock management screenshot mob](media/screenshots/oos_prod_page_mob.JPG)
  ![Stock management screenshot](media/screenshots/oos_prod_detail_page.JPG)

* Additional functionality - As a customer, I receive a confirmation email with my order details that match my order
  confirmation from the site.

  ![Order confirmation site screenshot](media/screenshots/order_confirmed.JPG)
  ![Order confirmation email screenshot](media/screenshots/order_confirmation_email.JPG)

* Additional functionality - As non admin/superuser, i don't have access to edit products either from the nav
  or by manipulating the url.
  ![Restricted access nav screenshot](media/screenshots/non_superuser_access_profile.JPG)
  ![Permissions error screenshot](media/screenshots/permissions_error.JPG)





### Further testing ###
     

* Bugs:

Please see all code bugs listed in the screenshot below:
  ![Bugs](media/screenshots/bugs.JPG)

PLEASE NOTE: During working on this project, a db.json file was comitted to github with test user details from
Dev environment. None of this data was sent to the deployed app in production, and once the issue had been
identified, the following steps were taken to mitigate:
  * The data that was identified in the file was removed from the dev environment.
  * The db.json file was deleted as it wasn't being used
  * Production data (users, products, classes) were created in the admin console in production, manually.

* Potential enhancements:

    i. Ideally there should be and order management system for the superuser, using a boolean object,
      when the order is fulfilled (true) an email is sent to the customer to let them know the order is ready
      to be collected
    ii. Additional defensive programming to prevent customers from adding out of stock products to their basket. 

<h2 style="text-align: center">Deployment</h2>

### Requirements ###


* Python3
* GitHub account
* Heroku account
* Gitpod or an IDE of your choice
* Stripe account
* AWS account
* Email provider

### GitHub Pages ###
The project was created through GitHub using the following steps...

#### Log in to GitHub and locate the GitHub Repository ####

* Going to [github.com](https://github.com)
* Clicking on the 'New' button in repositories section
* Selecting the CI template provided by Code Institute [template here](https://github.com/Code-Institute-Org/gitpod-full-template)
* Creating a name for my new repo and clicking on the 'Create Repository' button at the bottom of the screen.
* Once directed to my new repo, I clicked on the 'Gitpod' button which created my workspace

### Deployment to Heroku

**Create application:**
* Navigate to Heroku.com and login.
* Click on the new button.
* Select create new app.
* Enter the app name - this should be the same as the repo name to reduce complexity.
* Select region.

**Connect to Github Repo:**

* Click the deploy tab and select GitHub - Connect to GitHub.
* A prompt to find a github repository to connect to will then be displayed.
* Enter the repo name for your project in Github and click search.
* Once the repo has been found, click the connect button.

**Set environment variables:**

Go to the 'Settings' section at the far right of the menu and click 'Reveal Config Vars' button,
for my project I added the following:

KEY	VALUE
1. AWS_ACCESS_KEY_ID	
2. AWS_SECRET_ACCESS_KEY	
3. DATABASE_URL	
4. EMAIL_HOST_PASS	
5. EMAIL_HOST_USER	
6. SECRET_KEY_MS4	
7. STRIPE_PUBLIC_KEY	
8. STRIPE_SECRET_KEY	
9. STRIPE_WH_SECRET	
10. USE_AWS	
11. CSRF_COOKIE_SECURE 

**Enable automatic deployment:**
* Go to 'Deploy' section
* In the 'Automatic Deploys' section, I chose the main branch (choose the branch you want to deploy from) then click 'Enable Automation Deploys'.

**Static & Media Files**
To host static and media files you will need an AWS S3 Bucket. You will need an account and create an S3 bucket. From here set up a group,
a policy and user in the IAM environment. For more information, please look [here](https://aws.amazon.com/s3/)
**Forking the GitHub Repository**

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

* Log in to GitHub and locate the GitHub Repository**

* At the top of the repository section just above the "Settings" button on the menu, click the "Fork" button.
  The original repository in your GitHub account should now have duplicated.

**Run on Local Environment**

* Set up the environment variables either in env.py file or in gitpod account settings
  (ensure to add env.py to gitignore file):

* Import os
  os.environ("SECRET_KEY", "Added by developer")
  os.environ("STRIPE_PUBLIC_KEY", "Added by developer")
  os.environ("STRIPE_SECRET_KEY", "Added by developer")
  os.environ("STRIPE_WH_SECRET", "Added by developer")
  os.environ("DATABASE_URL", "Added by developer")

* Next, run migrations to create the database. Do this by running the command 'python3 manage.py makemigrations'
  followed by python3 manage.py migrate (use makemigrations --dry-run and migrate --plan to confirm what is being migrated).

* Create a superuser to have access to the admin panel. python3 manage.py createsuperuser

* Now run the app locally using python3 manage.py runserver

**Making a Local Clone**

* Log in to GitHub and locate the GitHub repository, under the repository name, click "clone or download".
* To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
* Open Git Bash
* Change the current working directory to the location where you want the cloned directory to be made.
* Type git clone, and then paste the URL you copied in Step 2.
   * $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
* Press Enter. Your local clone will be created.
   * $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.

Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages:
> pip install -r requirements.txt


### Credits


### Code ###
* Code has been credited throughout the project, Code institute
  Boutique Ado project helped support the ecommerce side of the site.
  Stackoverflow was used alot for answers on bugs.


### Content ###
* Content was inspired by Gymshark and MyProtein websites
  Content is from the Barbell Gym, locally run business in West Lothian.

#### Image credits ####
* 'No image' image was taken from Boutique ado project
* rawpixel was used for background overlay
* All images and logos were provided by the barbell gym

### Acknowledgements ###
Huge thanks to Aaron Sinnot, my mentor and the slack community
from helping me through this project. Massive thanks to Gaving Smith
at the Barbell Gym for trusting me with his brand.