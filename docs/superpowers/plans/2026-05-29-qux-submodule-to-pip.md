# qux Submodule → Pip Package Migration

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the qux git submodule with a pinned pip install of qux 0.8.2, bringing qjango in line with the qux 0.8.x migration standard.

**Architecture:** qux currently lives at `./qux/` as a git submodule; Python finds it because `wsgi.py` inserts the repo root onto `sys.path`. Removing the submodule directory makes Python fall through to the venv-installed package — no `sys.path` surgery needed. Both requirements files get the HTTPS-pinned tag URL; `.gitmodules` is deleted. No application code changes are required because qjango's qux import surface (`qux.seo.mixin.SEOMixin`, `qux.token.models.CustomTokenAuthentication`, `qux.auth.urls.appurls`) is unaffected by the 0.8.x removals documented in Zeus's migration notes.

**Tech Stack:** Python 3.12 / Django 5.x, qux 0.8.2 (`git+https://github.com/quxdev/qux.git@v0.8.2`), pytest-django or Django test runner.

---

## Affected files

| File | Action |
|------|--------|
| `requirements/py312_dj5.txt` | Add qux pin |
| `requirements/py38_dj4.txt` | Add qux pin |
| `.gitmodules` | Delete (qux is the only entry) |
| `qux/` (submodule) | Remove via `git submodule deinit` + `git rm` |
| `apps/gizmo/tests.py` | Create — import smoke tests (TDD baseline) |
| `apps/gizmo/tests` | Delete — empty no-extension placeholder |

No changes to `project/wsgi.py`, `project/settings/settings.py`, `project/urls.py`, or `apps/gizmo/views/appviews.py`.

---

## Task 1: Write failing import smoke tests

These tests will fail immediately (submodule still present, but they document the contract). They pass once the pip-installed qux is wired up and `manage.py check` is clean.

**Files:**
- Create: `apps/gizmo/tests.py`
- Delete: `apps/gizmo/tests` (empty placeholder with no extension)

- [ ] **Step 1: Delete the empty placeholder**

```bash
rm apps/gizmo/tests
```

- [ ] **Step 2: Create `apps/gizmo/tests.py`**

```python
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model

from apps.gizmo.views.appviews import ApplicationHomeView


class QuxImportSmokeTest(TestCase):
    """Verify qux APIs used by qjango survive the submodule→pip migration."""

    def test_seo_mixin_importable(self):
        from qux.seo.mixin import SEOMixin
        self.assertTrue(callable(SEOMixin))

    def test_token_auth_importable(self):
        from qux.token.models import CustomTokenAuthentication
        self.assertTrue(callable(CustomTokenAuthentication))

    def test_auth_urls_importable(self):
        from importlib import import_module
        mod = import_module("qux.auth.urls.appurls")
        self.assertTrue(hasattr(mod, "urlpatterns"))

    def test_application_home_view_resolves(self):
        factory = RequestFactory()
        request = factory.get("/")
        User = get_user_model()
        request.user = User()
        view = ApplicationHomeView.as_view()
        # Should not raise ImportError — that's the contract
        self.assertTrue(callable(view))
```

- [ ] **Step 3: Run tests — confirm they pass against the submodule (baseline)**

```bash
source venv/bin/activate
python manage.py test apps.gizmo --verbosity=2
```

Expected: all 4 tests pass against the old submodule. If any fail now, fix the test before proceeding.

- [ ] **Step 4: Commit baseline tests**

```bash
git add apps/gizmo/tests.py
git rm apps/gizmo/tests
git commit -m "test(gizmo): add qux import smoke tests as migration baseline"
```

---

## Task 2: Pin qux 0.8.2 in both requirements files

Both files currently have no qux entry at all — it arrived via submodule only.

**Files:**
- Modify: `requirements/py312_dj5.txt`
- Modify: `requirements/py38_dj4.txt`

- [ ] **Step 1: Add qux pin to `requirements/py312_dj5.txt`**

Append this line at the end of the file:

```
git+https://github.com/quxdev/qux.git@v0.8.2#egg=qux
```

- [ ] **Step 2: Add qux pin to `requirements/py38_dj4.txt`**

Append this line at the end of the file:

```
git+https://github.com/quxdev/qux.git@v0.8.2#egg=qux
```

- [ ] **Step 3: Commit**

```bash
git add requirements/py312_dj5.txt requirements/py38_dj4.txt
git commit -m "deps: pin qux 0.8.2 via HTTPS tag in requirements"
```

---

## Task 3: Remove the git submodule

Three git commands are required. **Order matters** — deinit before rm before module cache cleanup.

**Files:**
- Delete: `qux/` (submodule directory)
- Delete: `.gitmodules` (becomes empty after removal)

- [ ] **Step 1: Deinit the submodule**

```bash
git submodule deinit -f qux
```

Expected output contains:
```
Cleared directory 'qux'
Submodule 'qux' (https://github.com/quxdev/qux.git) unregistered for path 'qux'
```

- [ ] **Step 2: Remove from git tracking**

```bash
git rm -f qux
```

Expected output:
```
rm 'qux'
```

- [ ] **Step 3: Delete the module cache**

```bash
rm -rf .git/modules/qux
```

No output expected.

- [ ] **Step 4: Verify `qux/` directory is gone**

```bash
ls qux 2>&1
```

Expected: `ls: qux: No such file or directory`

- [ ] **Step 5: Delete `.gitmodules` — it had only one entry**

```bash
git rm .gitmodules
```

Expected: `rm '.gitmodules'`

- [ ] **Step 6: Commit submodule removal**

```bash
git commit -m "chore: remove qux git submodule (migrating to pip install)"
```

---

## Task 4: Install qux from pip and run system check

At this point qux is in requirements but not installed. The smoke tests will fail until after this step.

- [ ] **Step 1: Install qux 0.8.2**

```bash
source venv/bin/activate
pip install -r requirements/py312_dj5.txt
```

Watch for: `Successfully installed qux-0.8.2` (or similar). If pip errors with a git clone failure, check network access to github.com.

- [ ] **Step 2: Verify qux resolves from venv, not project root**

```bash
python -c "import qux; print(qux.__file__)"
```

Expected: path contains `site-packages/qux`, NOT the project root `qjango/qux`.

- [ ] **Step 3: Run Django system check**

```bash
python manage.py check
```

Expected:
```
System check identified no issues (0 silenced).
```

If any `ImportError` or `AppRegistryNotReady` appears, see the Troubleshooting section below.

- [ ] **Step 4: Run migrations check**

```bash
python manage.py migrate --check
```

Expected: no unapplied migrations (or only migrations from apps not yet run — not from qux itself changing).

---

## Task 5: Verify smoke tests pass and commit

- [ ] **Step 1: Run the smoke tests**

```bash
python manage.py test apps.gizmo --verbosity=2
```

Expected:
```
test_application_home_view_resolves ... ok
test_auth_urls_importable ... ok
test_seo_mixin_importable ... ok
test_token_auth_importable ... ok

Ran 4 tests in 0.XXXs

OK
```

If any test fails, see Troubleshooting.

- [ ] **Step 2: Commit**

```bash
git add apps/gizmo/tests.py
git commit -m "chore: migrate qux from git submodule to pip 0.8.2 — tests green"
```

---

## Troubleshooting

### `ImportError: cannot import name 'SEOMixin' from 'qux.seo.mixin'`

qux 0.8.x moved or renamed the class. Find it:

```bash
python -c "import qux.seo; print(dir(qux.seo))"
python -c "from importlib import import_module; m = import_module('qux.seo.mixin'); print(dir(m))"
```

Update the import in `apps/gizmo/views/appviews.py:3` and the test accordingly.

### `ImportError: cannot import name 'CustomTokenAuthentication' from 'qux.token.models'`

```bash
python -c "import qux.token.models; print(dir(qux.token.models))"
```

Update `project/settings/settings.py` REST_FRAMEWORK auth class string.

### `ModuleNotFoundError: No module named 'qux.auth.urls.appurls'`

```bash
python -c "import pkgutil, qux.auth.urls; [print(m.name) for m in pkgutil.iter_modules(qux.auth.urls.__path__)]"
```

Update the `include(...)` path in `project/urls.py`.

### `AppRegistryNotReady` during `manage.py check`

Pin to qux 0.8.2 (not 0.8.0). The 0.8.0 package has a known `AppRegistryNotReady` bug in `APIRequestLogDBHandler`. Confirm:

```bash
pip show qux | grep Version
```

Should show `0.8.2`. If not: `pip install "git+https://github.com/quxdev/qux.git@v0.8.2#egg=qux" --force-reinstall`.

### `qux` still resolves to old project-root path

The `qux/` directory wasn't fully removed. Check:

```bash
ls qux 2>&1          # should: No such file or directory
python -c "import qux; print(qux.__file__)"   # should: site-packages path
```

If the directory persists: `rm -rf qux/` then recheck.
