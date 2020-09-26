# brightness-tk

A Gui brightness controller on top of `xrandr`.


Python v2.7

## requirements:
* `Tkinter` python library
* `xrandr` a command link tool to change the brightness

## via command line
`python brighttk.py <monitor> <brightness percentage>` 

* `<monitor>`: The name/ID of your monitor/screen. If not passed, the application will try to fetch that from using `xrandr`.
* `<brightness percentage>`: The increase/decrease in the brightness percentage. For example to increase the brightness by 10%, use `0.1`. If you want to decrease the percentage by 20%, use `-0.2`. Not that `xrandr` may allow you to go beyond 100%.

## How to use it
Try to bind the script to the brightness buttons if you have them, or just choose any binding software. I am using it with MintLinux (Keyboard -> Shortcuts -> Add custome shortcut). You can the command for the brightness decrease as follows `python /home/localtion/brighttk.py -0.1` (make sure to adjust the location to make the directory of the app).

## Design
The design is pretty simple, rather not design. You can add images and different colors to make it much better. 

