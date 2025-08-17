# Herta

## Setup

## Next steps

### Features

- Functions to create users, manage shares / folders / permissions, etc.
- Mount encrypted folders over network

### Tech

- Simple command to mount / unmount files locally with WebDAV
- Change volume mounts to be able to easily back up user data (and avoid mistakes with docker)

### Experimental

- Edit theme (cf [docs](https://hub.docker.com/_/nextcloud#additional-volumes)), branding, etc.
- Explore apps and find out how to install them on startup

## Notes

- The config supports [hooks](https://hub.docker.com/_/nextcloud#auto-configuration-via-hook-folders) to execute code at certain points of Nextcloud's startup. 