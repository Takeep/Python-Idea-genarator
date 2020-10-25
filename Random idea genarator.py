This will import the random module
import random

#These are the basic ideas, i put them in list, here are all the idea catgories. change them as you want:video games, coding projects, art ideas,  new coding lanugauges.
video_game_creation_ideas = ['pong', 'a game where you dont play the game', 'build a house', 'play a mouse', 'run', 'a game where u make a button fun to press', 'a game with 10 features', 'a game with 100 features', 'a game where you play blue trying to get rid of red', 'a game where u squash bugs', 'a game where your the bad guy', 'a game where you make your bed']
coding_projects_ideas = ['A phonebook', 'celluar automation', 'chat bot', 'pong', 'snake', 'platformer game only with c++', 'a fighting game only in pygame', 'sudoku solver', 'random idea genarator', 'a text to speech bot', 'a text adventure game in python', 'a dungeon crawler with pygame', 'random 2d terrain genarator', 'turtle racer']
art_ideas = ['draw manga', 'make a comic book', 'make a sculpatre', 'make a sculptre out of paper', 'try 3d modeling', 'make an animation', 'make a animation on paper', 'make a one line drawing', 'draw an avatar', 'animate with only paper and pencil', 'make a panting', 'make a wartercolor painting', 'try following along with a bob ross video']
new_coding_language = ['Python', 'c++', 'ruby', 'c#', 'c', 'java', 'javascript', 'phb', 'vscode', 'css', 'html', 'sql', 'obj c', 'swift', 'A.NET', 'action scirpt', 'A+', 'fortran', 'kolbolt', 'Assembly language', 'ABC', 'ABAP', 'A-0 SYSTEM', 'ABC ALGLO', 'ACC', 'Acent', 'Ace Dasl', 'Action', 'Actor', 'Ada', 'Adenie', 'Advlp', 'Agda', 'Adglint', 'Agora', 'AIMMS', 'Aldor', 'Basic', 'BCPL', 'B', 'Draco', 'F#', 'Game amker language', 'Go', 'Google app script', 'J++']

#Im defening the function that randomly picks the random video game idea
def random_video_game_creation_ideas():
    random_idea1 = random.choice(video_game_creation_ideas)

#This is printing the random idea
    print(random_idea1)


def random_coding_projects_ideas():
    random_project = random.choice(coding_projects_ideas)

# This is printing the random project
    print(random_project)

def random_art_ideas():
    random_art_project = random.choice(art_ideas)

    #This is printing the random art idea
    print(random_art_project)

def random_new_coding_language():
    random_codeing_language = random.choice(new_coding_language)

    # This is printing the random art idea
    print(random_codeing_language)

question = input('Hello i am random bot, you can pick from four random idea gearators which one will you pick(video_game_creation_ideas/coding_projects_ideas/art_ideas/new_coding_language)')

if question == 'video_game_creation_ideas':
    random_video_game_creation_ideas()
    
if question == 'coding_projects_ideas':
    random_coding_projects_ideas()

if question == 'art_ideas':
    random_art_ideas()

if question == 'new_coding_language':
    random_new_coding_language()
