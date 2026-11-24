# First steps

## Images sit beside the lesson

![The repository is pushed by GitHub Actions to ML-Arena](images/diagram.png)

This image is the file `intro/images/diagram.png`. The lesson links it as
`images/diagram.png`, a path from the folder of this lesson, as GitHub reads
it. The page therefore looks the same in GitHub's preview and on ML-Arena.

- Put a lesson's images and data files in its folder or below it, for example
  in `images/`.
- A link with `..` is refused, because it leaves the lesson's folder.
- A link to a file that is not in the repository stops the push and names the
  link, so a broken image never reaches your students.

## Embedding a challenge

A lesson can show a challenge as a card that opens it. Write the block below
at the start of a line, without the four leading spaces, with the slug of a
challenge that exists (the end of its URL, `ml-arena.com/challenges/<slug>`):

    ```mlarena:challenge slug=your-challenge-slug
    ```

An exercise of an exercise set is embedded the same way, with the set's slug
and the exercise's key:

    ```mlarena:exercise slug=your-exercise-set-slug key=hello
    ```

A push is refused when a block names a challenge that does not exist. Run the
workflow as a dry run first (**Actions → Push course to ML-Arena → Run
workflow**) to see that check without changing anything.

To count a challenge in the students' progress, attach it to the module in
`course.yaml` (`challenges:`) as well.
