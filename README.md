
# **Diner Hash: An Educational Computer Science Game**

## Table of Contents
- [Project Roadmap](#project-roadmap)
  - [Goals for Iteration I](#goals-for-iteration-i)
    - [Iteration I Guidelines](#iteration-i-guidelines)
  - [Goals for Iteration II](#goals-for-iteration-ii)
    - [Iteration II Guidelines](#iteration-ii-guidelines)
  - [Goals for Iteration II](#goals-for-iteration-iii)
    - [Iteration II Guidelines](#iteration-iii-guidelines)
  - [Overflow I Goals](#overflow-i-goals)
    - [Overflow I Guidelines](#overflow-i-guidelines)
  - [Overflow II Goals](#overflow-ii-goals)
    - [Overflow II Guidelines](#overflow-ii-guidelines)
- [Contributors](#contributors)
- [Coding Conventions](#coding-conventions)
- [Helpful Resources](#helpful-resources)

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

#### Iteration I Guidelines

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

#### Iteration II Guidelines

~~~~

>

~~~~

	Fibonacci Hours: 21

  

### **Goals for Iteration III (Final Development Week)**

Game framework (main menu/end game screens, scoreboard, timer). 

#### Iteration III Guidelines

~~~~

>

~~~~

	Fibonacci Hours: 8

  

### **Overflow I Goals**
*Due to the constraint of time, these tasks are moved to overflow goals.
Development time is limited to 3 weeks.*

Game feedback (implement ‘Excellent’, and ‘Good’ feedback labels, implement pop-
ups explaining user interaction with hashmap abilities)

#### Overflow I Guidlines

~~~~

>

~~~~

	Fibonacci Hours: 8

  

### **Overflow II Goals**
*Due to the constraint of time, these tasks are moved to overflow goals.
Development time is limited to 3 weeks.*

Sprite implementations and graphical animations

#### Overflow II Guidelines

~~~~

>

~~~~

	Fibonacci Hours: 21

  
## Contributors

Jillian David - *Scrum Master*

Beau Forest - *Team Member*

Mark Fraser - *Product Owner*

Naomi Nunis - *Team Member*

Dharak Vasavda - *Team Member*

## Coding Conventions

See [this](https://chris.beams.io/posts/git-commit/) entertaining link on writing descriptive commit messages

All Python files should follow the PyCodeStyle standard

Lines should be wrapped at 80 characters for all other file types

## Helpful Resources

- [Commit Messages](https://chris.beams.io/posts/git-commit/)
- [Sprite Intro](https://www.pygame.org/docs/tut/SpriteIntro.html)
- [Game Development with PyGame](https://pythonspot.com/game-development-with-pygame/)
- [Introduction to JavaFx for Game Development](https://gamedevelopment.tutsplus.com/tutorials/introduction-to-javafx-for-game-development--cms-23835)