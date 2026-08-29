# Contributing to Python Interview Questions

Thanks for helping grow this list! This repo collects **real Python interview
questions** encountered by candidates interviewing for DevOps, MLOps, SRE,
and related roles. If you've been asked a Python question in an interview,
please add it here.

## How to Contribute

1. **Fork** this repository.
2. Create a new branch for your change:
   ```bash
   git checkout -b add-question-<short-description>
   ```
3. Open the `Interview_questions` file and add your question at the **end
   of the list**, continuing the numbering.
4. Follow the format below.
5. Commit and push your branch, then open a **Pull Request** against `main`.

## Question Format

Please keep new entries consistent with the existing style:

```markdown
<N>. <Clear, one-line problem statement.>

   <If the question includes sample data/code, add it as a fenced code
   block or indented block, using valid Python syntax.>
```

**Guidelines:**
- State the question clearly and completely — someone should be able to
  attempt it without needing extra context.
- If there's sample input (a list, dict, DataFrame, etc.), include it and
  make sure it's syntactically valid Python.
- If the question was asked with a twist or constraint (e.g. "without using
  built-in functions," "must execute live," "handle edge cases"), include
  that constraint — it's often the point of the question.
- Keep company/interviewer names out of it — just the question itself.
- Avoid duplicates — do a quick search of the file before adding.

## What Counts as a Good Question

- Actually asked in a real interview (DevOps/MLOps/SRE/Python-adjacent roles
  preferred, but general Python is welcome too).
- Specific enough to be solvable, not just a vague topic.
- Categories we're especially interested in: scripting (files, logs,
  monitoring), cloud/AWS tasks, data structures/algorithms, and Python
  fundamentals asked with unusual constraints.

## Adding a Solution (Optional)

If you'd like to also contribute a solution, add it to a separate
`solutions.md` file (create one if it doesn't exist), referencing the
question number so it's easy to match up.

## Questions or Suggestions

Open an issue if you want to suggest a structural change (e.g. splitting
into categories, adding difficulty tags) rather than just adding a question.

Thanks for contributing — every question added helps someone else prepping
for their next interview! 🙌
