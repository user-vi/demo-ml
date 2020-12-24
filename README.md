# demo-ml

0. Clone this repository. Use bash.
```
    git clone https://github.com/user-vi/demo-ml
```

1. Change worker directory. pwd - current directory, cd - change directory, /demo-ml - path, ls - check files
```
    pwd
	ls
	cd /demo-ml
	ls
```

2. Create virtualenv. "test" - name of virtualenv
```
    python3.7 -m  virtualenv test
	source test/bin/activate
```

3. Install package to virtualenv.
```
    python3.7 -m pip freeze
	python3.7 -m pip install -r /requirements.txt
```

4. Run code.
```
    python3.7 main.py
```
