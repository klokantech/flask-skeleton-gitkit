# Flask application skeleton

```shell
$ source activate
$ dev build
$ dev manage db upgrade
$ dev up
^C
$ production build
$ production manage export_static /mnt/static
$ production up
```

Sample accounts:

- john.doe@example.com
- admin@example.com


Production images must have explicit image names.
Production containers must have explicit container names if they
are run on the same machine as development.
