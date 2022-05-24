## Bugs and Fixes During the Development Process


# Lighthouse


## No Login Required 
### Sign-in:
#### Mobile
![Mobile-Sign-in](docs/images/lighthouse/signin-mobile.jpg)
#### Desktop
![Desktop-Sign-in](docs/images/lighthouse/signin-desktop.jpg)
### Sign-up:
#### Mobile
![Mobile-Sign-up](docs/images/lighthouse/signup-mobile.jpg)
#### Desktop
![Desktop-Sign-up](docs/images/lighthouse/sign-up-desktop.jpg)
### External Homepage:
#### Mobile
![Mobile-External](docs/images/lighthouse/external-landing-page-mobile.jpg)
#### Desktop
![Desktop-External](docs/images/lighthouse/external-landing-page-mobile.jpg)
### Root Page:
#### Mobile
![Mobile-Root](docs/images/lighthouse/homepage-mobile.jpg)
#### Desktop
![Desktop-Root](docs/images/lighthouse/homepage-desktop.jpg)
## Sign-Login Required
### Index Page (Links)
#### Mobile
![Mobile-Index](docs/images/lighthouse/index-page-mobile.jpg)
#### Desktop
![Desktop-Index](docs/images/lighthouse/index-page-desktop.jpg)
### Add A Link
#### Mobile
![Mobile-Add](docs/images/lighthouse/add-a-link-mobile.jpg)
#### Desktop
![Desktop-Add](docs/images/lighthouse/add-a-link-desktop.jpg)
### Edit A Link
#### Mobile
![Mobile-Edit](docs/images/lighthouse/edit-a-link-mobile.jpg)
#### Desktop
![Desktop-Edit](docs/images/lighthouse/edit-a-link-desktop.jpg)


#### *Desktop*:


## [CSS](https://jigsaw.w3.org/css-validator/):
Checking by URL there were a lot of errors coming from the bootstrap and font awesome source code.  However my CSS file was tested by direct upload was found to be free from errors
![CSS-check](docs/images/css-check.jpg)
<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

## [PEP8](http://pep8online.com):
Before using the pep8 validator I ran ``` autopep8 --in-place --aggressive --aggressive <file name> ``` on all py files.  

Due to this, the only error I found was in settings.py with ``` AUTH_PASSWORD_VALIDATORS ``` & ``` STATICFILES_STORAGE ```.   

![settings.py pep8 errors](docs/images/PEP8-Validation.jpg) 

The first appears to be a long-standing issue with using the pep8 checker with Django, and there have been some [suggest resolves](). However, Django seems to think shortening these lines is ill advisable. For this reason, I left them to be longer than 80 characters. 

# Manual testing
Below is a summary of how I manually tested each user story.

## As an **Admin** I can...

Here I have only tested the admin panel relating to the JOB_SEARCH app, as the other sections relate to imported libraries.

| Checked | ...**use a text editor within the admin panel** so that **I can create a job description in a way that is clear and appeals to the eye when creating a job post** |



## As an **Unregistered User** I can...

| Checked | ...**quickly determine the subject of the site** so that **from the landing page, I can see if I want to continue spending my time on this site and register** |


## As a **Site User** I can...


[Back to Readme](README.md)