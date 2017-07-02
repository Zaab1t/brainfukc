# brainfukc
The flexibility of Python and the raw logic of brainfuck in a seamless integration, that even allows metaprogramming:


```python
>>> def reverse_string(s):
>>>     code = '>'.join([',']*len(s)) + '<'.join(['.']*len(s))
>>>     return brainfukc.run(code, s)

>>> reverse_string('racecar')
racecar
```
