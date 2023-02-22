# Turtles & Tuples
```python
In this project, I made a few different files with the turtle module



```
## Turtleshapes
```python
In this, I had the turtle create shapes with the number of sides going from 3 up to 9. For each shape, it picks a random color and then draws the shape. Then it switches colors before drawing the next.
```
## spirograph
```python
In this, I made a simple spirograph. I used a tuple to get the rgb value. Each circle is a different color.
The program creates a circle, then changes angle by 2 degrees and creates a new circle. The program is done when it has ended where it started.
```
## Spiro2
```python
This one is similar to the spirograph but I added some extra lines/triangles in the design. Every six circles it creates a big line. Then it changes angles to create a triangle
```
## Main
```python
This was the main project for the Hirst_Painting_Project

It was modeled after the artist Hirst who makes dot paintings

I used the colorgram package to extract colors from a random picture, then I got the rgb values from each color. Next, I instructed my turtle to go to the bottom left corner. It chooses a random color from the list, creates a dot, then it stops painting and scoots to the right to create another dot. After 12 dots, it moves up on the y axis and to the left on the x axis to start again. It does this for 12 rows.

the colors.py file is where I used colorgram to extract colors. the thumnail is the picture I extracted from. 
```