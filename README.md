<h1  align="center">SQL Alchemy Challenge</h1>
<a name="readme-top"></a>


<!-- TABLE OF CONTENTS -->



Table of Contents
<ol>
<li><a href="#about-the-project">About The Project</a></li>
<li><a href="#built">Build With FLASK, PYTHON, SQLITE, and SQLALCHEMY Framework</a></li>
<li><a href="#contributing">Contributing (UC Berkeley Bootcamp Students Only) </a></li>
<li><a href="#contact">Contact</a></li>
<li><a href="#acknowledgments">Acknowledgments</a></li>
</ol>


<!-- ABOUT THE PROJECT -->

## About The Project

### Instructions

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

## Part 1: Analyze and Explore the Climate Data

1. Note that you’ll use the provided files (`climate_starter.ipynb` and `hawaii.sqlite`)` to complete your climate analysis and data exploration.
2. Use the SQLAlchemy `create_engine()` function to connect to your SQLite database.
3. Use the SQLAlchemy `automap_base()` function to reflect your tables into classes, and then save references to the classes named `station` and `measurement`.
4. Link Python to the database by creating a SQLAlchemy session.
5. Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

### Precipitation Analysis

1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame. Explicitly set the column names.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame `plot` method, as the following image shows:
   <img width="426" alt="image" src="https://github.com/user-attachments/assets/9a885b0d-b9e8-44aa-b38f-58032dcd1e59">

8. Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

1. Design a query to calculate the total number of stations in the dataset
2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
   - List the stations and observation counts in descending order.
3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
4. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps: 
   - Filter by the station that has the greatest number of observations.
   - Query the previous 12 months of TOBS data for that station.
   - Plot the results as a histogram with `bins=12`, as the following image shows:


<img width="407" alt="image" src="https://github.com/user-attachments/assets/9b815ec1-ebc6-43bc-8caf-d04d5d62a68b">

5. Close your session.

## Part 2: Design Your Climate App

Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:

1. `/`

- Start at the homepage.

- List all the available routes.

<img width="571" alt="image" src="https://github.com/user-attachments/assets/f445945b-bdda-4d33-8355-6984ba446e6c">


2. `/api/v1.0/precipitation`

- Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

- Return the JSON representation of your dictionary.

<img width="391" alt="image" src="https://github.com/user-attachments/assets/8d7ef6aa-2a3d-44c8-a923-39abbdec1b77">


3. `/api/v1.0/stations`

- Return a JSON list of stations from the dataset.

<img width="391" alt="image" src="https://github.com/user-attachments/assets/399eb16a-6858-454c-97f1-b4007a90f516">


4. `/api/v1.0/tobs`

- Query the dates and temperature observations of the most-active station for the previous year of data.

- Return a JSON list of temperature observations for the previous year.

<img width="343" alt="image" src="https://github.com/user-attachments/assets/280b5e48-c8d2-4c26-9be9-dfb3e1d2b0dd">


5. `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

- Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

- For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

- For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

<img width="352" alt="image" src="https://github.com/user-attachments/assets/30b865fd-c6ad-49b2-ab47-54df55a88050">


<img width="407" alt="image" src="https://github.com/user-attachments/assets/d4e7be2a-2263-49f5-8953-8db980cbc99b">

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>
  
<!-- BUILT -->

## Built with FLASK, PYTHON, SQLITE, and SQLALCHEMY Framework 

- Flask: A lightweight Python web framework that simplifies building web applications.
Provides tools for handling routes, requests, responses, and templating.

- SQLite: A self-contained, embedded database engine.
Stores data in a single file, making it ideal for smaller projects and development environments.
Included in the Python standard library, so no additional installation is required.

- SQLAlchemy: An Object Relational Mapper (ORM) for Python.
Allows you to interact with databases using Python objects instead of raw SQL queries. Provides a layer of abstraction that simplifies database interactions and reduces boilerplate code.

- Application: Leverages Flask to create a web application.
Utilizes SQLite as the database engine to store measurement data.
Employs SQLAlchemy to interact with the SQLite database and translate between Python objects and database tables.
This combination of technologies enables you to develop a web application that can manage and retrieve measurement data efficiently.

  
  <p  align="right">(<a  href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->

## Contributing 

(UC Berkeley Bootcamp Students Only)  

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

  

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project

2. Create your Feature Branch (`git checkout -b new-branch-name`)

3. Commit your Changes (`git commit -m 'Add some message'`)

4. Push to the Branch (`git push origin new-branch-name`)

5. Create a pull request. 

Forking a repository and creating a pull request on GitHub is a great way to contribute to open-source projects. Here's a breakdown of the process:

1. Forking the Repository:

Find the repository you want to contribute to on GitHub.
Click on the "Fork" button in the top right corner. This creates a copy of the repository in your own account.

2. Clone the Forked Repository to Your Local Machine

You'll need Git installed on your system.
Use Git commands to clone your forked repository to your local machine. There will be instructions on the GitHub repository page for cloning.

3. Making Changes (Local Work):

Make your changes to the code in your local copy.
Use Git commands to track your changes (adding, committing).

4. Pushing Changes to Your Fork:

Once you're happy with your changes, use Git commands to push your local commits to your forked repository on GitHub.

5. Creating a Pull Request:

Go to your forked repository on GitHub.
Click the "Compare & pull request" button (might appear as a yellow banner).
Here, you'll see a comparison between your changes and the original repository.
Write a clear title and description for your pull request explaining the changes you made.
Click "Create Pull Request" to submit it for review.

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under  GNU General Public License. See `LICENSE.txt` for more information.

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Thay Chansy - [@thaychansy](https://twitter.com/thaychansy) - or thay.chansy@gmail.com


Please visit my Portfolio Page: thaychansy.github.io (https://thaychansy.github.io/)



Project Link: [thaychansy/sqlalchemy-challenge (github.com)](https://github.com/thaychansy/sqlalchemy-challenge)
  

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>

   
  

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments


Here's a list of resources we found helpful and would like to give credit to. 

  
* [Chat GPT] [ChatGPT](https://chatgpt.com/)
* [Google Gemini] [Gemini Generative AI](https://gemini.google.com/app)
  

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>

