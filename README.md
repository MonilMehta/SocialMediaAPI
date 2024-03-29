<h1 align="center" id="title">Social Media API</h1>

<p align="center"><img src="https://socialify.git.ci/MonilMehta/SocialMediaAPI/image?description=1&amp;descriptionEditable=A%20backend%20Social%20Media%20API%20created%20using%20Django&amp;font=Raleway&amp;language=1&amp;name=1&amp;owner=1&amp;stargazers=1&amp;theme=Dark" alt="project-image"></p>

<p id="description">The Social Media Platform API is a Django-based RESTful API that provides functionality for users to register log in create posts like/unlike posts. It offers token-based authentication using Django Knox and allows users to interact with various features commonly found in social media platforms.</p>

<h2>Project Screenshots:</h2>
## Signup
<img src="./media/projectphotos/PO1.png" alt="project-screenshot" >
## Sign in
<img src="./media/projectphotos/PO2.png" alt="project-screenshot" >
##  Profile Updation
<img src="./media/projectphotos/PO3.png" alt="project-screenshot" >
##  View Profile
<img src="./media/projectphotos/PO4.png" alt="project-screenshot" >
##  Post Creation
<img src="./media/projectphotos/PO5.png" alt="project-screenshot" >
##  Like Functionality
<img src="./media/projectphotos/PO6.png" alt="project-screenshot" >
## Post Viewer
<img src="./media/projectphotos/PO7.png" alt="project-screenshot" >

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   ## User Authentication and Profile Management:
    User registration with username password and email. 
    User login to obtain authentication tokens. 
    User profile management with additional information such as profile picture bio and date of birth.
*   ## Post Creation and Retrieval 
    Authenticated users can create posts with images and captions. 
    Retrieval of posts including the author's information.
*   ## Like and Unlike Posts 
    Users can like and unlike posts. 
    Ensures that users can only like or unlike a post once.

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the Repository:</p>

```
git clone https://github.com/MonilMehta/SocialMediaAPI.git
```

<p>2. Navigate to Project Directory:</p>

```
cd SocialMediaAPI
```

<p>3. Install Dependencies:</p>

```
pip install -r requirements.txt
```

<p>4. Apply Migrations:</p>

```
python manage.py migrate
```

<p>5. Run the Development Server:</p>

```
python manage.py runserver
```
Access API Endpoints:

    User Registration: http://127.0.0.1:8000/api/signup/ (POST)
    User Login: http://127.0.0.1:8000/api/login/ (POST)
    Update User Profile: http://127.0.0.1:8000/api/profile/update/ (PUT)
    Create Post: http://127.0.0.1:8000/api/createpost/ (POST)
    Like Post: http://127.0.0.1:8000/api/like/ (POST)
    Unlike Post: http://127.0.0.1:8000/api/unlike/ (POST)

Interact with Endpoints:

    Use tools like Postman or cURL to interact with the API endpoints.
    For user registration, send a POST request to /api/signup/ with username, password, and email.
    For user login, send a POST request to /api/login/ with username and password to get the authentication token.
    Use the token in the header for authenticated endpoints.
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Django
*   DjangoRestFramework

<h2>💖Like my work? Star this repository</h2>