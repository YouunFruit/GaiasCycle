# Git Workflow

This document outlines the Git workflow for the Gaia Cycle project to ensure consistency, collaboration, and code quality. It defines the branching strategy, commit conventions, and merging processes.

---

## 1. **Branching Strategy**
We follow the **Gitflow Workflow** to manage feature development and releases. The main branches include:

- **main**: Stable, production-ready code. Only release versions are merged here.
- **develop**: Integration branch for development. Features and fixes are merged here before being pushed to `main`.

### **Supporting Branches**
- **feature/***: For new features under development.
- **bugfix/***: For addressing bugs found during development.
- **hotfix/***: For critical fixes directly applied to `main`.
- **release/***: For preparing and finalizing new releases.

---

## 2. **Branch Naming Conventions**
- **Feature Branch**: `feature/<feature-name>`
  Example: `feature/user-authentication`
- **Bugfix Branch**: `bugfix/<bug-name>`
  Example: `bugfix/fix-login-error`
- **Hotfix Branch**: `hotfix/<hotfix-name>`
  Example: `hotfix/critical-bug-fix`
- **Release Branch**: `release/<version>`
  Example: `release/v1.0.0`

---

## 3. **Commit Messages**
Commit messages should follow the **Conventional Commits** format:

```
[type]: Short description

Optional longer description.
```

### **Types**
- **feat**: A new feature.
- **fix**: A bug fix.
- **docs**: Documentation updates.
- **style**: Code style changes (formatting, no logic changes).
- **refactor**: Code refactoring without changing functionality.
- **test**: Adding or updating tests.
- **chore**: Maintenance tasks like dependency updates.

**Examples:**
```
feat: Add user authentication

Implemented login and registration APIs with JWT support.

fix: Resolve login error

Fixed the invalid token issue during login.
```

---

## 4. **Workflow Process**

1. **Start a Feature**
    - Create a new branch from `develop`:
      ```bash
      git checkout develop
      git pull origin develop
      git checkout -b feature/<feature-name>
      ```

2. **Develop and Commit**
    - Make changes and commit following the conventions:
      ```bash
      git add .
      git commit -m "feat: Add new user authentication"
      ```

3. **Push Changes**
    - Push the branch to the remote repository:
      ```bash
      git push origin feature/<feature-name>
      ```

4. **Create a Pull Request (PR)**
    - Open a PR to merge changes into `develop`.
    - Add reviewers and link related issues.

5. **Code Review and Approval**
    - Reviewers approve or request changes.
    - Apply requested changes and update the PR.

6. **Merge to Develop**
    - Once approved, merge the branch into `develop`:
      ```bash
      git checkout develop
      git merge feature/<feature-name>
      git push origin develop
      ```

7. **Release and Deployment**
    - When ready, merge `develop` into `release/<version>` for final testing.
    - After testing, merge the release branch into `main`:
      ```bash
      git checkout main
      git merge release/<version>
      git push origin main
      ```

---

## 5. **Pull Request Guidelines**
- Use descriptive titles and link to related issues.
- Provide context for the changes in the PR description.
- Include screenshots or logs if applicable.
- Ensure all tests pass before submitting.

---

## 6. **Tagging Releases**
Tag releases for better version tracking:
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

---

## 7. **Handling Conflicts**
- If a merge conflict occurs:
```bash
git checkout branch-with-conflict
git merge branch-to-merge
```
- Manually resolve conflicts and mark them as resolved:
```bash
git add resolved-file.py
git commit -m "fix: Resolve merge conflict"
```

---

## Final Notes
Following this Git workflow ensures a structured approach to development, enabling collaboration and reducing deployment errors. For any issues, reach out to the project lead or consult the [Git Documentation](https://git-scm.com/doc).

