# A simple IME for usage with the keyboard number pad.
# It allows to type texts using only the keyboard number pad in a style commonly found on older cell phones.

# This script contains the core logic. It should not executed directly,
# but instead executed on key press by the other NumpadIME_key_* scripts alongside this script.

# License: GPLv3+ (Gnu General Public License version 3 or (at your option) any later version)
# Copyright (C) 2018 Thomas Hess <thomas.hess@udo.edu>

import time

# (decimal, floating point) wait delay in seconds that needs to pass to start typing a new letter
new_key_delay=1

# The customizable key map.
# Note that this version follows the typical keyboard number pad layout, and thus is not fully equivalent to a typical cellphone.
# e.g. it contains "abc8" instead of the cellphone-default "abc2".
# Currently row ordering is in keyboard order from top to bottom, but re-ordering rows does not change the semantics.
key_map = {
    "7": " .,:;!?7", # First character is a space.
    "8": "abc8",
    "9": "def9",
    "4": "ghi4",
    "5": "jkl5",
    "6": "mno6",
    "1": "pqrs1",
    "2": "tuv2",
    "3": "wxyz3"
}

key = store.get_global_value("NumpadIME_key")

if key is not None:  # key is None if this is script invoked directly. Prevent script errors by skipping all further logic in this case
    prev_key = store.get_value("NumpadIME_previous_key")

    now = time.perf_counter()
    # Handle first keypress the same as a different keypress: If key not present, default to a time larger than the new_key_delay
    last_keypress = store.get("NumpadIME_time_last_keypress", now - 2 * new_key_delay)
    if last_keypress > now:
        # AutoKey keeps the store across restarts, but time.perf_counter looses it’s meaning across restarts,
        # So if the last keystroke looks like coming from the future, discard the stored time.
        last_keypress = 0
    store.set_value("NumpadIME_time_last_keypress", now)
    elapsed_time = now - last_keypress

    if key == prev_key and elapsed_time < new_key_delay:
        # Currently typing a letter, so cycle to the next choice.
        keyboard.send_keys("<backspace>")
        index = store.get("NumpadIME_key_index", 0)  # Default to 0 for the first ever pressed key
        # Use send_keys even for a single character, because it automatically generates neccessary modifier key presses for upper case letters.
        keyboard.send_keys(key_map[key][index])
        store.set_value("NumpadIME_key_index", (index+1) % len(key_map[key]))
    else:
        # Start typing a new character, because of a timeout or different key
        keyboard.send_keys(key_map[key][0])
        # Reset the index, to start at the second character of the key list, if possible
        store.set_value("NumpadIME_key_index", 1 if len(key_map[key]) > 1 else 0)
        
        store.set_value("NumpadIME_previous_key", key)
        
