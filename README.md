# Alacritty-theme-changer

Try

```python
python alac-theme.py --help
```

```python
python alac-theme.py disco --help
```
![2021-05-20 13-59-20](https://user-images.githubusercontent.com/58474947/118960630-1e960500-b981-11eb-9171-9ec25c4025f9.gif)


#### For listing out available themes

```python
python alac-theme.py --list
```

#### For changing theme

```python
python alac-theme.py --theme breeze
```

#### Do some party and disco

Try

```python
python alac-theme.py disco

```

this arguments takes two argument

`--count [ how many times you want to make transition ]`

`--gap [ time gap of each transition in seconds ]`

by default `python ala-theme.py disco` have 30 count and 0.5 second of transition

you can pass any number and seconds eg-

`python alac-theme.py disco --count 20 --gap 1`

for terminating this script do `ctrl + c`

note that theme name is not case sensitive , you can pass in any case

#### Know current theme

```python
python alac-theme.py --curr
```

For now only work on linux , later i will update it for windows also
