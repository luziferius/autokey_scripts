# Wait until an outside event occurs.
# This script waits until DEBUG_SCRIPT_NEXT_STEP global entry is set to something
# that evaluates to True.

import time
store.set_global_value("DEBUG_SCRIPT_RUNNING", True)

while not store.get_global_value("DEBUG_SCRIPT_NEXT_STEP"):
    time.sleep(0.1)

store.set_global_value("DEBUG_SCRIPT_NEXT_STEP", False)
store.set_global_value("DEBUG_SCRIPT_RUNNING", False)
