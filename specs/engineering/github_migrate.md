## Plan: Migrate to New GitHub Repository

**TL;DR:** Sanitize the codebase (update .gitignore, scrub credentials), wipe the existing git history, init a fresh repo, then connect and push to a new public GitHub repository named `playwright_python_framework`.

---

**Phase 1 — Sanitize the codebase** *(do first, before any git ops)*

1. Update .gitignore — add missing entries: .vscode, venv, screenshots, `.env`
2. Replace hardcoded credentials in config.ini under the `[OCTANE]` section with safe placeholders:
   - `WORKSPACE_USER` → `YOUR_WORKSPACE_USER`
   - `USER_ID` → `your.email@example.com`
   - `PASSWORD` → `YOUR_PASSWORD`
   - `AUTOMATED_TEST_ID` → `YOUR_AUTOMATED_TEST_ID`

**Phase 2 — Re-initialize git** *(parallel steps 3–4, then 5–6 sequentially)*

3. Delete the existing .git directory to erase all history: `Remove-Item -Recurse -Force .git`
4. Initialize a new repo: `git init`
5. Stage all files: `git add .`
6. Create initial commit: `git commit -m "Initial commit"`

**Phase 3 — Connect to GitHub and push**

7. **You** create the repo at [github.com/new](https://github.com/new) — name it `playwright_python_framework`, set to **Public**, and select **no README/gitignore template** (to keep it empty)
8. Add remote: `git remote add origin https://github.com/<YOUR_USERNAME>/playwright_python_framework.git`
9. Push: `git push -u origin main`

---

**Relevant files**
- .gitignore — add 4 missing entries
- config.ini — replace `[OCTANE]` credentials with placeholders

**Verification**
1. `git status` shows clean tree after commit
2. `git log --oneline` shows exactly 1 commit
3. Repo is visible at `https://github.com/<USERNAME>/playwright_python_framework`
4. Inspect config.ini in the public repo — confirm no real credentials appear

**Scope exclusions**
- No git history migration
- No branch protection rules or GitHub Actions setup
- No collaborators or repo settings configured
- azure-pipelines.yml left as-is

---

Does this plan look good, or would you like to adjust anything before implementation begins?