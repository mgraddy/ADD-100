'''Develop a Python-based Madlib based on a song of your choice. The program should collect at least 8 different pieces of information from the user and incorporate them into the song using named arguments. The goal is to practice using functions, user input, and string manipulation in Python. Important Note: Choose any song you like for your madlib, but remember, no Rickrolling! Be creative and respectful in your song choice. Task: Select a Song: Choose a song that is well-known and suitable for a classroom setting. Avoid any song with inappropriate or offensive content. Identify Variables: Determine at least 8 different variables that the user will provide to customize the song. These could include names, adjectives, nouns, places, etc. Write the Function: Define a function named custom_song that takes at least 8 parameters corresponding to the variables you've identified. Use f-strings to incorporate these parameters into the song's lyrics. Ensure the function prints the customized song lyrics. Collect User Input: Write code to collect user input for each of the 8 variables. Use clear and descriptive prompts to guide the user. Call the Function: Call the custom_song function with the user inputs as named arguments. Ensure the order of arguments matches the parameters in your function definition.'''
def custom_song(like_1, like_2, like_3, like_4, drink, location, dislike_1, dislike_2 ): # Define custom song with 8 parameters
    print(f"""CUSTOM SONG CREATED: \"Escape (The {title} Song)"
I was tired of my lady
We'd been together too long
Like a worn out recording
Of a favorite song
So while she lay there sleepin'
I read the paper in bed
And in the personal columns
There was this letter I read

If you like {like_1}
And {like_2}
If you're not into {dislike_2}
If you have half a brain
If you like {like_4}
{location}
Then I'm the love that you've looked for
Write to me and escape

I didn't think about my lady
I know that sounds kinda mean
But me and my old lady
Had fallen into the same old dull routine
So I wrote to the paper
Took out a personal ad
And though I'm nobody's poet
I thought it wasn't half bad

Yes, I like {like_1}
And {like_2}
I'm not much into {dislike_1}
I am into {drink}
I've got to meet you by tomorrow noon
And cut through all this red tape
At a bar called O'Malley's
Where we'll plan our escape

So I waited with high hopes
And she walked in the place
I knew her smile in an instant
I knew the curve of her face
It was my own lovely lady
And she said, "Oh, it's you"
Then we laughed for a moment
And I said, "I never knew"

That you like {like_1}
And {like_2}
And {like_3}
And the taste of {drink}
If you like {like_4}
{location}
You're the lady I've looked for
Come with me and escape
If you like {like_1}
And {like_2}
If you're not into {dislike_2}
If you have half a brain
If you like {like_4}
{location}
I'm the love that you've looked for
Write to me and escape""")

print("This program will make a Madlibs version of a famous late 70's song about a vacation. For each question, there will be an optional syllable guideline if you want your answers to still fit the tune of the song. Use present participle for all verbs.")
like_1 = input("Your favorite thing about vacation (5 syllables): ")
title = like_1.capitalize()
like_2 = input("Something else you like about vacation (6 syllables): ")
like_3 = input("Something else you like about vacation (6 syllables): ")
like_4 = input("An activity you enjoy on vacation (6 syllables): ")
location = input("Where or when do you most enjoy doing that activity? Include a leading preposition (e.g. \"In the rolling green hills\")(6 syllables): ")
drink = input("Your favorite beverage to enjoy on vacation (2 syllables): ")
dislike_1 = input("Something you definitely wouldn't want to do on vacation (2 syllables): ")
dislike_2 = input("Something else you definitely wouldn't want to do on vacation (2 syllables): ")
custom_song(like_1, like_2, like_3, like_4, drink, location, dislike_1, dislike_2)
