
# **Diner Hash: An Educational Computer Science Game**



Diner Hash is an educational game to teach prospective students about the Hash
table data structure in a gamified form.

  

## Project Roadmap

To maintain consistency with the Agile Framework, we will have a total of 3
iterations for the product development.

The amount of time necessary for each iteration will be measured in Fibonacci
Hours.

Code blocks written under the 'Guideline' header contain tasks which are listed
in chronological order for completion.

  

### **Goals for Iteration I**

User interactions (movement, object collision, object retrieval/placement)

#### Guideline:

~~~~

> Build basic enivornment
    > @Mark: Build an environment, rather than a grid/board. That way, character
    movement is not constrained to an n*n grid
    > Ideally, the environment would have its own module, environment.py  

> Create a basic character placed on the basic grid/board
    > Ideally, create a separate module for this, character.py
    > character.py will manage character generation onto the board

> Allow for interaction with character (keybindings mapped to character
    movement)
    > Map keybindings to character actions, such as move and update
    > Interaction can be handled within character.py with respective functions
    such as update_location()

> Generate objects on the environment
    > For extensibility, this can be handled in a module, generate_objects.py
    > environment.py can inherit code from generate_objects.py and spawn them
    into the environment

> Detect character collision with objects
    > We can decide this later depending on how our project file structure ends
    up
    > Most likely there will need to be some character update function where the
    character's coordinates intersects with the edges of the object's
    coordinates and then prints out detection of collision

> Allow for character to pick up objects:
    > Map keybinds to character for pick up action
    > Print pick up action message neatly to console output
    > For now, I'm guessing this will only be console write-outs

> Print collision messages neatly to console output
    > More like a cleanup step to make sure all of the above test cases are
    printed out neatly onto the console

~~~~

  

	Fibonacci Hours: 8

  
  

### **Goals for Iteration II**

Foundational game logic (end conditions, “hash station” functionality)

#### Guideline:

~~~~

>

~~~~

	Fibonacci Hours: 21

  

### **Goals for Iteration III (Final Development Week)**

Game framework (main menu/end game screens, scoreboard, timer). 

#### Guideline:

~~~~

>

~~~~

	Fibonacci Hours: 8

  

### **Overflow goals I**
*Due to the constraint of time, these tasks are moved to overflow goals.
Development time is limited to 3 weeks.*

Game feedback (implement ‘Excellent’, and ‘Good’ feedback labels, implement pop-
ups explaining user interaction with hashmap abilities)

#### Guideline:

~~~~

>

~~~~

	Fibonacci Hours: 8

  

### **Overflow Goals II**
*Due to the constraint of time, these tasks are moved to overflow goals.
Development time is limited to 3 weeks.*

Sprite implementations and graphical animations

#### Guideline:

~~~~

>

~~~~

	Fibonacci Hours: 21

  
**Contributers**

Jillian David - *Scrum Master*

Beau Forest - *Team Member*

Mark Fraser - *Product Owner*

Naomi Nunis - *Team Member*

Dharak Vasavda - *Team Member*

## Coding Conventions

See [this](https://chris.beams.io/posts/git-commit/) entertaining link on writing descriptive commit messages

All Python files should follow the Pep8 standard

Lines should be wrapped at 80 characters for all other file types

## Helpful Resources

- [Sprite Intro](https://www.pygame.org/docs/tut/SpriteIntro.html)
- [Game Development with PyGame](https://pythonspot.com/game-development-with-pygame/)
- [Introduction to JavaFx for Game Development](https://gamedevelopment.tutsplus.com/tutorials/introduction-to-javafx-for-game-development--cms-23835)