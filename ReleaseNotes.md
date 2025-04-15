# Release 4.3.0

- Remove the ISSUE_TEMPLATE relying on the .github repository for the defaults.
- Add new workflows:
  - py-temp-fork-pvt_merge_with_local-def.yaml
  - py-temp-fork-scheduled_sync_with_upstream-def.yaml
- Removed workflow:
  - python-template-pypi-public-no-docker.yaml
- Updated config files
  - .gitignore
  - pre-commit-config.yaml
- Updated scripts
  - SetupDotEnv.ps1
  - SetupGitHubAccess.ps1
  - SetupPrivateRepoAccess.ps1

______________________________________________________________________

# Release 2.0.1

- Update ISSUE_TEMPLATE's
- Implement GitHub Reusable workflows.
- Upgrade to support Python 13.1
- Update formatting configuration files
  - flake8
  - .gitattributes
  - .gitignore
  - .pre-commit-config.yaml
  - readthedocs.yaml
  - rstcheck.cfg
- Delete redundant files
  - fixdate.bat
  - install.ps1
- Add utility scripts
  - SetupDotEnv.ps1
  - SetupGitHubAccess.ps1
  - SetupPrivateRepoAccess.ps1

______________________________________________________________________

# Release 2.0.0

- Update ISSUE_TEMPLATE's
- Update GitHub Workflows
- Move code from `Code` directory to `src` directory
- Implemented Poetry
- Removed irrelevant info from README.rst

______________________________________________________________________
