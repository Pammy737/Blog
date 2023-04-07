# The Blog

A simple blog that allows admin to create, edit, and delete posts ; and enable users to comment on posts after logging in.


## Table of Contents
* [Demonstration](https://github.com/Pammy737/Blog_new/blob/main/README.md#demonstration)
* [How to use](https://github.com/Pammy737/Blog_new/blob/main/README.md#how-to-use)
* [Techniques & Tools](https://github.com/Pammy737/Blog_new/blob/main/README.md#techniques--tools)
* [Upcoming Features](https://github.com/Pammy737/Blog_new/blob/main/README.md#upgradable)
* [Notes](https://github.com/Pammy737/Blog_new/blob/main/README.md#notes)

## Demonstration

* User not logged in

  * if user attempts to enter pages with  __login_required__ decorator
  
    * lead to login page  ->  logged in -> redirect back to where user initially wanted to visit [(Notes: next)](https://github.com/Pammy737/The_Blog/blob/main/README.md#notes)    
      
      * home page 
        ![nolog](https://github.com/Pammy737/The_Blog/blob/main/readme_screenshots/homepage(nolog).png)     
      * post
        ![post nolog](https://github.com/Pammy737/The_Blog/blob/main/readme_screenshots/post.png)
      * posting a comment
        ![comment nolog](https://github.com/Pammy737/The_Blog/blob/main/readme_screenshots/comment(nolog).png)
      * about page
        ![about nolog](https://github.com/Pammy737/The_Blog/blob/main/readme_screenshots/aboutpage(nolog).png)
        
* User logged in

  * admin (admin_only) (first user registered) 
    * home
      ![adminhome](https://github.com/Pammy737/The_Blog/blob/main/readme_screenshots/homepage(adminlog).png)
    * post
      ![adminpost](https://github.com/Pammy737/The_Blog/blob/main/readme_screenshots/post(admin).png)
    * create new post
      ![adminnewpost](https://github.com/Pammy737/The_Blog/blob/main/readme_screenshots/newpost(admin).png)
    * edit post
      ![adminpost](https://github.com/Pammy737/The_Blog/blob/main/readme_screenshots/editpost(adminlog).png)
      
    
  * user   
    * post
      ![postuserlog](https://github.com/Pammy737/The_Blog/blob/main/readme_screenshots/homepage(userlog).png)
    * posted a comment (with the username below)
      ![commentusrelog](https://github.com/Pammy737/The_Blog/blob/main/readme_screenshots/leavedcomment(userlog).png) 
    * about page
      ![aboutuserlog](https://github.com/Pammy737/The_Blog/blob/main/readme_screenshots/aboutpage(userlog).png)
      
* if email isn't registered
  
  * enter_register_data page -> login page
    ![registerlog](https://github.com/Pammy737/The_Blog/blob/main/readme_screenshots/register(nonuser).png)

## How to use
**Visitor**

As a visitor, you may:
* check all the blog posts and comments
* register as a blog member

**Blog Member**

As a blog member, you may:
* check all the blog posts and comments
* log in to your account
  * leave comments on posts

**Admin**

As an admin, you may:
* check all the blog posts and comments
* log in to your account
  * leave comments on posts
  * create, edit, and delete all the blog posts

## Techniques & Tools
* Frontend: starting code based on [blog-project](https://github.com/angelabauer/Flask-Blog-Project) and the theme [clean_blog](https://startbootstrap.com/theme/clean-blog)
 
* Backend: Python, Flask, SQLAlchemy, SQLite 
  * Python 3.9
   * Flask
     * flask-login (session..)
     * flask-ckeditor
     * flask-Bootstrap
     * flask-WTF / WTforms
     * flask-gravatar
* Database
    * SQLAlchemy
    * SQLite
* Test
    * pytest
    * Selenium


* Function
  * login
    * hashed & salted password
    * requires to enter_register_data if not yet a user
  * admin (the first user registered)
    * create / edit / delete posts
    * decorator
  * user 
    * required to login for specific pages
    * can only view posts 
    * able to leave comments with a gravatar created for the user


## Upcoming Features
 * password
   * change password / forgot password function
 * admin 
   * create a table for admins in database, allow users to apply for admin
 * tests
   * CI (Github actions / Travis CI)


## Notes

* ```next``` parameter
  * ex - about page
  
  * default function in [login_required](https://flask-login.readthedocs.io/en/latest/_modules/flask_login/utils/#login_required) -> login_url function
    
    *  would not work after submitting login form 
        
        * Reason - lost of ```next``` parameter when submitting login form
        
        * Solution - send the next parameter again when logging in
          1. retrieve next parameter -> redirect
        
              ```next=request.args.get("next") ``` 
              
              ```redirect(next)```
          2. Hidden Field in WTform + default value + retrieve -> redirect
              * Hidden Field in login form 
                 
                 ``` next=HiddenField("Next")```
              * set the next parameter as default value of login form
                
                  ```form = LoginForm(request.values, next=request.args.get("next"))```
              * retrieve the parameter -> redirect
                
                  ```next= form.next.data```

                  ``` redirect(next)```
  * without [login_required](https://flask-login.readthedocs.io/en/latest/_modules/flask_login/utils/#login_required)
    *  Solution - send next parameter through routes, check [show_post function](https://github.com/Pammy737/The_Blog/blob/main/main.py)


    
