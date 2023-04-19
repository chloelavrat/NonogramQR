![qrcode](README.assets/banner.jpg)

I like nonograms and I like QR codes. Both open the door to a new word when scanned or completed. That's why I created a quick and dirty python code that transfers a string into a QR-code which is then encoded into a nonogram.

To access the message (or website), the player must first fill in the nonogram, then scan it. Obviously, the longer the message, the more complicated the nonogram.

Have fun :)

## Getting Started

In order to use the qr-gram code please do the following: 
```
git clone https://github.com/azerty-labs/QR-Gram.git
cd QR-Gram/
python -m venv venv
source ./venv/bin/activate
python pip install itertools pyqrcode argparse
python qr-gram.py
```

## Help ?

Need help? Use the `-h` command to get some.

```
$ python qr-gram.py -h
usage: qr-gram.py [-h] [message ...]

This script change a string into a QR-Code and then convert it into a nonogram.

positional arguments:
  message     put the message to encode here

options:
  -h, --help  show this help message and exit

have fun :)
```

## Example

This is an example of what qr-gram can do after lauching:

```
$ python qr-gram.py :)
```

Here we go : 
```
$ python qr-gram.py ":)"
>>> String to encode: :)
                      1 1                                
                    1 3 3             1         1 1      
                    3 1 1         3 3 1 4       3 3 1    
                  1 1 1 2 1 7   2 1 1 1 3   7   1 1 3 1  
                  1 2 2 1 1 1   1 2 1 1 1   1   2 1 1 1 7
                7 2 1 1 1 2 1 1 1 3 1 1 1 2 4 1 2 3 1 1 2
                3 1 3 3 3 1 1 1 3 1 2 2 3 2 1 1 1 3 3 1 1
                7 1 1 1 1 1 7 1 2 1 2 2 1 2 2 4 1 1 5 2 2
        7 2 1 7
      1 1 4 1 1
1 3 1 3 1 1 3 1
1 3 1 1 1 1 3 1
1 3 1 1 1 1 3 1
        1 1 1 1
      7 1 1 1 7
            1 1
      2 2 2 1 2
      2 1 1 1 1
  3 4 1 1 1 1 1
    1 3 1 4 2 1
      1 1 4 1 3
        3 1 2 1
      7 1 2 4 1
      1 1 1 1 3
1 3 1 1 2 2 2 1
    1 3 1 1 2 3
    1 3 1 2 3 3
    1 1 2 2 1 3
```

Note the apparition of a neat csv file named `./my-nono.csv` for easy excel and word integration!

## Sources

[Reddit - r/dailyprogrammer]( https://www.reddit.com/r/dailyprogrammer/comments/42lhem/20160125_challenge_251_easy_create_nonogram/)

[Reddit - TheBlackCat13]( https://www.reddit.com/user/TheBlackCat13/)

[PyPi - PyQRCode](https://pypi.org/project/PyQRCode/)
