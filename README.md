# chrplotlib
Plot graphs using chars

install:
```bash
$pip install chrplotlib
```

For the current developer version:
```bash
git clone git@github.com:guofei9987/chrplotlib.git
cd chrplotlib
pip install .
```

## example

```python
from chrplotlib import animation


def update_bar(i):
    data = 10 * np.random.rand(20)
    print(bar(data, label=range(20), max_height=10))
    print('\033[{}A'.format(12))


animation(update_func=update_bar, interval=range(100), pause=0.2)
```

![](/img/chrplotlib.gif)


```python
data = 10 * np.random.rand(20)
label = range(20)
```

```python
print(bar(data))
```

Print this:
```
                                 ▃▃                         
▃▃                      ▃▃       ██                ▅▅       
██ ▇▇                   ██       ██       ▇▇       ██       
██ ██                   ██       ██       ██       ██       
██ ██             ▇▇ ▃▃ ██       ██       ██       ██       
██ ██ ▄▄ ▅▅       ██ ██ ██       ██       ██       ██    ▃▃ 
██ ██ ██ ██    ▂▂ ██ ██ ██       ██ ▃▃    ██       ██    ██ 
██ ██ ██ ██    ██ ██ ██ ██       ██ ██    ██       ██    ██ 
██ ██ ██ ██    ██ ██ ██ ██ ▄▄ ██ ██ ██    ██    ▂▂ ██ ▇▇ ██ 
██ ██ ██ ██ ▃▃ ██ ██ ██ ██ ██ ██ ██ ██ ▃▃ ██ ██ ██ ██ ██ ██ 
```

```python
print(bar(data=data, label=range(20)))
```

Print this:
```
                                 ▃▃                         
▃▃                      ▃▃       ██                ▅▅       
██ ▇▇                   ██       ██       ▇▇       ██       
██ ██                   ██       ██       ██       ██       
██ ██             ▇▇ ▃▃ ██       ██       ██       ██       
██ ██ ▄▄ ▅▅       ██ ██ ██       ██       ██       ██    ▃▃ 
██ ██ ██ ██    ▂▂ ██ ██ ██       ██ ▃▃    ██       ██    ██ 
██ ██ ██ ██    ██ ██ ██ ██       ██ ██    ██       ██    ██ 
██ ██ ██ ██    ██ ██ ██ ██ ▄▄ ██ ██ ██    ██    ▂▂ ██ ▇▇ ██ 
██ ██ ██ ██ ▃▃ ██ ██ ██ ██ ██ ██ ██ ██ ▃▃ ██ ██ ██ ██ ██ ██ 
0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19

```



```python
print(bar(data, kind='bar'))
```

Get this:
```
  █▌█▌█▌█▌█▌█▌█▌█▌▌   
  █▌█▌█▌█▌█▌█▌█▌█▌    
  █▌█▌█▌█▌▋           
  █▌█▌█▌█▌█           
  ▌                   
  █▌█▌█▌▎             
  █▌█▌█▌█▌█▌█▌        
  █▌█▌█▌█▌█▌▌         
  █▌█▌█▌█▌█▌█▌█▌█▌▍   
  █▌▋                 
  █▌█▌                
  █▌█▌█▌█▌█▌█▌█▌█▌█▌▌ 
  █▌█▌█▌▍             
  ▌                   
  █▌█▌█▌█▌█▌█▌█▌█▌    
  █▌                  
  █▌▎                 
  █▌█▌█▌█▌█▌█▌█▌█▌█▎  
  █▌█▌                
  █▌█▌█▌█▌▌           
```


```python
print(bar(data=data, label=range(20), kind='barh'))
```

Get this:
```
0 █▌█▌█▌█▌█▌█▌█▌█▌▌   
1 █▌█▌█▌█▌█▌█▌█▌█▌    
2 █▌█▌█▌█▌▋           
3 █▌█▌█▌█▌█           
4 ▌                   
5 █▌█▌█▌▎             
6 █▌█▌█▌█▌█▌█▌        
7 █▌█▌█▌█▌█▌▌         
8 █▌█▌█▌█▌█▌█▌█▌█▌▍   
9 █▌▋                 
10█▌█▌                
11█▌█▌█▌█▌█▌█▌█▌█▌█▌▌ 
12█▌█▌█▌▍             
13▌                   
14█▌█▌█▌█▌█▌█▌█▌█▌    
15█▌                  
16█▌▎                 
17█▌█▌█▌█▌█▌█▌█▌█▌█▎  
18█▌█▌                
19█▌█▌█▌█▌▌        
```
