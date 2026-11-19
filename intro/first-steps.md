# First steps

## How this course is published

![The repository is pushed by GitHub Actions to ML-Arena](assets/intro/diagram.png)

Every commit on `main` runs a GitHub Actions job that pushes the course to
ML-Arena. Images are files of the repository: link them with their path **from
the course root** (the folder of `course.yaml`), as above.

## Embedding a challenge

A lesson can show a challenge as a card. Write the block below at the start of a
line, without the four spaces, with the slug of a challenge that exists
(`ml-arena.com/challenges/<slug>`):

    ```mlarena:challenge slug=your-challenge-slug
    ```

An exercise of an exercise set is embedded the same way:

    ```mlarena:exercise slug=your-exercise-set-slug key=hello
    ```

A push is refused when a block names a challenge that does not exist.
