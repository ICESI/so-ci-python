### Description
The op-stats service provides an api to interact with the operating system resources

### How to test
Tests are performed by the tox framework which dinamically creates and destroy virtual enviroments for testing.
```
$ tox -e pytest
```

### How to debug
In order to debug add a line 'import pdb' at the top of your python file.
Then add a line 'pdb.set_trace()' in the position where you want to have a breakpoint.
```
import pdb
...
pdb.set_trace()
...
```

You can run pytest with pdb enable using the following command:
```
pytest --pdb
```

### How to build
In progress

### How to deploy
In progress
