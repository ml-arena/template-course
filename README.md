# ML-Arena course template

Keep an [ML-Arena](https://ml-arena.com) course in a GitHub repository: its
lessons, and every challenge's code, data and scoring. Every commit on `main`
updates the course. The repository pushes with **the course's key**, a secret
that belongs to the course and pushes that course only.

> The `challenges/` folders hold answer keys (`y_test.csv`) and hidden tests.
> Keep this repository **private**.

## Set up (once)

| # | Where | Step |
|---|---|---|
| 1 | ML-Arena: Studio → **New → Course** | Name it. *Where will you edit it?* **On GitHub**. Create |
| 2 | The wizard's step *Repository* | **Create the repository**: GitHub opens "new repository" from this template, private. Create it, then type its `owner/name` back in the wizard |
| 3 | The wizard's step *Key* | **Create the key** and copy it (it is shown once). **Add it to the repository** opens the repository's *Settings → Secrets and variables → Actions → New repository secret*: name `MLARENA_COURSE_KEY`, value the key |
| 4 | GitHub: **Actions → Push to ML-Arena → Run workflow** | Untick `dry_run` to apply, or push any commit to `main` |
| 5 | The wizard's step *First push* | It shows the run: "Updated from owner/name @ abc1234: 1 module, 1 lesson, 1 draft challenge". Open the course |

Open a run in the **Actions** tab: its summary is the plan, with each module,
lesson and challenge *created*, *updated* (with the fields that changed) or
*unchanged*. If the platform refuses the push (a missing lesson file, an
unknown key, a broken image link, an `env.py` that does not load), nothing
changes and the job fails with the platform's message. Every run, refused ones
included, is listed in the course's **Settings › GitHub**.

**Check before you publish.** *Run workflow* keeps `dry_run` ticked by default:
the run shows the plan and changes nothing.

Then, in the Studio, start the challenge (its **Overview** lists what still
blocks **Start**) and share the course: visibility, dates, the join link,
assistants and the roster stay in the console.

## Already have a course on ML-Arena?

Start from your course rather than from this template: in the Studio, open the
course → **Settings › GitHub → Edit this course on GitHub…**. The wizard:

1. **Downloads the course as a repository** (`.zip`, or `mlarena course export
   <slug>` with a personal key): `course.yaml`, the lessons and their files, one
   folder per challenge, this workflow and a `README.md`.
2. **Creates an empty private repository**, where you put the folder (three git
   commands, or GitHub's upload page: the `.github` folder is hidden on a Mac and
   on Windows, so the wizard also links *Add file → Create new file* with the
   workflow's path and content).
3. **Connects it and creates the key** (`MLARENA_COURSE_KEY`, as in step 3
   above). The course is now *connecting*: the console stays fully editable, and
   every run is a plan.
4. **Shows the first plan.** Pushed back unchanged, it reads *unchanged*
   everywhere; otherwise it lists what the repository would replace. **Switch to
   GitHub editing**: from then on each commit applies.

## Editing on GitHub

- Lessons, modules, challenges and their files are edited here, and **the last
  push wins**. In the console they are read-only under a banner with *Edit in the
  console instead…*, which revokes the keys and stops the pushes (your
  repository is not changed; download the course again to come back).
- What the console keeps in every mode: visibility, dates, enrolment and the
  roster, assistants, report recipients, Start and Stop of a challenge, its
  end date, *Update scoring*, its teams and submissions. `course.yaml` refuses
  `visibility`, `start_date` and `end_date`.
- **What the repository no longer lists** is not deleted: a lesson is
  unpublished (its students' progress is kept; `prune: true` deletes it), a
  module is unpublished, a challenge leaves its module and the course page, with
  its submissions and scores kept. Putting it back brings it back.
- **A started challenge** takes changed files as an update: the platform runs
  the benchmark on the new files first and keeps the previous ones if it fails.
  Scores already given stay until *Update scoring*. Overview, image and the
  settings editable while running apply at once.

## Layout

```
course.yaml                      the manifest: course, modules, lessons, challenges
intro/                           one folder per module
  welcome.md                     a lesson, named by course.yaml
  images/diagram.png             an image of the lessons of this folder
challenges/house-prices/         one folder per challenge, named by course.yaml
  env.py                         the scoring: class Env, evaluate(self, submission_path)
  y_test.csv                     a scoring file next to env.py (never shown to participants)
  challenge.toml                 config and scoring; description = the card's blurb
  overview.md                    the challenge page
  data/sample_submission.csv     what participants download
  benchmark/submission.csv       the benchmark submission (your baseline)
  test_local.py                  scores the benchmark locally: python challenges/house-prices/test_local.py
.github/workflows/ml-arena.yml   the workflow that pushes to ML-Arena
```

**A relative link is relative to the file it is written in**, as on GitHub, so
a lesson looks the same in GitHub's preview and on ML-Arena:

- In a lesson, `![](images/diagram.png)` means `intro/images/diagram.png`.
- In `course.yaml`, the paths (`file`, `folder`, `cover`) start from the folder
  of `course.yaml`.
- A link with `..` is refused. Keep a lesson's images and files in its folder
  or below it.
- The lessons of a module share one store of files, so one link names one
  file. The simplest rule is one folder per module.

## `course.yaml`

| Key | Default | Meaning |
|---|---|---|
| `course.name` | required | |
| `course.slug` | | Optional: the key names the course. When written, it must be the course's slug |
| `course.code`, `course.description` | | Optional texts |
| `course.cover` | | Cover image (PNG, JPEG, GIF or WebP), a path from `course.yaml` |
| `modules[].title`, `modules[].slug` | required | |
| `modules[].summary`, `modules[].icon` | | Optional |
| `modules[].is_published` | `true` | `false` hides the whole module from students |
| `modules[].lessons[].title`, `.slug` | required | |
| `.file` or `.body_md` | one of the two | The lesson's Markdown: a file (path from `course.yaml`), or the text inline |
| `.kind` | `lesson` | `lesson` or `exercise` |
| `.is_published` | `false` | Students see only published lessons |
| `.gated` | `false` | Only enrolled students read it, even in a public course |
| `.estimated_minutes` | | Shown to students |
| `.children` | | Sub-lessons, one level deep, with the same keys |
| `modules[].challenges[].name` | required | The challenge's identity in the course, and its title |
| `.folder` | | The challenge's folder, a path from `course.yaml`. Left out, the entry only places an existing challenge |
| `.kernel_version` | | `file_v1`, `flex_v1`, `chat_v1` or `exercise_v1`. Required when the push creates the challenge |
| `.pass_threshold` | | The score that counts as passed (left out: unchanged; `null`: no bar) |
| `renamed_from` | | On a module, a lesson or a challenge: its previous slug or name (see below) |

An unknown key is refused. A key you leave out takes the default above. A
challenge entry written `slug:` (or `challenge_id:`) names an existing challenge
of this course and only places it.

## Rules worth knowing

- **Slugs and names are identities.** If you change one, the push creates a
  new module, lesson or challenge. To rename, write `renamed_from: <old>` next
  to the new value, and students keep their progress and their submissions. A
  started challenge's name is locked.
- **Challenges and exercises** are embedded in a lesson with a block naming
  them. `intro/welcome.md` shows how. The push is refused when a block names a
  challenge that does not exist.
- **Size.** 300 MB for the course's own files, 500 MB per challenge folder,
  100 MB per file. A Git LFS pointer is refused: add `lfs: true` to the
  checkout step if you use LFS.

## Keys over time

- A key expires after 30, 90 or 365 days (365 by default). Settings › GitHub
  warns two weeks before.
- **Rotate:** create a second key, replace the secret `MLARENA_COURSE_KEY`,
  check one green run, revoke the old key.
- A key is revoked when the staff member who created it leaves the course, when
  the course goes back to console editing or is archived. The next run fails
  and says so: create a new key.
- **Repository transferred** (to a teacher, an organisation): the key does not
  name the repository, so nothing changes on ML-Arena. If the secret did not
  follow, add a new key. Settings › GitHub › Repository updates the links.

## Harden it

Once `main` is protected (*Settings → Branches*: pull requests and reviews), keep
the key where only `main` reaches it:

1. *Settings → Environments → New environment*: `ml-arena`.
2. *Deployment branches and tags*: **Selected branches**, add `main`.
3. Add the secret `MLARENA_COURSE_KEY` to that environment, then delete the
   repository secret of that name.
4. In `.github/workflows/ml-arena.yml`, uncomment `environment: ml-arena`.

A workflow on another branch then has no key to read.

## Several courses in one repository

Give each course its own folder, each with its own `course.yaml`, and each its
own key, stored as its own secret. Keep a single workflow at the repository root:
the `on:`, `permissions:` and `concurrency:` of `ml-arena.yml` as they are, and its
job replaced by one job per course through a matrix:

```yaml
jobs:
  push:
    if: ${{ !github.event.repository.is_template }}
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false                          # one refused course does not stop the other
      matrix:
        include:
          - course: ml-practice                 # the folder
            secret_name: MLARENA_COURSE_KEY_ML_PRACTICE
          - course: deep-learning
            secret_name: MLARENA_COURSE_KEY_DEEP_LEARNING
    steps:
      - uses: actions/checkout@v7
      - uses: ml-arena/mlarena-action@v2
        env:
          MLARENA_COURSE_KEY: ${{ secrets[matrix.secret_name] }}
        with:
          command: course-push
          path: ${{ matrix.course }}
          dry-run: ${{ inputs.dry_run || false }}
```

`path` is the folder that holds the course. Only that folder is sent. If you
exported a course into a sub-folder, delete its `.github/` folder: GitHub reads
workflows only at the repository root.

From a terminal, the same push: `MLARENA_COURSE_KEY=mlc_… mlarena course push .`;
`mlarena course status` shows where the course is edited, its keys and its last
runs. All the action's options:
[ml-arena/mlarena-action](https://github.com/ml-arena/mlarena-action).
