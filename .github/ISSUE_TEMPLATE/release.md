---
name: Release
about: Make a release.
title: ''
labels: 'release todo'
assignees: 'yannickkirschen'
---

# Release x.y.z

**Quality stuff**

- [ ] All dependencies have the latest version.
- [ ] README is up to date.
- [ ] App runs.

**Organization stuff**

- [ ] Merge develop to master.
- [ ] Create `release/x.y.z` branch.
- [ ] Update version in `VERSION`.
- [ ] Fill changelog
    - Date and version
    - Changes
    - Additions
    - Deletions
    - Notes
- [ ] Merge release branch to master (use release template!).
- [ ] Create tag x.y.z.
- [ ] Check if pipeline succeeds and artifact is pushed to PyPi.
- [ ] Remove release branch.
- [ ] Merge master to develop (mention this issue).
- [ ] Change version in `VERSION` to next snapshot version.
