# RESTful API Project

## 0. Basics of HTTP/HTTPS

### Objectives:
- Differentiate between HTTP and HTTPS.
- Understand the basic structure of HTTP requests and responses.
- Identify and explain common HTTP methods and status codes.

### Instructions:
1. **Differentiating HTTP and HTTPS**:
   - Read the provided resources to understand the differences between HTTP and HTTPS.
   - Note the key differences, focusing on security aspects.

2. **Understanding HTTP request structure**:
   - Visit a simple website and inspect the requests in the “Network” tab of the inspector.
   - Explore the requests and responses to understand the structure (methods, paths, status codes, headers).

3. **Explore HTTP methods and status codes**:
   - Make a list of 4 common HTTP methods and explain their usage.
   - List 5 common HTTP status codes, providing a brief description and an example scenario for each.

### Resources:
- [MDN - Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [MDN - List of HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [MDN - Difference between HTTP and HTTPS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#http_and_https)

---

## 1. Consuming data from an API with curl

### Objectives:
- Install and use curl to interact with RESTful APIs.
- Construct and execute basic API requests using curl.
- Interpret the results of common API requests.

### Instructions:
1. **Install curl**:
   - Install curl on your system (available in standard repositories for Linux/Mac, or download for Windows).
   - Confirm the installation with `curl --version`.

2. **Use curl to interact with an API**:
   - Use curl to retrieve posts from JSONPlaceholder: `curl https://jsonplaceholder.typicode.com/posts`.

3. **Use headers and other curl options**:
   - Retrieve only the headers with: `curl -I https://jsonplaceholder.typicode.com/posts`.
   - Make a POST request with: `curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts`.

### Resources:
- [Everything curl](https://everything.curl.dev/)
- [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)

---

## 2. Consuming and processing data from an API with Python

### Objectives:
- Use the `requests` library to send HTTP requests.
- Parse and manipulate JSON data with Python.
- Convert structured data into other formats (e.g., CSV).

### Instructions:
1. **Install the `requests` library**:
   - Install `requests` using `pip install requests`.

2. **Retrieve and display posts**:
   - Create a function to fetch and display the titles of posts from JSONPlaceholder.

3. **Save posts to a CSV file**:
   - Create a function to fetch posts and save them to a CSV file.

### Resources:
- [Python Requests](https://docs.python-requests.org/en/master/)
- [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)

---

## 3. Develop a simple API with `http.server`

### Objectives:
- Set up a basic HTTP server using the `http.server` module.
- Handle different types of HTTP requests.
- Serve JSON data in response to specific endpoints.

### Instructions:
1. **Set up a simple HTTP server**:
   - Create a subclass of `http.server.BaseHTTPRequestHandler`.
   - Implement the `do_GET` method to return a simple response.

2. **Serve JSON data**:
   - Modify `do_GET` to return a JSON data set for the `/data` endpoint.

3. **Handle multiple endpoints**:
   - Add a `/status` endpoint to check the API status (returns "OK").
   - Implement error handling for undefined endpoints (returns 404 error).

### Resources:
- [Python docs: http.server](https://docs.python.org/3/library/http.server.html)

---

## 4. Develop a simple API with Flask

### Objectives:
- Set up a Flask application.
- Define and manage routes in Flask to handle different endpoints.
- Serve JSON data with Flask.
- Handle POST requests to add new data to the API.

### Instructions:
1. **Set up Flask**:
   - Install Flask: `pip install Flask`.
   - Create a Flask application and define a root endpoint that returns "Welcome to the Flask API!".

2. **Serve JSON data**:
   - Create a `/data` endpoint that returns a list of users in JSON format.

3. **Handle POST requests**:
   - Create a `/add_user` endpoint that accepts POST requests to add a new user.

### Resources:
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)

---

## 5. Securing the API and Authentication

### Objectives:
- Understand the importance of API security.
- Implement basic authentication with Flask.
- Set up token-based authentication using JSON Web Tokens (JWT).

### Instructions:
1. **Basic Authentication**:
   - Use `Flask-HTTPAuth` to configure basic authentication.

2. **JWT Authentication**:
   - Use `Flask-JWT-Extended` to add JWT authentication.
   - Create a `/login` endpoint that generates a JWT token upon successful login with valid credentials.

### Resources:
- [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)

---

## GitHub Repository:
Create a GitHub repository with the following files and structure:
