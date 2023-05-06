# **TRIVIA QUIZ**


You can find the site [here](LÄÄÄÄÄÄÄÄÄÄÄÄNK).

## **Features**

### **Existing features**

### **Future features**

Expansion of the game:
- Add levels to each quiz - easy, medium, hard

## **Testing**

### **Validator testing**

### **Resolved problems**

### **Bugs**


No other bugs have been idenitified in the deployed version.

## **Deployment**
You can find the link to the live site [here](LÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄNK).

The site was deployed to Heroku with the following steps:

1. Log in to GitHub
2. Find the right repository and open it with Gitpod.
3. Make sure you have removed any unused imported packages from your python code file and that you have uninstalled the packages. 
4. Make sure you have added \n to the end of all input()-methods in your code (otherwise the text will not show up in the terminal). For example data = input("Please enter data here:\n")
5. Create a new file named "requirements.txt". In the file, create a list of all the dependencies that the project needs to run, so that they will be installed by Heroku. Create the list by typing 'pip3 freeze > requirements.txt', in the terminal and press enter. This updates the file with all the dependencies.  
6. Make sure you save all changes made in previous steps and commit and push to GitHub.
7. Log in to your Heroku account at their website. From your Heroku dashboard, create a new app by clicking the "New"-button on the right hand side and select the "Create new app"-option. If it´s the first time you create an app, there will be a "Create new add"-button in the middle of the page instead.




5. In the app you created, you need to create an environment variable, called Config Var in Heroku. This is done under the "Settings"-tab in the top menu. Click the tab. On the settings page scroll down to the Config Vars-section and click the "Reveal Config Vars"-button.
6. In the input field "KEY", type in "PORT" to name the Config Var. In the input field "VALUES" type in "8000". Then click the "Add"-button. NÅGOT MEEEEEEEEER?
7. Scroll down to the "Buildpacks"-section and add two buildpacks by clicking the "Add buildpack"-button First select Python and click "Add". Then click the "Add buildpack"-button again, select nodejs and click "Add".
8. Now scroll back up to the top menu and select the "Deploy"-tab. Scroll to the methods-section and select GitHub by clicking on that  Om du inte redan har beräkftat flr Heroku att du vill koppla til Github, kilcka på Connetct to Github. Sen, i sektionen Connect to Github - sök efter namnet på ditt Github repositry i sökrutan. Klicka på Connect-button som dyker upp när Heroku har hittat ditt repositry. 
9. Sroll further down and choose either to deploy automatically by clicking the "Enable Automatic Deploys" or deploy manually by clicking the "Deploy Branch"-button. When de deployment is finished you can click the "View"-button to view the game. 



## **Credits**
I used [this Code Insitute lesson example](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/c92755338ef548f28cc31a7c3d5bfb46/?child=first) to figure out how to build the try/except-statement in the 'validate_username()'-function. I also used this [geeksforgeeks page](https://www.geeksforgeeks.org/password-validation-in-python/) to figure out how to return to the 'get_username'-function if invalid username was entered.

I used [the Love Sandwiches project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/c92755338ef548f28cc31a7c3d5bfb46/?child=first) to figure out what to start with to build the game. 

[This geeksforgeeks.org page](https://www.geeksforgeeks.org/python-string-isspace-method/) was used to help me figure out how to check for blank spaces in the username, i.e. by using the isspace()-method and iterate through the username put into the 'validate_username'-function. 

In the 'validate_choice'-function, I wanted the message informing the player of invalid input to be clean and nice. Instead of showing the 'valid_options'-list in the terminal when printing the message, for example '["s", "m", "g", "v"]', I wanted it to look like this ''s', 'm', 'g', or 'v''. In order to do this I used code from [this geeksforgeeks.org page](https://www.geeksforgeeks.org/python-add-phrase-in-middle-of-string/) to be able to insert an 'or'-string into the list before printing the message. It was done by re-designing the list in three steps: (1) splitting it, (2) adding "or" to the second to last position and (3) putting it back together again. After this I also needed to remove the '[]' around the list and ',' between the options. To understand how to do this I used [this blog post](https://blog.finxter.com/how-to-print-a-list-without-brackets-and-commas-in-python/) to learn more about the 'replace'-method for strings and how to use it to make a list look cleaner when printed.

I used [this askpython.com page](https://www.askpython.com/python-modules/tabulate-tables-in-python) and [this pypi.org page](https://pypi.org/project/tabulate/) to learn how to create simple tables with the tabulate package which resulted in this line of code to make the table look good: 'table = tb(scores_as_list, headers='firstrow')'. 

Code on line 167-172 is taken from [this stackabuse.com page](https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/). The code is used to loop through a dictionary of scores in the 'score_boards' list of dictionarys. The code has been adjusted to fit my program by changing variable names.

The code on line 36 to clear the screen/user window is taken from [this Stackoverflow page](https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python).

[This](https://sports-hangman.herokuapp.com/) peer portfolio project inspired me to have different catagories of questions (i.e. different games).

The following external python libraries were used in this project:
- [tabulate](https://pypi.org/project/tabulate/)
- [colorama](https://pypi.org/project/colorama/)

The quiz-questions were taken from these websites:
- science quiz: [Radiotimes.com](https://www.radiotimes.com/quizzes/pub-quiz-science/), [Greatwolf.com](https://www.greatwolf.com/blog/science-trivia-questions/), [Icebreakerideas.com](https://icebreakerideas.com/science-trivia/), [Triviawhizz.com](https://triviawhizz.com/trivia-questions/space), [Quiztriviagames.com](https://www.quiztriviagames.com/human-body-quiz/), [Usefultrivia.com](https://www.usefultrivia.com/science_trivia/animal_trivia_index.html)
- movie quiz: [Buzzfeed.com](https://www.buzzfeed.com/kellyrissman/movie-trivia-questions), [rd.com](https://www.rd.com/article/movie-trivia-facts/) 
- geography quiz: [Usefultrivia.com](https://www.usefultrivia.com/geography_trivia/)

## **Acknowledgements**
I would like to thank my mentor Antonio Rodriguez for guiding me when building this site, for example helping me with how to refactor repetative code and how to clear the screen/user window and delay the program at specific points in the game. 