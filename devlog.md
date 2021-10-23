# Devlog so I dont forget what i've done

## Creating sugnup form

### Template

- Created a new app for all our authentication
- Used django's default views and user model to handle user authentication
- Create template which inherits from our base which displays the login screen
  - You'll note the `csrf_token`. THis is just for securty
  - In the template, we use `{{ form.as_p }}` which renders our form as a
    paragraph tags
- Specifying a `LOGIN_REDIRECT_URL = '/'` to redirect to after login

## View

- Created a custom form inheriting from the main django user form
- Created the login, logut and signup views

## todo

- create custom user model with name and surname
- Fix form presentation using crispy. Perhaps iterate over
