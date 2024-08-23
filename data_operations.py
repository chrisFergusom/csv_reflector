# data_operations.py

from PyQt6.QtWidgets import QMessageBox
import pandas as pd
import numpy as np
from button_tracking import track_button_press
from file_operations import display_data_with_info

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

def apply_operation(gui, operation):
    if gui.df is None:
        QMessageBox.information(gui, "Info", "Please load a CSV file first.")
        return

    if not hasattr(gui, 'original_columns'):
        gui.original_dtypes = gui.df.dtypes.to_dict()
        gui.original_columns = gui.df.columns.tolist()
        gui.original_df = gui.df.copy()

    if operation == 'rotate':
        # Rotate column names and data 180 degrees
        column_row = pd.DataFrame([gui.df.columns.tolist()], columns=gui.df.columns)
        temp_df = pd.concat([column_row, gui.df], ignore_index=True)
        gui.df = temp_df.iloc[::-1, ::-1].reset_index(drop=True)
        new_columns = gui.df.iloc[0].tolist()
        gui.df = gui.df.iloc[1:]
        gui.df.columns = [str(col) for col in new_columns]
    elif operation == 'reflect':
        # Reflect columns and data
        gui.df = gui.df.iloc[:, ::-1]
        gui.df.columns = [str(col)[::-1] for col in gui.df.columns]
        gui.df = gui.df.astype(str).apply(lambda x: x.str[::-1])
    elif operation == 'flip':
        # Flip rows and set first row as new column names
        column_row = pd.DataFrame([gui.df.columns.tolist()], columns=gui.df.columns)
        gui.df = pd.concat([column_row, gui.df], ignore_index=True)
        gui.df = gui.df.iloc[::-1].reset_index(drop=True)
        gui.df.columns = [str(val) for val in gui.df.iloc[0]]
        gui.df = gui.df.iloc[1:].reset_index(drop=True)
    elif operation == 'random':
        # Randomly swap all data values and column names.
        all_values = gui.df.columns.tolist() + gui.df.values.flatten().tolist()
        np.random.shuffle(all_values)
        total_elements = len(all_values)
        new_cols = int(np.sqrt(total_elements))
        new_rows = total_elements // 
        reshaped_values = np.array(all_values[:new_rows * new_cols]).reshape(new_rows, new_cols)
        gui.df = pd.DataFrame(reshaped_values[1:], columns=reshaped_values[0])
    elif operation == 'restore':
        if gui.original_df is not None:
            gui.df = gui.original_df.copy()
        else:
            QMessageBox.information(gui, "Info", "No original data to restore.")
            return

    if is_original_state(gui):
        restore_original_dtypes(gui)

    display_data_with_info(gui)

def rotate_data(gui):
    track_button_press('Rotate', gui.button_log)
    apply_operation(gui, 'rotate')

def reflect_data(gui):
    track_button_press('Reflect', gui.button_log)
    apply_operation(gui, 'reflect')

def flip_data(gui):
    track_button_press('Flip', gui.button_log)
    apply_operation(gui, 'flip')

def random_data(gui):
    track_button_press('Random', gui.button_log)
    apply_operation(gui, 'random')

def restore_data(gui):
    track_button_press('Restore', gui.button_log)
    apply_operation(gui, 'restore')