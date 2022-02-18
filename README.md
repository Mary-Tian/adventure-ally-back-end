Adventure Ally

Introduction:

Have you ever had analysis paralysis from trying to keep track of many different options? Or had fear of missing out because you weren’t sure if you reviewed all of the best options? Adventure Ally aims to solve that with a way for users to easily find AND track activities when going on vacation, deciding on a joint activity with friends, etc.

In this iteration of the webapp, users have the ability to log in to their own individual pages, where they are able to see the activities they selected. With this login, they can choose to login with email and password, or Google OAuth.

Once logged in, users have the ability to input a location or destination. On the backend, this section makes an external call to the Yelp API, which returns a list of all of the activities for the inputted locatiomn, as well as the name of the activity, a corresponding image, the price point and the Yelp rating that activity has received.

Once we have a list of our favorite activities, we are able to notate how much we would enjoy that activity with our number of likes.

Finally, when we are ready for our next adventure, we can simply adjust our destination, and the app is now ready for us to plan our next great adventure.

Installation

Clone both the frontend and backend repositories.

Frontend Install dependencies by running npm install or yarn install. Create a .env file with environment variable: REACT_APP_BACKEND_URL=whatever_your_backend_url_will_be. To start up the frontend, run yarn start (or npm). You will need your own Yelp Fusion API key in order to call the Yelp API to generate adventures by location: In order to set up your access to Yelp Fusion API, you need to create an app with Yelp. This app represents the application you'll build using our API and includes the credentials you'll need to gain access. Here are the steps for creating an app: Go to Create App In the create new app form, enter information about your app, then agree to Yelp API Terms of Use and Display Requirements. Then click the Submit button. You will now have an API Key. Please keep the API Key to yourself since it is the credential for your call to Yelp's API.

Backend Set up a virtual environment: python3 -m venv venv and source venv/bin/activate. Install the requirements: pip install -r requirements.txt. Create a local PostgreSQL database for the project, you can call this database something like adventure_ally. Create a .env file and add environment variable SQLALCHEMY_DATABASE_URI to hold the path to this database. For example: SQLALCHEMY_DATABASE_URI=here put the path to the database you created on your local machine. Run flask db init and flask db migrate. Run the backend server with flask run.
