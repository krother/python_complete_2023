
# HTTP Requests with authentication

In this folder you find code to start an HTTP server, and a Python client that authenticates itself with a password to generate a JWT bearer token.
The token is used for further requests.

## 1. Create a SSL secret key:

Run: 

    openssl rand -hex 32

You should see a hash key similar to:

    b2aded50e12ee627a42a74edbaa3eaf4c911c9737c3572d9ce31c8cf9affae64

The key will be used to sign the JWT token. The key itself stays on the server.

## 2. Insert the key to app.py

Set `SECRET_KEY` in `server/app.py`

## 4. Install requirements

Run:

    python -m pip install -r server/requirements.txt


## 5. Run the server

with: 

    uvicorn app:app

## 6. Visit the server page

Go to the Swagger page at `http://localhost:8000/docs`

You can manually authenticate with username `johndoe` and password `secret`.
(A hashed password is stored in `app.py`).

## 7. Set an environment variable

Configure the environment variable `API_PASSWORD` to contain the value `secret`
- on Windows in environment settings, on Unix in your `.bashrc` file with:

    export API_PASSWORD=secret

Continue from a new terminal session after this step.

## 8. Run the client

Also install Python requirements in the `client/` folder.

Then run requests against the site with:

    python send_auth.py localhost:8000

## 9. Run with Docker

Easy. Go to the main folder and type:

    docker-compose build
    docker-compose run

## Source:

Part of the code for this recipe was taken from [https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)