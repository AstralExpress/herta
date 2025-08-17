# Herta

## Setup

### Samba setup

Important arguments to create a share, as explained in the docs:

```
    -s "<name;/path>[;browse;readonly;guest;users;admins;writelist;comment]"
                Configure a share
                required arg: "<name>;</path>"
                <name> is how it's called for clients
                <path> path to share
                NOTE: for the default values, just leave blank
                [browsable] default:'yes' or 'no'
                [readonly] default:'yes' or 'no'
                [guest] allowed default:'yes' or 'no'
                NOTE: for user lists below, usernames are separated by ','
                [users] allowed default:'all' or list of allowed users
                [admins] allowed default:'none' or list of admin users
                [writelist] list of users that can write to a RO share
                [comment] description of share
    -u "<username;password>[;ID;group;GID]"
                Add a user
                required arg: "<username>;<passwd>"
                <username> for user
                <password> for user
                [ID] for user
                [group] for user
                [GID] for group
```

## Next steps

### Features

- Functions to create users, manage shares / folders / permissions, etc.

### Tech
- Generate .env automatically from a friendly config file (avoids having to write commands in the .env file)
