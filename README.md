# MovieApp

MovieApp is a Python-based movie management application that allows users to store, update, delete, and list movies from their local storage (CSV or JSON format). 
The app also integrates with the OMDb API to fetch movie details such as ratings, posters, and IMDb URLs.

## Features

	•	Add Movies: Add new movies to the database and retrieve movie details from OMDb API.
	•	List Movies: Display all movies in the local storage.
	•	Delete Movies: Remove movies from the database.
	•	Update Movie Notes: Update notes for specific movies.
	•	Movie Statistics: View average, median, best, and worst movie ratings.
	•	Generate Website: Create an HTML website showcasing all your movies.
	•	Random Movie Selector: Randomly selects a movie for you to watch.
	•	Storage Options: Supports JSON and CSV storage formats.

## Installation

To install this project, simply clone the repository,
and install the dependencies in `requirements.txt` using `pip`

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- Git 

## Steps

1. **Clone the Repository**

   Open the Terminal and run:
    ```bash 
    git clone https://github.com/SangamithraMB/MovieApp.git

2. Install Dependencies
   ```bash
   pip install -r requirements.txt

3. Set up your .env file:
Create a .env file in the root directory with your OMDb API key:
   ```bash
   OMDB_API_KEY=your_api_key_here

### Usage
To use this project:

1.	Run the MovieApp:
You can start the MovieApp with either a CSV or JSON file as the storage medium.
      ```bash
      python3 main.py movies.json   # For JSON storage
      python3 main.py movies.csv    # For CSV storage

2. Command-line menu:
Once the app is running, you’ll be presented with a menu:
   ********** My Movies Database **********

Menu:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Generate website

Enter the corresponding number to perform an action.

### Example Commands

	•	Add Movie: When you choose the “Add movie” option, the app will ask you for a movie title and automatically fetch details from the OMDb API.
	•	Generate Website: This option will create an index.html file that lists all your movies in a grid format with posters, ratings, and IMDb links.

### Dependencies

	•	Python 3.x
	•	requests - for interacting with the OMDb API
	•	python-dotenv - for environment variable management
	•	pandas - for CSV manipulation
	•	argparse - for command-line argument parsing

### How to Contribute

	1.	Fork the repository.
	2.	Create your feature branch: git checkout -b feature/my-new-feature
	3.	Commit your changes: git commit -m 'Add some feature'
	4.	Push to the branch: git push origin feature/my-new-feature
	5.	Submit a pull request.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

	•	OMDb API for providing movie information.
	•	Python community for awesome libraries like requests, pandas, and argparse.

This is a basic structure for the README.md. 
You can modify the content to match the specifics of your project and personal preferences.