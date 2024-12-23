## Virtual Environments
### Creating venv
`python -m venv <venv-path>`

### Activating venv
`source <venv-path>/bin/activate`

### Exporting packages to `requirements.txt`
`pip freeze > requirements.txt`


## Fixtures
Fixtures are placed in `<app_name>/fixtures`
Apply fixtures using command
`python manage.py loaddata <fixture_name>`
