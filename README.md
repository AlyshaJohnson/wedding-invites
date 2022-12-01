# Project Portfolio 4 - 

Purpose: A wedding invite generator based on user input.

Aim: To create and manage wedding invites and guest list, so party-goers can respond with RSVP and preferences.

![Responsive Mockup](/static/media/readme_images/responsive_mockup.jpg/)

The live link can be found here - https://wdg-invite.herokuapp.com/invite/

## 1. Design and Development

For the design of this Wedding Invite app, the 5 pillars of User Experience Design (UXD) were used to cover the strategy, scope, structure, skeleton and surface to make sure the design is intuitive, simple and enjoyable.

### 1.1 Strategy

Initial interviews with the stakeholder were conducted to understand their high-level requirements for the app. This allowed further research to be conducted into user profiles / groups benefitting.

Competitor research was then carried out on similar sites to get an idea of what is currently in the market.

### 1.2 Scope

A brainstorming session was held with the customer to generate user themes and epics, which user stories can then be generated from. Once the user stories had been generated and confirmed, they were prioritised and time bound. For a full list of all user stories, please click [here](https://github.com/AlyshaJohnson/project-portfolio-4/issues?q=).

![Brainstorm](/static/media/readme_images/brainstorm.png)

The SP, or Story Point, is a relative prediction of the time taken to complete the user story against a baseline. The baseline user story was "Create Account".

To complete all user stories, the predicted time it would take would be 8 weeks. As the customer required a release date of the 1st December 2022, a minimum set of user stories were agreed and reviewed weekly. The final agreed set of user stories were:

| USER STORY # | TITLE                            | PRIORITY |
|--------------|----------------------------------|----------|
| #3           | Add new guest                    | Mo       |
| #16          | Send invite                      | Mo       |
| #17          | Send messages                    | Mo       |
| #42          | Admin overview                   | Mo       |
| #23          | Create food questionnaire        | Mo       |
| #34          | Respond to questionnaires        | Mo       |
| #25          | Create playlist                  | S        |
| #13          | Edit image description           | S        |
| #26          | Edit additional information      | Co       |
| #27          | Clear additional information     | Co       |
| #39          | Combine with other party members | S        |
| #15          | Delete image                     | S        |
| #12          | Add image to gallery             | S        |
| #33          | View information                 | Mo       |
| #35          | Create account                   | Mo       |
| #32          | Edit contact information         | Mo       |
| #18          | Add contact information          | Mo       |
| #36          | Sign in                          | Mo       |
| #6           | View guest list                  | Mo       |
| #20          | Add date of wedding              | Mo       |
| #31          | Edit venue information           | Mo       |
| #30          | Edit wedding date                | Mo       |
| #37          | New password                     | Co       |
| #5           | Delete guest                     | Mo       |
| #4           | Edit guest information           | Mo       |
| #29          | Delete local hotel information   | Co       |
| #19          | Add venue information            | Mo       |
| #21          | Add local hotel information      | Co       |
| #22          | Add additional information       | Co       |
| #28          | Edit local hotel information     | Co       |

### 1.3 Structure

From the user stories, content, data, features and functionality can be determined.

**For the content / features:**

- Sign in page - directs to invite
- Sign up page - generated from email
- Admin overview
    - Analytics
        - no. of RSVPs
        - no. of responses to questionnaires
        - no. of song requests
    - Send invite button
        - Warning of no. of guest who aren't "published"
- Invitation
    - Formal invitation to wedding
    - RSVP form
- Profile page
    - Profile information
    - Song list
    - Questionnaire answers
- Information page
    - Countdown clock
    - Venue information
    - Menu
    - Hotel information
    - Contact information
    - Additional information
- Gallery
    - View of images stored in database
    - Description under image

**Data Model:**

The following data model was created:

![Data Model](/static/media/readme_images/data_model.jpeg)

### 1.4 Skeleton

When the structure of the app, features and data model had been determined, a wireframe for each view could be created:

**Invite**

![Invite](/static/media/readme_images/wf-invite.png)

**Information Page**

![Info](/static/media/readme_images/wf-info.png)

**Gallery**

![Gallery](/static/media/readme_images/wf-gallery.png)

**Profile**

![Profile](/static/media/readme_images/wf-profile.png)

### 1.5 Surface

**Colour Palette**

![Colour Palette](/static/media/readme_images/colors.jpg)

- The app's primary colours are (from left to right) #E05F72, #BD8185, #FFF5F6 and #A2B597 as seen in the picture above. These are based of the dark pink colour extracted from the background image.Then using the online tool [colorspace](https://mycolor.space/) to generate the others, to make sure they complement and contrast.
- #E05F72 is one of the main colours in the background image, and was used to generate the colour theme.
- #BD8185 is used as the font colour through the majority of the site. It is also used as the border colour in the header and on icon buttons in the nav bar.
- #FFF5F6 is used as the main background colour on the div-cards to contrast the background image.
- #A2B597 is used as the button and link colour.

**Typography**
- Petit Formal Script is used for headings and header elements. The fallback font is cursive.
- Nunito Sans is used for all other text elements including paragraphs, button labels, lists, etc. The fallback font is sans serif.
- Both fonts are from Google Fonts.

## 2. Technologies used

Several technologies were used to aid the project:

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- Used as the basic building block for the project and to structure the content.
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- Used to style all the web content across the project. 
- [Google Fonts](https://fonts.google.com/)
- Used to obtain the fonts in website
- [Font Awesome](https://fontawesome.com/)
- Used to obtain the icons used throughout website.
- [GitHub](https://github.com/)
- Used to store code for the project after being pushed.
- [Git](https://git-scm.com/)
- Used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- [Gitpod](https://www.gitpod.io/)
- Used as the development environment.
- [Balsamiq](https://balsamiq.com/)
- Used to create the wireframes for the project.
- [Colormind](http://colormind.io/)
- Used to determine colour palette throughout website.
- [Tiny.png](https://tinypng.com/)
- Used to compress my images so that the page would load faster.
- [Techsini](http://techsini.com/multi-mockup/index.php)
- Used to generate multi-device mockup.
- [Freeformatter CSS Beautify](https://www.freeformatter.com/css-beautifier.html)
- Used to accurately format CSS code.
- [Freeformatter HTML Formatter](https://www.freeformatter.com/html-formatter.html)
- Used to accurately format HTML code.
- [Python](https://www.python.org/)
- Python is the core programming language used to write all of the code in this game to make it fully functional.
- [Heroku](https://dashboard.heroku.com/apps)
- Used to deploy the app
- [PythonTutor](https://pythontutor.com/)
- Used to visualise the flow of code as it is executed
- [Pep8](http://pep8online.com/)
- Used to test my code for any issues or errors.

## 3. Features

### 3.1 Existing Features

The features deployed for this app are as follows:

**Invite**

The invite uses the information from the wedding object to display the relevant information to the user.

![Invite](/static/media/readme_images/invite.png)

**Countdown Clock**

A countdown clock to the big day. This uses the admin input of wedding date and time to count down to.

![Clock](/static/media/readme_images/clock.png)

**Venue Information**

The venue information is gathered from the wedding object. The site uses google maps api's to generate the latitude and longitude coordinates from the venue address input and displays these on the map. The venue elements on the screen are buttons to allow the user to toggle between the two venues on the map. 

![Venue](/static/media/readme_images/venue.png)

**List of hotels**

A list of hotels generated from the hotels object in the database.

![Hotels](/static/media/readme_images/hotels.png)

**Gallery**

An image gallery showing images from the gallery object in the database.

![Gallery](/static/media/readme_images/gallery.png)

**Profile page with editting**

The profile page shows information about the user. This information can be editted by the user.

![Profile](/static/media/readme_images/profile.png)

**Overview for admin**

The overview to the admin user, gives a count of the number of certain objects in the database, for example, the number of RSVPs recieved verses the total number of guests.

![Admin](/static/media/readme_images/admin.png)

**Send messages**

Allows the admin to send an email to the guest list with any updates necessary before the big day.

![Message](/static/media/readme_images/message.png)

### 3.2 Future Features

There is an addition of 3 weeks worth of work still to perform to give the customer everything they require. This includes the following user stories:

| USER STORY # | TITLE                        | PRIORITY |
|--------------|------------------------------|----------|
| #2           | Download CSV template        | Co       |
| #24          | Upload menu                  | S        |
| #14          | Edit image order             | S        |
| #11          | Change invitation font       | W        |
| #10          | Import invitation background | W        |
| #9           | Select invite template       | W        |
| #8           | Link accounts                | S        |
| #7           | Export data                  | Co       |
| #1           | Upload guest list            | Co       |

## 4. Testing

Multiple layers of testing were performed on this project including:
- Bug capturing during development
- Automated Testing
- Code validation testing 
- User experience tesing

### 4.1 Initial Developer Testing

As the project was developed and coded, developer testing was conducted to reduce the impact of bugs and errors in the code. This testing consisted of general debugging of written code based off gitpod IDE recommendations; running through input validator testing scenarios to check for input errors; and testing on different browsers.

**General Debugging**

Bugs were captured throughout the course of the project using the 'issues' object within GitHub. 

**Automated Testing**

Some automated tests were written for testing views of the app. This is handy in case packages need upgrading, or major changes to the app are made. In this case, automated tests can be run first, to find obvious errors caused by the changes. After that, manual testing should still be performed.

The tests are run by entering 'python3 manage.py test' in the terminal window (inside the project folder). This will automatically run all test. If running tests in quick succession, it's recommended to add --keepdb at the end, so the database doesn't have to be rebuild for every test cycle. The test in the suite for this project all pass, but if one would fail, it would be displayed with a clear error message, so errors can be solved.

Unfortunately, the test datebase failed to be created and therefore could not run the tests.

![Automated Tests](/static/media/readme_images/auto-test.png)

**Browser / Device testing**

The development of this app was conducted on Google Chrome, therefore extensive testing was conducted on this browser. This was used as a benchmark against Firefox and Safari.

The elements of testing conducted on each browser are:
- User Experience - what does the app look like; is the flow through the app the same; are all elements where they are expected?
- Functionality - do the buttons work as expected; do the forms work as expected?
- Performance - how responsive is the site?

The user experience is consistent on Chrome, Firefox and Safari.

Responsive design is important, CSS code had to be amended and adjusted to make sure the app could work on a number of devices. There were a number of user experience bugs that were produced when testing. These have now been fixed in the code.

### 4.2 Code Validation Testing

Using tools such as W3C validator, Jigsaw and Lighthouse gives visibility of any code, scripts or elements that are causing any errors. The results for the site are as follows:

**HTML**
- 0 errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwdg-invite.herokuapp.com%2F)

**CSS**
- 0 errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fwdg-invite.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

**JS**
- [JSHint](https://jshint.com/) was used to check for errors in the JS code.
- For script.js, there were 0 errors and 11 warnings.

**Performance**
- Results can be seen through the official [Lighthouse](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Fwdg-invite.herokuapp.com%2Finvite%2F&strategy=mobile&category=performance&category=accessibility&category=best-practices&category=seo&category=pwa&utm_source=lh-chrome-ext) report.

As part of the performance test through Lighthouse, some changes were made:
- Accessibility (aria-label) tags were implemented on all buttons to improve the score.
- The cache policy was amended to increase the length of number of seconds the browser should cache the resource.

### 4.3 User Testing
This app has been tested by a small group of 10 users in which some feedback was captured in the design and some errors in functionality and spelling were corrected.

UI improvements made:
- Invite too small for mobile devices

Errors / bug fixes:
- Invite too small for mobile devices.
- RSVP form not submitting

### 4.4 Unfixed Bugs

- Invite too small for mobile devices
- RSVP form not submitting

## 5. Deployment

The master branch of this repository has been used for the deployed version of this application.

### 5.1 Using Github & Gitpod

To deploy this command-line interface application, the [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template) was used, as this enables the application to be properly viewed on Heroku using a mock terminal. 

- Click the `Use This Template` button.
- Add a repository name and brief description.
- Click the `Create Repository from Template` to create your repository.
- To create a Gitpod workspace you then need to click `Gitpod`, this can take a few minutes.
- When you want to work on the project it is best to open the workspace from Gitpod (rather than Github) as this will open your previous workspace rather than creating a new one. You should pin the workspace so that it isn't deleted.
-  Committing your work should be done often and should have clear/explanatory messages, use the following commands to make your commits:
    - `git add .`: adds all modified files to a staging area
    - `git commit -m "A message explaining your commit"`: commits all changes to a local repository.
    - `git push`: pushes all your committed changes to your Github repository.

*Forking the GitHub Repository*

To make changes to a repository without affecting it, a copy can be be made by 'Forking' it. This ensures the original repository remains unchanged.

1. Find the relevant GitHub repository
2. In the top right corner of the page, click the Fork button (under account)
3. The repository has now been 'Forked' and a copy has been made

*Cloning the GitHub Repository*

Cloning a repository will allow a local version of the repository to be downloaded and worked on. Cloning is also be a great way to backup work.

1. Find the relevant GitHub repository
2. Press the arrow on the Code button
3. Copy the link that is shown in the drop-down
4. Now open Gitpod & select the directory location where the clone is to be created
5. In the terminal type 'git clone' & then paste the link copied in GitHub
6. Press enter and a local clone will be created.

### 5.2 Creating an Application with Heroku

Following the below steps using the Code Institute tutorial:

- The following command in the Gitpod CLI will create the relevant files needed for Heroku to install project dependencies `pip3 freeze --local > requirements.txt`. Please note this file should be added to a .gitignore file to prevent the file from being committed. Int he instance of this project, no requirements were created as there were no project dependencies.

1. Go to [Heroku.com](https://dashboard.heroku.com/apps) and log in; create an account if needed.
2. Click the `New` dropdown and select `Create New App`.
3. Enter a name for the new project - all Heroku apps need to have a unique name.
4. Select the region.

*Heroku Settings*
Environment Variables need to be set up - this is a key step to ensuring the application is deployed properly.
- In the Settings tab, click on `Reveal Config Vars` and set the following variables:
    - If using credentials they will need to be added as a variable, the key is the name 'CREDS' and the value is the contents of the creds JSON
    - Add key: `PORT` & value `8000`
- Buildpacks are also required for proper deployment, simply click `Add buildpack` and search for the ones required.
    - For this project, `Python` and `Node.js` were needed, in this order.

*Heroku Deployment*
In the Deploy tab:
1. Connect the Heroku account to the Github Repository following these steps:
    1. Click on the `Deploy` tab and choose `Github-Connect to Github`.
    2. Enter the GitHub repository name and click on `Search`.
    3. Choose the correct repository for the application and click on `Connect`.
2. A choice is given to deploy the project manually or automatically, automatic deployment will generate a new application every time a change is pushed to Github, whereas manual deployment requires the `Deploy Branch` button to be pushed whenever a change is made.
3. Once the deployment method has been chosen, the application will be built and can be opened using the `Open App` button at the top of the page.

![heroku-deployment](/static/media/readme_images/heroku_deployment.png)

## 6. Credits

### 6.1 Content

Logos and Fonts:
- The fonts were taken from [GoogleFonts](https://fonts.google.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

Tutorials and support:
- General guidance, information and limitations on elements, attributes, and methods from [w3schools](https://www.w3schools.com/default.asp) and [MDN Web Docs](https://developer.mozilla.org/en-US/)
- [realpython](https://realpython.com/customize-django-admin-python/
https://ordinarycoders.com/blog/article/django-user-register-login-logout) tutorials on how to do user registration and log in, plus amending the admin page views.
- The many people who 'beta tested' the app.

### 6.2 Media

Any photos used throughout the app are stock imagery from the following services:
- [unsplash](https://unsplash.com/)

Credit goes to the following artists for use of their images on the site:
- [Hannah Olinger](https://unsplash.com/@hannaholinger) on Unspalsh for the couple images in the gallery for the demo.
- [Evie Shaffer](https://unsplash.com/@evieshaffer) on Unsplash for the invite images.
- [Alex Grey](https://unsplash.com/@sharonmccutcheon) on Unsplash for the background image.

### 6.3 Research

As mentioned in the design section, competitor research was conducted. These are credited below:
- [Greenvelope](greenvelope.com)
- [Paperless Post](paperlesspost.com)

### 6.4 Special Thanks

Special thanks goes to the Code Institute community for helping when I was in a bind, especially to Ryan O'Neill and Dirk Ornee.