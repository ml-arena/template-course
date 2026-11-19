# ML-Arena course template

Write an [ML-Arena](https://ml-arena.com) course as Markdown in a repository:
every commit on `main` is pushed to the platform. No API key, no secret in the
repository.

## Setup

1. Click **Use this template**.
2. On ML-Arena, open your Profile and **connect your GitHub account**. A
   repository owned by an organisation must also be added under **Profile →
   Trusted repositories**.
3. In `course.yaml`, set `course.slug` (the course's URL,
   `ml-arena.com/courses/<slug>`), its name and its dates, then commit to `main`.

The first push creates the course; the next ones update it. The run's **summary**
is the plan: each module and lesson created, updated, unchanged or orphaned. A
refused push (a lesson file that is missing, an unknown key, a broken image
link) changes nothing and fails the job with the platform's message.

To see the plan without changing anything, run the workflow from the **Actions**
tab (*Run workflow*): `dry_run` is ticked by default.

## Layout

```
course.yaml                  the manifest
intro/welcome.md             a lesson body, named by the manifest
assets/intro/diagram.png     an image a lesson links to
```

Every path, in `course.yaml` and in a lesson's links and images, is relative to
the **course root** (the folder of `course.yaml`), not to the lesson's file:
`![](assets/intro/diagram.png)`.

## `course.yaml`

| Key | Meaning |
|---|---|
| `course.name`, `course.slug` | Required. The slug is the course's identity and URL |
| `course.start_date`, `course.end_date` | `YYYY-MM-DD`. Required when the push creates the course |
| `course.visibility` | `private` (default), `unlisted` or `public` |
| `course.code`, `course.description`, `course.instructor_name` | Optional texts |
| `course.cover` | Optional cover image, a path from the course root |
| `modules[].title`, `modules[].slug` | Required |
| `modules[].summary`, `modules[].icon` | Optional |
| `modules[].visibility` | `private` (default); `public` lets other teachers reuse the module |
| `modules[].is_published` | Default `true`; `false` hides the module from students |
| `modules[].challenges` | Challenges attached to the module: `- slug: <challenge slug>`, with optional `label` and `pass_threshold`. Left out: the links made in the console are kept |
| `modules[].lessons[].title`, `.slug` | Required |
| `.file` or `.body_md` | The lesson's Markdown: a file, or inline text. Exactly one |
| `.kind` | `lesson` (default) or `exercise` |
| `.is_published` | Default `false`: students do not see the lesson |
| `.gated`, `.estimated_minutes` | Optional |
| `.children` | Sub-lessons, one level deep, with the same keys |
| `renamed_from` | On a module or a lesson: its previous slug (see below) |

An unknown key is refused. A key left out of a module or a lesson takes its
default, not the value it had before.

## Rules worth knowing

- **Slugs are identities.** Changing a slug creates a new module or lesson and
  orphans the old one. To rename, keep the content in place and write
  `renamed_from: old-slug` next to the new `slug`; students keep their progress.
- **Removing a lesson** from `course.yaml` unpublishes it; it is not deleted. Set
  `prune: true` on the action to delete such lessons, **with their students'
  progress**.
- **A module absent from `course.yaml`** is left untouched.
- **One writer.** A module pushed from the repository is read-only in the console
  editor. *Detach* it there to edit it by hand; the next push takes it back.
- **Challenges** are embedded in a lesson with a `mlarena:challenge slug=…` block:
  see `intro/first-steps.md`.

All the options: [ml-arena/mlarena-action](https://github.com/ml-arena/mlarena-action).
