in pycharm :
    - mark src as source root
    - mark tests as test source root


run mypy
```shell
mypy --no-namespace-packages .
```

run the tests
```shell
pytest
```

create image : 
```shell
docker build -t mon-app-python .
```

run the app
```shell
docker run -p 8000:8000 -e PORT=8000 -e HOST=0.0.0.0  mon-app-python
```
