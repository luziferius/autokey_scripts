# autokey_scripts
This repository holds some of my Python scripts for usage with autokey.
See https://github.com/autokey/autokey

## NumpadIME
This set of scripts lets you type texts using the keyboard number pad,
by emulating an old-style cellphone keyboard (without T9 functionality).
Use it if you go for maximum space saving and only connect a USB keypad.

This was requested in the https://gitter.im/autokey/autokey chat around May 15th, 2018.

## script_debug
The two scripts inside provide a breakpoint system for scripts.

### script_stepper
This script is meant to be executed by another script.
Usage inside the to-be stepped script: Place any number of `engine.run_script("script_stepper")` lines.
The script execution then pauses on each `engine.run_script("script_stepper")`.

### script_stepper_next_step
This script should be triggered by a free hotkey of your choice. If executed, it will un-pause a currently paused script and cause
it’s execution to continue to the next `engine.run_script("script_stepper")` line (if any).

### Example usage script
This script simply outputs some line of text. The breakpoints between each `keyboard.send_keys` causes it to pause between lines.
```
keyboard.send_keys("First line\n")
engine.run_script("script_stepper")
for number in range(2, 7):
    keyboard.send_keys("line {}\n".format(number))
    engine.run_script("script_stepper")
keyboard.send_keys("Last line\n")
```

