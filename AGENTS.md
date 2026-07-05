# AGENTS.md

## Contest workflow

Each contest is worked on in its own branch and merged back into `master` when done.
The steps below define the conventions for each stage.

### 1. Create a contest branch

Before participating in a contest, create a branch from `master`.
Branch name:

```
contest/<SERIES>-<NUMBER>
```

Examples: `contest/ABC-465`, `contest/ARC-220`.

### 2. Save the contest-end state

After the contest ends, commit the solutions that were AC during the contest, exactly as submitted.
Problems without an AC get no file at this step.
Commit message:

```
<SERIES> <NUMBER>: save contest-end AC
```

Example: `ABC 465: save contest-end AC`.

### 3. Mark post-contest TODOs

In a separate commit right after the contest-end commit:

- For each AC problem, add `# TODO: review` followed by a blank line at the top of the file.
- For each unsolved problem worth solving later, create a stub file containing only `# TODO: solve`.
- Unsolved problems not worth attempting get no file.

Commit message:

```
<SERIES> <NUMBER>: mark post-contest TODOs
```

Example: `ABC 465: mark post-contest TODOs`.

### 4. Resolve the TODOs

Resolve each TODO in its own commit, removing the resolved TODO marker.

Commit message, matching the TODO being resolved:

```
<SERIES> <NUMBER> <PROBLEM>: review
<SERIES> <NUMBER> <PROBLEM>: solve
```

Examples: `ABC 465 A: review`, `ABC 465 E: solve`.

### 5. Merge into master

Once every TODO is resolved, merge the branch into `master` with `--no-ff`, keeping the default merge message.
After merging, delete the branch both locally and on `origin`.

## Study workflow

Studying an algorithm in depth happens on its own branch, created from `master`.
Branch name:

```
study/<topic>
```

Examples: `study/shortest-path`, `study/segment-tree`.

Commit each practice problem solved along the way separately.
Commit message:

```
<CONTEST> <PROBLEM>: solve
```

Examples: `ABC 068 C: solve`, `典型アルゴリズム問題集 E: solve`.

Once the study is complete, merge and delete the branch as in contest step 5.

## Maintenance

Non-solution changes (README, dependencies, tooling) are committed directly on `master`.

## Problem help

When the user asks for help with a problem they are solving:

- Never read or reveal editorials or other people's solutions.
- Read the whole problem page, including the problem statement, constraints, input/output format, input/output samples,
  and time/memory limits.
- Give the smallest hint that lets the user keep thinking on their own; do not reveal the intended approach.
- If solving requires a specific algorithm or data structure, infer from this repo's solutions whether the user knows
  it.
  If not, name it as a study topic.
  If they know it, do not name it; at most confirm that no unfamiliar knowledge is needed.

These restrictions apply only while the user is solving the problem.
Once they have an AC, feedback on their code (readability, elegance, alternative implementations) is unrestricted.
