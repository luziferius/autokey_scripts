# Execute the next step in currently debugged script

if store.get_global_value("DEBUG_SCRIPT_RUNNING"):
    # Only set this, if a script is currently stopped
    store.set_global_value("DEBUG_SCRIPT_NEXT_STEP", True)