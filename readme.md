Simple Note-Taking API

A RESTful API built with Django for a simple note-taking application. This application allows users to create, fetch, query, and update notes. No user authentication is required.

Features
Create Note: Create a new note with a title and body.
Fetch Note by ID: Retrieve a note using its primary key (ID).
Query Notes by Title Substring: Search for notes using a substring present in their title.
Update Note: Update the title and body of an existing note by ID.
(Optional)

Swagger Documentation: Integrated Swagger UI to easily test API endpoints.
Technologies Used
Python 3.x
Django 4.x
Django REST Framework
PostgreSQL
Setup Instructions
Follow these steps to set up the project on your local machine.

1. Clone the Repository
bash
Copy code
git clone https://github.com/sakshikasera/simple-note-api.git
cd simple-note-api
2. Set Up a Virtual Environment
Create and activate a virtual environment to manage project dependencies.

bash
Copy code
# For MacOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
Install all the required Python packages using pip.

bash
Copy code
pip install -r requirements.txt
4. Set Up the Database
By default, the project uses SQLite. To use PostgreSQL or any other database, update the DATABASES setting in settings.py.

For SQLite (default):

bash
Copy code
python manage.py migrate
For PostgreSQL: Update your DATABASES setting in settings.py:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<your-database-name>',
        'USER': '<your-database-user>',
        'PASSWORD': '<your-password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Then, run the migrations:

bash
Copy code
python manage.py migrate
5. Run the Development Server
Start the development server:

bash
Copy code
python manage.py runserver
The API will be available at http://127.0.0.1:8000/.

API Endpoints
HTTP Method	Endpoint	Description	Request Body
POST	/notes/	Create a new note	{ "title": "<string>", "body": "<string>" }
GET	/notes/<id>/	Fetch a note by its primary key (ID)	None
GET	/notes?title=<substring>	Query notes by title substring	None
PUT	/notes/<id>/	Update an existing note by ID	{ "title": "<string>", "body": "<string>" }
Example Requests
Create Note
bash
Copy code
POST /notes/

{
    "title": "Shopping List",
    "body": "Buy milk, eggs, and bread."
}
Fetch Note by ID
bash
Copy code
GET /notes/1/
Query Notes by Title Substring
bash
Copy code
GET /notes?title=Shop
Update Note
bash
Copy code
PUT /notes/1/

{
    "title": "Updated Shopping List",
    "body": "Buy milk, eggs, bread, and butter."
}
Running Tests
To run the test suite, use the following command:

bash
Copy code
python manage.py test
This will execute all integration tests written for the API endpoints.

Error Handling
The API uses proper HTTP status codes to indicate the result of operations:

201 Created: When a note is successfully created.
200 OK: When a note is successfully fetched or updated.
400 Bad Request: When the request payload is invalid.
404 Not Found: When a note with the specified ID does not exist.
Project Structure
bash
Copy code
.
├── notes/                # App for handling notes
│   ├── migrations/       # Django migration files
│   ├── models.py         # Note model definition
│   ├── serializers.py    # DRF serializers for the API
│   ├── tests.py          # Integration tests for the API
│   ├── urls.py           # URL routing for the notes app
│   └── views.py          # API views
├── project/              # Project-level settings
│   ├── settings.py       # Django settings, including database config
│   ├── urls.py           # Project-level URL routing
├── manage.py             # Django management script
├── requirements.txt      # Python package requirements
└── README.md             # Project documentation
