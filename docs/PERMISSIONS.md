# Permissions

## Adding Publishers

### Create publisher group

1. Log in to admin
2. Create `Publishers` group
3. Add following permissions:
  * `Can add user`
  * `Can change user`
  * `Can change article`
  * `Can change profile`

### Adding new publishers

1. Create new user
2. Add new staff users to `Publishers` and check `is_staff` after user creation
3. Check `is_publisher` in `Profile` for user

## Adding Authors

1. Fill out form for creating user
  * Fill password with dummy password

## Publishing Articles

1. Fill out form for creating new article
  * Ensure `Contents file` is a markdown file
  * Ensure `Header image` is an image