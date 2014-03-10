このサイトについて
==================

I'm writing my templates in *Markdown!*

[語源辞典：スペースアルク](http://home.alc.co.jp/db/owa/etm_sch)


http://home.alc.co.jp/db/owa/etm_sch

Hightlight Code
---------------

HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Title</title>
</head>
<body>
</body>
</html>
```

Python

```python
def hello_vimmer():
  for i in range(10):
    print('Happy Vimming')
```

Vim

```vim
" Utilities for list.

let s:save_cpo = &cpo
set cpo&vim

function! s:pop(list)
  return remove(a:list, -1)
endfunction

function! s:push(list, val)
  call add(a:list, a:val)
  return a:list
endfunction

function! s:shift(list)
  return remove(a:list, 0)
endfunction

function! s:unshift(list, val)
  return insert(a:list, a:val)
endfunction

function! s:cons(x, xs)
  return [a:x] + a:xs
endfunction

function! s:conj(xs, x)
  return a:xs + [a:x]
endfunction
```
