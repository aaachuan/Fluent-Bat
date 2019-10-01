### file-operation

#### Python文件读写

Python内置函数open()

```
>>> f = open('./test.txt','r')
>>> f.read()
'Tell Me,Do you bleed?'
>>> f.close()
```
| **Character** | **Meaning** |
| :------------ | :---------- |
|'r'            | open for reading (default)                                      |
|'w'            | open for writing, truncating the file first                     |
|'x'            | open for exclusive creation, failing if the file already exists |
|'a'            | open for writing, appending to the end of the file if it exists |
|'b'            | binary mode                                                     |
|'t'            | text mode (default)                                             |
|'+'            | open a disk file for updating (reading and writing)             |

在windows系统当中读取文件路径可以使用\,但是在python字符串中\有转义的含义，如\t可代表TAB，\n代表换行，所以我们需要采取一些方式使得\不被解读为转义字符。
有三种解决方法：
- 在路径前面加r，即保持字符原始值的意思。
```
>>> f = open(r'./test.txt','r')
```
- 替换为双反斜杠
```
>>> f = open('.\\test.txt','r')
```
- 替换为正斜杠
```
>>> f = open('./test.txt','r')
```

open()打开一个文件并返回file object(或者file-like object),如果该文件不能打开，则触发 OSError。
> There are actually three categories of file objects: raw binary files, buffered binary files and text files. 
> Their interfaces are defined in the io module.

[module-io](https://docs.python.org/zh-cn/3/library/io.html#module-io)
> 创建file object的规范方式是使用 open() 函数。

由于读写时有可能出现IOError，所以每次文件打开都需要正确关闭：
```
with open('./test.txt', 'r') as f:
    print(f.read())
```
Q：
```
>>> f = open('./test.txt','r')
>>> f.read()
'Tell me,Do you bleed?'
>>> f.read()
''
>>> f.tell()
21
>>> f.seek(0)
0
>>> f.read()
'Tell me,Do you bleed?'
>>>
```
当到达文件末尾（EOF）时，read()返回''，因为没有更多的数据要读取了。
> f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.
> To change the file object’s position, use f.seek(offset, whence). The position is computed from adding offset to a reference point; the reference point is selected by the whence argument. A whence value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. whence can be omitted and defaults to 0, using the beginning of the file as the reference point.

官方文档例子：
```
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```

> 调用`read()`会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用`read(size)`方法，每次最多读取size个字节的内容。另外，调用`readline()`可以每次读取一行内容，调用`readlines()`一次读取所有内容并按行返回`list`。因此，要根据需要决定怎么调用。
> --阮一峰's personal blog

```
>>> f = open('./test.txt','r')
>>> print(f.read())
Tell me,Do you bleed?
Batman
The killing Joker
>>> print(type(f.read()))
<class 'str'>
>>> f.close()
```

```
>>> f = open('./test.txt','r')
>>> print(f.readline())
Tell me,Do you bleed?

>>> print(type(f.readline()))
<class 'str'>
>>> f.close()
```

```
>>> f = open('./test.txt','r')
>>> f.readlines()
['Tell me,Do you bleed?\n', 'Batman\n', 'The killing Joker']
>>> print(type(f.readlines()))
<class 'list'>
>>> f.close()
```

自己写的word count:
```
import sys
import re
def word_count(path):
    count = {}
    with open(path) as f:
        str = f.read()
        str = str.lower()
        str = re.sub(r'\W', ' ', str)

        for word in str.split():
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
        return count

def main(argv):
    print(word_count(argv))

if __name__ == '__main__':
    main(sys.argv[1])
```
```
C:\Users\Administrator\Python\Fluent-Bat\Scripts\file-operation>python word_count.py ./reword.txt
{'i': 3, 'am': 3, 'a': 3, 'boy': 2, 'not': 1, 'and': 1, 'girl': 1}

C:\Users\Administrator\Python\Fluent-Bat\Scripts\file-operation>type reword.txt
I am a boy?
I am not a boy,and I am a girl.
```
有个比较鸡肋的是对`,.?`符合的处理，本来用replace()就可以的，但是replace()仅支持一次替换一个，同时替换多个得多次调用，所以采用正则表达式来匹配。
其它方法下次搞搞看。
#### Python处理log
字符串是不可变的有序集合
```
>>> s = 'hello'
>>> s[0] = 'H'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> s = 'H' + s[1:]
>>> s
'Hello'
>>> s + 'world'
'Helloworld'
>>> s * 3
'HelloHelloHello'
>>> char = ['a', 'b', 'c', 'd']
>>> ', '.join(char)
'a, b, c, d'
>>> s[::-1]
'olleH'
>>> ''.join(reversed(s))
'olleH'
>>>
```
文件和目录操作
列出当前目录下的所有目录:
```
>>> import os
>>> os.listdir()
['cache.bak', 'cache.dat', 'cache.dir', 'dbm_exitsing.py', 'dbm_new.py', 'dbm_official_example.py', 'dbm_test.py', 'example.db.bak', 'example.db.dat', 'example.db.dir', 'websites.bak', 'websites.dat', 'websites.dir']
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
[]
```
列出所有的`.py`文件：
```
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['dbm_exitsing.py', 'dbm_new.py', 'dbm_official_example.py', 'dbm_test.py']
```
os.path.splitext(x)将文件名和扩展名分开。利用Python内置的字符串方法后缀匹配，可以更加简短，通用性更好：
```
>>> [x for x in os.listdir() if x.endswith('.py')]
['dbm_exitsing.py', 'dbm_new.py', 'dbm_official_example.py', 'dbm_test.py']
```
[os.path](https://docs.python.org/zh-cn/3/library/os.path.html)
