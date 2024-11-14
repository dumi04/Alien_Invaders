# 2D-Game
This Python script utilizes the Pygame library to create a simple 2D game where the player controls a spaceship, shoots bullets, and earns points by destroying randomly moving alien enemies.

Instructions
Installation:

Make sure you have Python installed on your system.
Install the Pygame library by running pip install pygame in your terminal.
Game Controls:

Use the left and right arrow keys to move the player spaceship horizontally.
Press the space bar to shoot bullets.
Game Elements:

Player Spaceship: Controlled by the left and right arrow keys.
Alien Enemies: 20 randomly moving alien enemies on the screen.
Bullets: The player can shoot up to 3 bullets at a time.
Score: Points are earned for each alien enemy destroyed.
Scoring:

Each time a bullet collides with an alien enemy, the player earns one point.
The score is displayed at the top-left corner of the screen.
Game Over:

The game ends if any alien enemy reaches the bottom of the screen.
The "GAME OVER" message is displayed, and all enemies disappear.
File Requirements:

Ensure that the following image files are present in the same directory as the script:
background.jpg (background image for the game screen)
spaceship.png (image for the player's spaceship)
alien.png (image for the alien enemies)
bullet.png (image for the bullets)
Customization:

You can customize the game window dimensions by modifying the pygame.display.set_mode parameters.
Adjust the number of enemies (num_of_enemies) and bullets (num_of_bullets) based on your preferences.
Dependencies:

This script uses the Pygame library. Ensure it is installed before running the script.
Running the Game
Execute the script in a Python environment.
The game window will appear, and you can control the player spaceship using the arrow keys.
Press the space bar to shoot bullets and earn points by destroying alien enemies.
