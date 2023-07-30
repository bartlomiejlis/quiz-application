import time
import random

# Define a list of questions and answers
questions = [
    {"question": "What is the capital of France?", "answer": "Paris", "options": ["Paris", "London", "Berlin", "Rome"]},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter", "options": ["Jupiter", "Saturn", "Uranus", "Neptune"]},
    {"question": "Who directed the movie 'The Shawshank Redemption'?", "answer": "Frank Darabont", "options": ["Frank Darabont", "Martin Scorsese", "Quentin Tarantino", "Steven Spielberg"]},
    {"question": "In 1768, Captain James Cook set out to explore which ocean?", "answer": "Pacific Ocean", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"]},
    {"question": "What is the speed of sound?", "answer": "1,200 km/h", "options": ["120 km/h", "1,200 km/h", "400 km/h", "700 km/h"]},
    {"question": "Which did Viking people use as money?", "answer": "Jewellery", "options": ["Rune stones", "Jewellery", "Seal skins", "Wool"]},
    {"question": "What was the first country to use tanks in combat during World War I?", "answer": "Britain", "options": ["France", "Japan", "Britain", "Germany"]},
    {"question": "What is the main component of the sun?", "answer": "Gas", "options": ["Liquid lava", "Gas", "Molten iron", "Rock"]},
    {"question": "Goulash is a type of beef soup in which country?", "answer": "Hungary", "options": ["Hungary", "Czech Republic", "Slovakia", "Ireland"]},
    {"question": "Which two months are named after Emperors of the Roman Empire?", "answer": "July and August", "options": ["January and February", "March and April", "May and June", "July and August"]},
    {"question": "What is the most points that a player can score with a single throw in darts?", "answer": "60", "options": ["20", "40", "60", "80"]},
    {"question": "The two biggest exporters of beers in Europe are Germany and …", "answer": "Belgium", "options": ["Spain", "France", "Italy", "Belgium"]},
    {"question": "The phrase: ”I think, therefore I am” was coined by which philosopher?", "answer": "Descartes", "options": ["Socrates", "Plato", "Aristotle", "Descartes"]},
    {"question": "In the series “Game of Thrones”, Winterfell is the ancestral home of which family?", "answer": "The Starks", "options": ["The Lannisters", "The Starks", "The Tully’s", "The Targaryens"]},
    {"question": "Who is known as the Patron Saint of Spain?", "answer": "St James", "options": ["St Patrick", "St Benedict", "St James", "St John"]},
    {"question": "What does the term “SOS” commonly stand for?", "answer": "Save Our Souls", "options": ["Save Our Sheep", "Save Our Ship", "Save Our Seal", "Save Our Souls"]},
    {"question": "Which company is known for publishing the Mario video game?", "answer": "Nintendo", "options": ["Xbox", "Nintendo", "SEGA", "Electronic Arts"]},
    {"question": "Which was the first film by Disney to be produced in colour?", "answer": "Snow White and the Seven Dwarfs", "options": ["Toy Story", "Sleeping Beauty", "Snow White and the Seven Dwarfs", "Cinderella"]},
    {"question": "What is the name of the first book of the Old Testament in the Bible?", "answer": "Genesis", "options": ["Exodus", "Genesis", "Proverbs", "Matthew"]},
    {"question": "Neil Armstrong was the first astronaut in the world to step foot on the moon. Who was the second?", "answer": "Buzz Aldrin", "options": ["Yuri Gagarin", "James Irwin", "Alan Bean", "Buzz Aldrin"]},
    {"question": "How many time zones are there in total in the world?", "answer": "24", "options": ["8", "16", "24", "32"]},
    {"question": "Cu is the chemical symbol for which element?", "answer": "Copper", "options": ["Oxygen", "Copper", "Zinc", "Helium"]},
    {"question": "What is the largest active volcano in the world?", "answer": "Mouna Loa", "options": ["Mount Etna", "Mount Vesuvius", "Mouna Loa", "Mount Batur"]},
    {"question": "In the Big Bang Theory, what is the name of Sheldon and Leonard’s neighbour?", "answer": "Penny", "options": ["Penny", "Patty", "Lily", "Jessie"]},
    {"question": "What is the largest continent in size?", "answer": "Asia", "options": ["Asia", "Africa", "Europe", "North America"]},
    {"question": "Which French king was nicknamed the “Sun King”?", "answer": "Louis XIV", "options": ["Louis XVI", "Charlemagne", "Francis I", "Louis XIV"]},
    {"question": "Which famous inventor invented the telephone?", "answer": "Alexander Graham Bell", "options": ["Thomas Edison", "Benjamin Franklin", "Alexander Graham Bell", "Nikola Tesla"]},
    {"question": "How many wives had Henry VIII?", "answer": "6", "options": ["1", "3", "4", "6"]},
    {"question": "What does the Richter scale measure?", "answer": "Earthquake intensity", "options": ["Wind Speed", "Temperature", "Tornado Strength", "Earthquake intensity"]},
    {"question": "How many sides has a Hexagon?", "answer": "6", "options": ["5", "6", "7", "8"]},
    {"question": "When were Guy Fawkes and The Gunpowder Plot discovered?", "answer": "1605", "options": ["1505", "1605", "1705", "1805"]},
    {"question": "If you are eating chicken jalfrezi, what type of food are you eating?", "answer": "Indian Food", "options": ["French food", "Italian food", "Indian Food", "Mexican Food"]},
    {"question": "What is the capital of Iraq?", "answer": "Baghdad", "options": ["Baghdad", "Islamabad", "Tehran", "Amman"]},
    {"question": "Which country won the first Football World Cup in 1930?", "answer": "Uruguay", "options": ["Brazil", "Portugal", "Italy", "Uruguay"]},
    {"question": "In which country is the baht the currency?", "answer": "Thailand", "options": ["Vietnam", "Malaysia", "Indonesia", "Thailand"]},
    {"question": "“Onze” is the french number for?", "answer": "11", "options": ["3", "8", "9", "11"]},
    {"question": "What does NASA stand for?", "answer": "National Aeronautics and Space Administration", "options": ["National Aeronautics and Space Administration", "Nautical And Space Association", "National Aeronautics and Space Association", "New Aeronautics and Spacial Administration"]},
    {"question": "What is Marshall’s job in How I met your mother?", "answer": "Lawyer", "options": ["Architect", "Lawyer", "Teacher", "Journalist"]},
    {"question": "What is the capital of New Zealand?", "answer": "Wellington", "options": ["Christchurch", "Wellington", "Auckland", "Dunedin"]},
    {"question": "Apart from water, what is the most popular drink in the world?", "answer": "Tea", "options": ["Tea", "Coffee", "Beer", "Orange Juice"]},
    {"question": "In The Lion King, who is Simba’s uncle?", "answer": "Scar", "options": ["Mufasa", "Scar", "Timon", "Zazu"]},
    {"question": "How many bones are there in an adult human body?", "answer": "206", "options": ["186", "206", "286", "306"]},
    {"question": "Mallorca is part of which archipelago?", "answer": "Balearic Islands", "options": ["Balearic Islands", "Canary Islands", "Whitsunday Islands", "Galapagos Islands"]},
    {"question": "In Home Alone, where were the McCallister flying to when they left Kevin?", "answer": "France", "options": ["England", "Florida", "France", "Mexico"]},
    {"question": "Who lives at the following address ‘10 Downing Street’?", "answer": "UK Prime Minister", "options": ["US President", "French President", "UK Prime Minister", "Scotland First Minister"]},
    {"question": "What’s Garfield favourite food?", "answer": "Lasagna", "options": ["Pizza", "Lasagna", "Burger", "Sandwich"]},
    {"question": "How high is Mount Everest?", "answer": "8,849 m", "options": ["5,849 m", "6,849 m", "7,849 m", "8,849 m"]},
    {"question": "Which chemical element has Ag as a symbol?", "answer": "Silver", "options": ["Gold", "Silver", "Iron", "Carbon"]},
    {"question": "What is the largest ocean in the world?", "answer": "Pacific Ocean", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"]},
    {"question": "Who painted the famous artwork 'The Starry Night'?", "answer": "Vincent van Gogh", "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Rembrandt"]}
]

# shuffle the questions list
random.shuffle(questions)

# Initialize the score
score = 0

# Time per question
time_per_question = 20 # in seconds

# Print a brief description of the quiz
print("Welcome to the quiz!")
print("You will be presented with a set of 50 multiple choice questions.")
print(f"You have {time_per_question} seconds to answer each question.")
print("Enter the number of the correct answer and press enter.")
input("Press enter to begin the quiz")
print()

# Iterate through the questions
for question in questions:
    # shuffle the options list
    random.shuffle(question["options"])
    # Start the timer for the current question
    start_time = time.time()
    # Ask the question
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter the number of the correct answer: ")
    # Check if the time is up
    if time.time() - start_time > time_per_question:
        print("Time's up!")
        print()
    # Check if the answer is correct
    elif question["options"][int(user_answer)-1].lower() == question["answer"].lower():
        print("Correct!")
        score += 1
        print()
    else:
        print("Incorrect. The correct answer is", question["answer"])
        print()

# Print the final score
print("You scored", score, "out of", len(questions))