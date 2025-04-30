27th April 2025
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ mkdir app/errors/
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/errors/__init__.py
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/errors/__init__.py && git commit -m "E
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/__init__.py 
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/__init__.py && git commit -m "Register
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/errors/handlers.py
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/errors/handlers.py && git commit -m "E

(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ mkdir app/auth/
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/auth/__init__.py
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/auth/__init__.py && git commit -m "Auth Module:  Initialization" && git push
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/__init__.py 
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/__init__.py && git commit -m "Auth Blueprint: Register the authentication blueprint with the application." && git push
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/auth/routes.py
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/auth/routes.py && git commit -m "Appli
cation routes: Auth routes" && git push
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/auth/forms.py
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/auth/forms.py && git commit -m "Applicaiton Forms: Auth Forms" && git push
vim app/auth/email.py
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/auth/email.py && git commit -m "Reset_Password: Function" && git push

(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/main/routes.py 
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/main/routes.py && git commit -m "Main Routes: Index, Explore, Username, Edit profile, Follow, Unfollow, Translate" && git push
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/main/forms.py
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/main/forms.py && git commit -m "Forms: Post, Empty and EditProfile Forms" && git push

Installations done in Virtual environment as below
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $  pip install flask-wtf
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ pip install flask-sqlalchemy
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ pip install flask-migrate
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ pip install flask-login
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $  pip install email-validator
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ export FLASK_DEBUG=1
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ pip install flask-mail
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ pip install pyjwt
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ pip install flask-moment
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ pip install flask-babel
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $  pip install langdetect
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $  pip install requests
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $  pip install elasticsearch
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $  pip install rq
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ pip install httpie  # for testing API route
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ pip install flask-httpauth  # simplify the interactions between client and server when token authentication is used.

(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ mkdir app/templates/
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ mkdir app/templates/auth/
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/templates/auth/register.html
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/templates/auth/register.html && git commit -m "Auth Registration Templates: Register.html" && git push
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/templates/auth/login.html
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/templates/auth/login.html && git commit -m "Auth Login Template: Login.html" && git push
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/templates/auth/reset_password.html
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/templates/auth/reset_password.html && git commit -m "Auth Reset Password.html " && git push
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/templates/auth/reset_password_request.html
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/templates/auth/reset_password_request.
html && git commit -m "Auth Reset Password Request template: reset_password_request.html" && git push

(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ mkdir app/templates/email/
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/templates/email/reset_password.html
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/templates/email/reset_password.html && git commit -m "Reset Password mail: Link" && git push
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/templates/email/reset_password.txt
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/templates/email/reset_password.txt && git commit -m "Reset password: Text mail" && git push

(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ mkdir app/templates/errors/
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/templates/errors/404.html
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/templates/errors/404.html && git commit -m "Error: 404.html" && git push
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/templates/errors/500.html
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/templates/errors/500.html && git commit -m "ErrorT:500.html" && git push

(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/templates/bootstrap_wtf.html
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/templates/bootstrap_wtf.html && git commit -m "Bootstrap WTF" && git push
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/templates/base.html
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/templates/base.html && git commit -m "Base Template" && git push
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/templates/index.html
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/templates/index.html && git commit -m "Index Template" && git push
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/templates/edit_profile.html
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/templates/edit_profile.html && git commit -m "EditProfile Template" && git push
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/templates/user.html
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/templates/user.html && git commit -m "User Template" && git push
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim app/templates/_post.html
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/templates/_post.html && git commit -m "Subtemplate: _post.html" && git push

cli.py 
mail.py
models.py


28th April 2025
export MS_TRANSLATOR_KEY=7Zri4p0Mcfou6UtbQXHF1wUMWXo392DycmPSr7HWDhDWtLEyGWQpJQQJ99BDACrIdLPXJ3w3AAAbACOGJSe4   NB: Azure

.env and above key added

29th April 2025
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ vim .env    NB:other features added (Secret key):NOT TO BE COMMITED BECUASE OF KEYS

(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ pip install aiosmtpd
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:8025
NB: the 2 above to have dummy server to test email support
included python path to include the current directory SurveillanceBlog/ in .flaskenv commit
PYTHONPATH=. flask db init  #NB migration directory creation.
PYTHONPATH=. flask db migrate -m "Initial migration"  #NB generating migration script (for Users and Table)
PYTHONPATH=. flask db upgrade # NB to upgrade - to implement the creation of tables user and post
finally export PYTHONPATH=.  # reduce the manually inclusion whenever an action needs to be done.
 
30th April 2025
 pybabel extract -F babel.cfg -k _l -o messages.pot .  #NB: extracting all marked _() and _l() for translation
pybabel init -i messages.pot -d app/translations -l es # NB: creating translation into spanish (es)
 pybabel compile -d app/translations # NB: compiling the message.po to be ready for usage on application run.
git ocmmitted app/translations/
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ mkdir app/static/
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ touch app/static/.gitkeep
(S) @SUE2023 ➜ /workspaces/Beyond-Surveillance/SurveillanceBlog (Dev) $ git add app/static/.gitkeep && git commit -m " "Ad
ded static empty directory with .gitkeep" && git push

