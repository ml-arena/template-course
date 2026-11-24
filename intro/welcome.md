# Welcome

You are reading the file `intro/welcome.md` of this course's repository. To
change this page, edit the file, commit it to `main`, and reload the page in a
minute or so.

## What happens on a commit

1. GitHub Actions runs the workflow `.github/workflows/push.yml`.
2. The workflow sends `course.yaml` and the lessons it names to ML-Arena.
3. ML-Arena applies the whole course at once, or nothing if something is
   wrong. The run's summary, in the **Actions** tab, lists what changed.

To try a change without publishing it, use the **Actions** tab: choose *Push
course to ML-Arena → Run workflow* and keep `dry_run` ticked. The run shows the
plan and changes nothing.

## Writing a lesson

A lesson is Markdown: headings, lists, tables, code blocks and math such as
$e^{i\pi} + 1 = 0$.

```python
print("Hello, ML-Arena")
```

A new lesson is a new file plus an entry in `course.yaml` (a `title`, a `slug`
and its `file`). Students see it once you set `is_published: true`.

Next: **First steps**, on images and challenges.
