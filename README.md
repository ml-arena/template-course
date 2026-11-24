# ML-Arena course template

Write an [ML-Arena](https://ml-arena.com) course as Markdown files in a GitHub
repository. Every commit on `main` updates the course on the platform. There is
no API key and no secret to store.

## Quick start

1. Click **Use this template** (a private repository works).
2. On ML-Arena, open your **Profile** and **connect your GitHub account**. If
   the repository belongs to an organisation or to someone else, also add it
   under **Profile → Trusted repositories**.
3. In `course.yaml`, change `course.slug` (it becomes the course's URL,
   `ml-arena.com/courses/<slug>`), the name and the dates. Commit to `main`.

The first push creates the course and the next pushes update it. Open the run
in the **Actions** tab: its summary is the plan, with each module and lesson
*created*, *updated* (with the fields that changed), *unchanged* or *orphaned*.
If the platform refuses the push (a missing lesson file, an unknown key, a
broken image link), nothing changes and the job fails with the platform's
message.

**Check before you publish.** In the **Actions** tab, choose *Push course to
ML-Arena → Run workflow*. `dry_run` is ticked by default: the run shows the plan
and changes nothing.

## Already have a course on ML-Arena?

Start from your course rather than from this template. Use either of these:

- In the Studio, open the course → **Settings → Download as a folder (.zip)**.
- Or, from a terminal: `mlarena course export <slug>`. This needs a teacher
  API key in `MLARENA_API_KEY`.

The folder holds `course.yaml`, one Markdown file per lesson with its images
beside it, the cover, this workflow and a `README.md`. If a lesson links a file
the course does not hold, that README lists it under *Fix before your first
push*.

**The course's owner makes the first push.** A module written in the Studio
moves to the repository only when its owner pushes it; an assistant's run,
even a dry run, is refused until then. After that first push, the assistants'
commits update the course too. As the owner:

1. Commit the folder to a new repository (a private one works).
2. Run the workflow once as a dry run (**Actions → Run workflow**). Every
   lesson should read *unchanged*; each module reads *adopted*: it moves from
   the Studio to the repository.
3. Untick `dry_run` and run it again, or push a commit to `main`. The owner's
   push can also be `mlarena course push` with the owner's key, or the Studio's
   *Import / update from repository*.

## Layout

```
course.yaml                    the manifest: course, modules, lessons
intro/                         one folder per module
  welcome.md                   a lesson, named by course.yaml
  first-steps.md
  images/diagram.png           an image of the lessons of this folder
.github/workflows/push.yml     the workflow that pushes to ML-Arena
```

**A relative link is relative to the file it is written in**, as on GitHub, so
a lesson looks the same in GitHub's preview and on ML-Arena:

- In a lesson, `![](images/diagram.png)` means `intro/images/diagram.png`.
- In `course.yaml`, the paths (`file`, `cover`) start from the folder of
  `course.yaml`.
- A link with `..` is refused. Keep a lesson's images and files in its folder
  or below it.
- The lessons of a module share one store of files, so one link names one
  file. If two lessons in different folders link `images/x.png`, both must
  point to the same file. The simplest rule is one folder per module.

## `course.yaml`

| Key | Default | Meaning |
|---|---|---|
| `course.name`, `course.slug` | required | The slug is the course's identity and URL |
| `course.start_date`, `course.end_date` | | `YYYY-MM-DD`. Required when the push creates the course |
| `course.visibility` | `private` | `private`, `unlisted` or `public` |
| `course.code`, `course.description`, `course.instructor_name` | | Optional texts |
| `course.cover` | | Cover image (PNG, JPEG, GIF or WebP), a path from `course.yaml` |
| `modules[].title`, `modules[].slug` | required | |
| `modules[].summary`, `modules[].icon` | | Optional |
| `modules[].visibility` | `private` | `private`, `unlisted` or `public`; `public` lets other teachers reuse the module. Left out of an existing module: unchanged |
| `modules[].is_published` | `true` | `false` hides the whole module from students |
| `modules[].challenges` | | Challenges attached to the module: `- slug: <challenge slug>`, with optional `label` and `pass_threshold`. Left out: the module keeps the challenges attached in the Studio |
| `modules[].lessons[].title`, `.slug` | required | |
| `.file` or `.body_md` | one of the two | The lesson's Markdown: a file (path from `course.yaml`), or the text inline |
| `.kind` | `lesson` | `lesson` or `exercise` |
| `.is_published` | `false` | Students see only published lessons |
| `.gated` | `false` | Only enrolled students read it, even in a public course |
| `.estimated_minutes` | | Shown to students |
| `.children` | | Sub-lessons, one level deep, with the same keys |
| `renamed_from` | | On a module or a lesson: its previous slug (see below) |

An unknown key is refused. In `course`, a key you leave out keeps the course's
current value. In a module or a lesson, a key you leave out takes the default
above, not the value it had before. The exceptions are a module's `visibility`
and `challenges`, which stay as they are.

## Rules worth knowing

- **Slugs are identities.** If you change a slug, the push creates a new module
  or lesson and orphans the old one. To rename, write `renamed_from: old-slug`
  next to the new `slug`, and students keep their progress.
- **Removing a lesson** from `course.yaml` unpublishes it. It is not deleted.
  Set `prune: true` on the action to delete such lessons **with their students'
  progress**.
- **A module missing from `course.yaml`** is left as it is. A module of the
  course written in the Studio stays editable there.
- **One writer per module.** A module pushed from the repository is read-only
  in the Studio, and the Studio shows the commit it came from. The module's
  owner can choose *Edit here instead* to hand it back to the Studio. The next
  push takes it back.
- **Challenges and exercises** are embedded in a lesson with a block naming
  them by slug. `intro/first-steps.md` shows how. The push is refused when a
  block names a challenge that does not exist.

## Several courses in one repository

Give each course its own folder, each with its own `course.yaml`. Keep a
single workflow at the repository root: the `on:` and `permissions:` of
`push.yml` as they are, and its job replaced by one job per course through a
matrix:

```yaml
jobs:
  push:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false                          # one refused course does not stop the other
      matrix:
        course: [ml-practice, deep-learning]   # the folders, one per course
    steps:
      - uses: actions/checkout@v7
      - uses: ml-arena/mlarena-action@v1
        with:
          command: course-push
          path: ${{ matrix.course }}
          dry-run: ${{ inputs.dry_run || false }}
```

`path` is the folder that holds the course. Only that folder is sent. A course
that did not change reports *unchanged*. If you exported a course into a
sub-folder, delete its `.github/` folder: GitHub reads workflows only at the
repository root.

All the action's options: [ml-arena/mlarena-action](https://github.com/ml-arena/mlarena-action).
