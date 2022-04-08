# Python Packaging 
https://py-pkgs.org/welcome


# Helpful snippets

https://github.com/pytest-dev/pytest-reportlog

        with capsys.disabled():
            print('))))))))))))))))' + address.id)

print(\*a, sep = "\n")

print str(a)[1:-1]

print(' '.join(map(str, a)))

print"in new line"
print('\n'.join(map(str, a)))

---

You can turn a list into function arguments using \*:

def f(a,b,c): print a, b, c
x = [1,2,3]
f(_x)
f(_(1,2,3))

---

# Slider

styles https://github.com/Wanderson-Magalhaes/PyOneDark_Qt_Widgets_Modern_GUI/blob/master/gui/widgets/py_slider/py_slider.py

# Spilt and echo each line

for i in $(echo $PATH | tr ":" "\n"); do echo $i; done

https://stackoverflow.com/questions/9542738/python-find-in-list

# DI decorator

!!! Probably have to use metaclasses with inspection since decorators are man AFTER class instaniation

- On class with this set as metaclass allow somehow to pass another class/metaclass to it can also
  inherit from that

`__new__` is called for the creation of a new class
`__init__` is called after the class is created, to perform additional initialization before the class is handed to the caller
`__call__` is invoked when a new instance is created and used to intercept creation of instances.

https://docs.python.org/3/library/inspect.html
http://pymotw.com/2/inspect/

see functools.singledispatch for registering class to DI
https://peps.python.org/pep-0318/

https://stackoverflow.com/questions/50384862/python-metaprogramming-generate-a-function-signature-with-type-annotation

https://www.informit.com/articles/article.aspx?p=1309289&seqNum=4
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Metaprogramming.html

# Theming

https://doc.qt.io/qtforpython/overviews/style-reference.html
https://doc.qt.io/qtforpython/overviews/stylesheet.html
https://doc.qt.io/qtforpython/overviews/stylesheet-customizing.html
https://doc.qt.io/qtforpython/overviews/stylesheet-reference.html
https://doc.qt.io/qtforpython/overviews/stylesheet-syntax.html
https://doc.qt.io/qtforpython/overviews/stylesheet-examples.html

qss files

Set stylesheet from text with placeholders
https://github.com/Wanderson-Magalhaes/PyOneDark_Qt_Widgets_Modern_GUI/blob/master/gui/widgets/py_line_edit/py_line_edit.py
[LIGHT] https://github.com/Wanderson-Magalhaes/PyOneDark_Qt_Widgets_Modern_GUI/blob/master/gui/themes/bright_theme.json
[DARK] https://github.com/Wanderson-Magalhaes/PyOneDark_Qt_Widgets_Modern_GUI/blob/master/gui/themes/default.json

self.setStyleSheet(
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;"
)

```css
::root {
  /* General style definitions */
  /* ************************* */
  --white:                #ededef
  --gray-light:           #8a95aa
  --gray-dark:            #36373d
  --black:                #222327
  --black-ligher:         #333333
  --green:                #55ff7f
  /* #55FF00 ?? */
  --orange:               #f50
  --red:                  #ff5555
  --pink:                 #ff007f
  --purple:               #9c6dcd
  --blue:                 #55aaff
  --blue-light-0:         #edf0f5
  --blue-light-25:        #dce1ec
  --blue-light-50:        #c3ccdf
  /* --blue-dark-0:       #343b48 */
  --blue-dark-0:          #33334c
  --blue-dark-50:         #27273a
  --blue-dark-100:        #1d1d2b

  --font-style:           "Segoe UI"
  --font-size:            9pt

  --border-radius:        10px
  --border-size:          2px

  /* Element definitions */
  /* ******************* */
  /* Window */
  --window-background-color:    var(--blue-dark-100)

  /* Inputs */
  --input-background-color:     var(--blue-dark-0)
  --input-border-radius:        var(--border-radius)

  /* Text */
  --text-color:                 var(--white)
  --text-disabled-color:        var(--gray-dark)
  --text-success-color:         var(--green)
  --text-danger-color:          var(--red)
  --text-font-size:             var(--font-size)

  /* Button */
  --button-background-color:    var()
  --button-hover-color:         var()
  --button-pressed-color:       var()

  /* Icon */
  --icon-background-color:    var()
  --icon-hover-color:         var()
  --icon-pressed-color:       var()

  /* Card */
  --card-text-color:            var(--black)
  --card-light-background-color:var(--white)
  --card-dark-background-color: var(--blue-dark-0)
  --card-border-radius:         var(--border-radius)

  /* Frames */
  --frame-background-color:     var(--blue-dark-50)
  --frame-border-radius:        var(--border-radius)
}
```

# Resource Files

https://doc.qt.io/qtforpython/overviews/resources.html
https://doc.qt.io/qtforpython/tutorials/basictutorial/qrcfiles.html
https://www.pythonguis.com/tutorials/pyside-qresource-system/

# GREAT RESOURCES

- https://python-course.eu/
-
-
-
-
-

#

dict info https://blog.teclado.com/python-dictionary-merge-update-operators/
