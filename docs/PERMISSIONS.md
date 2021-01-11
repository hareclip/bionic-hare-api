# Permissions

## Adding Admins

### Initial user

1. Run `python manage.py createsuperuser` and fill out prompts

### Using admin panel

1. Fill out form for creating user
2. Edit newly-created user and check `Is superuser`

## Adding Publishers

### Create publisher group

1. Log in to admin
2. Create `Publishers` group
3. Add following permissions:
    * `Can add user`
    * `Can change user`
    * `Can add article`
    * `Can change article`
    * `Can change profile`

### Adding new publishers

1. Create new user
2. Add new staff users to `Publishers` and check `Is staff` after user creation
3. Check `Is publisher` in `Profile` for user

## Adding Authors

1. Fill out form for creating user
    * Fill password with dummy password
2. Edit newly-created user and fill `First name` and `Last name`
3. Check `Is author` in `Profile` for user

## Publishing Articles

1. Fill out form for creating new article
    * Ensure `Contents file` is a markdown file
    * Ensure `Header image` is an image