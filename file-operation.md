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