# data_operations.py

def try_cast_boolean(value):
    value = str(value).lower().strip()
    if value in ['true', '1', '1.0']: return True
    if value in ['false', '0', '0.0']: return False
    return None

def is_original_state(gui):
    return hasattr(gui, 'original_columns') and gui.df.columns.tolist() == gui.original_columns

def restore_original_dtypes(gui):
    if hasattr(gui, 'original_dtypes'):
        for col, dtype in gui.original_dtypes.items():
            if col in gui.df.columns:
                try:
                    if dtype == bool:
                        gui.df[col] = gui.df[col].apply(try_cast_boolean)
                    else:
                        gui.df[col] = gui.df[col].astype(dtype)
                except Exception:
                    pass  # If conversion fails, keep the current type