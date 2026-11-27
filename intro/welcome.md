# Welcome

You are reading the file `intro/welcome.md` of this course's repository. To
change this page, edit the file, commit it to `main`, and reload the page in a
minute or so.

## What happens on a commit

![The repository is pushed by GitHub Actions to ML-Arena](images/diagram.png)

1. GitHub Actions runs the workflow `.github/workflows/ml-arena.yml`.
2. The workflow sends the folder to ML-Arena with the course's key: this
   lesson, `course.yaml` and the challenge folders under `challenges/`.
3. ML-Arena checks everything first, then applies it, or nothing if something
   is wrong. The run's summary, in the **Actions** tab, lists what changed.

To try a change without publishing it, use the **Actions** tab: choose *Push to
ML-Arena → Run workflow* and keep `dry_run` ticked. The run shows the plan and
changes nothing.

## Writing a lesson

A lesson is Markdown: headings, lists, tables, code blocks and math such as
$e^{i\pi} + 1 = 0$.

```python
print("Hello, ML-Arena")
```

A new lesson is a new file plus an entry in `course.yaml` (a `title`, a `slug`
and its `file`). Students see it once you set `is_published: true`.

## Images sit beside the lesson

The image above is the file `intro/images/diagram.png`. The lesson links it as
`images/diagram.png`, a path from the folder of this lesson, as GitHub reads
it, so the page looks the same in GitHub's preview and on ML-Arena. A link with
`..` is refused, and a link to a file that is not in the repository stops the
push and names the link.

## Embedding a challenge

A lesson can show a challenge as a card that opens it. Write the block below
at the start of a line, without the four leading spaces, with the name of a
challenge of this course (`course.yaml` lists them):

    ```mlarena:challenge name="House prices"
    ```

An exercise of an exercise set is embedded the same way, with the set and the
exercise's key:

    ```mlarena:exercise name="Python basics" key=hello
    ```

A push is refused when a block names a challenge that does not exist. Run the
workflow as a dry run first to see that check without changing anything.
