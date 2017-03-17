import spynner
import codecs
from PyQt4.QtCore import Qt

b = spynner.Browser()
b.show()
b.load("https://www.bet365.com/?lng=3&cb=105802124239#/AC/B13/C1/D50/E2/F163/")
b.wk_fill('input[name=q]', 'soup')
# b.browse() # Shows the word soup in the input box

b.sendKeys("input[name=q]",[Qt.Key_Enter])
b.wait(2)
codecs.open("out.html","w","utf-8").write(b.html)
print b.html
