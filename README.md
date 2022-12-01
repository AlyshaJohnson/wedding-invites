# Project Portfolio 4 - 

Purpose: 

Aim:

![Responsive Mockup](./wedding-invites/static/media/readme_images/responsive_mockup.jpg/)

The live link can be found here - <insert link>

## 1. Design and Development

For the design of this Wedding Invite app, the 5 pillars of User Experience Design (UXD) were used to cover the strategy, scope, structure, skeleton and surface to make sure the design is intuitive, simple and enjoyable.

### 1.1 Strategy

Initial interviews with the stakeholder were conducted to understand their high-level requirements for the app. This allowed further research to be conducted into user profiles / groups benefitting.

The target user audience…

Competitor research was then carried out...

### 1.2 Scope

A brainstorming session was held with the customer to generate user themes and epics, which user stories can then be generated from. Once the user stories had been generated and confirmed, they were prioritised and time bound. For a full list of all user stories, please click [here](https://github.com/AlyshaJohnson/project-portfolio-4/issues?q=).

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

![Invite](/static/media/readme_images/invite.png)

**Countdown Clock**

![Clock](/static/media/readme_images/clock.png)

**Venue Information**

![Venue](/static/media/readme_images/venue.png)

**List of hotels**

![Hotels](/static/media/readme_images/hotels.png)

**Gallery**

![Gallery](/static/media/readme_images/gallery.png)

**Profile page with editting**

![Profile](/static/media/readme_images/profile.png)

**Overview for admin**

![Admin](/static/media/readme_images/admin.png)

**Send messages**

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
- Input form validation
- Code validation testing 
- User experience tesing

### 4.1 Initial Developer Testing

As the project was developed and coded, developer testing was conducted to reduce the impact of bugs and errors in the code. This testing consisted of general debugging of written code based off gitpod IDE recommendations; running through input validator testing scenarios to check for input errors; and testing on different browsers.

**General Debugging**

Bugs were captured throughout the course of the project using the 'issues' object within GitHub. 

**Input Validator Testing**

**Browser / Device testing**

The development of this app was conducted on Google Chrome, therefore extensive testing was conducted on this browser. This was used as a benchmark against Firefox and Safari.

The elements of testing conducted on each browser are:
<insert list of testing performed and why - see example below>
- User Experience - what does the quiz look like; is the flow through the quiz the same; are all elements where they are expected?
- Functionality - do the buttons work as expected; does the question counter count?
- Performance - how responsive is the site?

The user experience is consistent on Chrome, Firefox and Safari. The instruction videos in Safari do not load - this bug has been captured.

Responsive design is important, CSS code had to be amended and adjusted to make sure the app could work on a number of devices. There were a number of user experience bugs that were produced when testing. These have now been fixed in the code.

### 4.2 Code Validation Testing

Using tools such as W3C validator, Jigsaw and Lighthouse gives visibility of any code, scripts or elements that are causing any errors. The results for the site are as follows:

**HTML**
- <insert report number> errors were returned when passing through the official [W3C validator](<insert link to report>)

**CSS**
- <insert report number> errors were found when passing through the official [(Jigsaw) validator](<insert link to report>)

**JS**
- [JSHint](https://jshint.com/) was used to check for errors in the JS code.
- For script.js, there were <insert report number> errors and <insert report number> warnings.
- For instructions.js, there were <insert report number> errors and <insert report number> warnings.
<insert any methods used to reduce number of errors and warnings>

**Performance**
- Results can be seen through the official [Lighthouse](<insert link to report>) report.

As part of the performance test through Lighthouse, some changes were made:
- Accessibility (aria-label) tags were implemented on all buttons to improve the score from 82 to 100.
- The cache policy was amended to increase the length of number of seconds the browser should cache the resource.
- The image file sizes needed to be compressed so reduce the impact on performance. This was successfully done using [tinyPNG](https://tinypng.com/).

### 4.3 User Testing
This app has been tested by a small group of 10 users in which some feedback was captured in the design and some errors in functionality and spelling were corrected.

UI improvements made:
- <list any improvements to UI that were made here>

Errors / bug fixes:
- <list errors/bugs that were found, what the problem was and how they were fixed>

### 4.4 Unfixed Bugs

- <list unfixed bugs here>

## 5. Deployment

This website was deployed using GitPages and following the below steps:

GitHub pages deployment
1. Log in to GitHub
2. In the Repository section, select the project repository that you want to deploy
3. In the menu located at the top of this section, click 'Settings'
4. Select 'Pages' on the left-hand menu - this is around halfway down
5. In the source section, select branch 'Master' and save
6. The page is then given a site URL which will be seen above the source section, it will look like the following:

![](/static/media/readme_imagesgithub_deployment.jpeg/)

Please note it can take a while for this link to become fully active.

Forking the GitHub Repository
To make changes to this repository without affecting it, a copy can be made by 'Forking' it. This ensures the original repository remains unchanged.
1. Find the relevant GitHub repository
2. In the top right corner of the page, click the Fork button (under account)
3. The repository has now been 'Forked' and you have a copy to work on

Cloning the GitHub Repository
Cloning a repository will allow a local version of the repository will be downloaded so can be worked on. Cloning is also a great way to backup work.
1. Find the relevant GitHub repository
2. Press the arrow on the Code button
3. Copy the link that is shown in the drop-down
4. Now open Gitpod & select the directory location
5. In the terminal type 'git clone' & then paste the link copied from GitHub
6. Press enter and a local clone will be created.

The ‘<insert app name>’ was deployed with the help of the Heroku app.

## 6. Credits

### 6.1 Content

Logos and Fonts:
- The fonts were taken from [GoogleFonts](https://fonts.google.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

Tutorials and support:
- General guidance, information and limitations on elements, attributes, and methods from [w3schools](https://www.w3schools.com/default.asp) and [MDN Web Docs](https://developer.mozilla.org/en-US/)
- <insert list of tutorials followed>
- The many people who 'beta tested' the quiz app.

### 6.2 Media

Any photos used throughout the app are stock imagery from the following services:
- [unsplash](https://unsplash.com/)
- [FreeImages](https://www.freeimages.com/)
- [PikWizard](https://pikwizard.com/)

Credit goes to the following artists for use of their images on the site:
- [Hannah Olinger](https://unsplash.com/@hannaholinger) on Unspalsh for the couple images in the gallery for the demo.
- [Evie Shaffer](https://unsplash.com/@evieshaffer) on Unsplash for the invite images.
- [Alex Grey](https://unsplash.com/@sharonmccutcheon) on Unsplash for the background image.
  

<insert any other media used throughout the app/site here>

### 6.3 Research

As mentioned in the design section, competitor research was conducted. These are credited below:
- <insert list of research links>

https://realpython.com/customize-django-admin-python/
https://ordinarycoders.com/blog/article/django-user-register-login-logout

### 6.4 Special Thanks