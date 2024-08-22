from PyQt6.QtWidgets import QFileDialog, QMessageBox
import pandas as pd
from button_tracking import track_button_press

def load_file(gui):
    track_button_press('Load', gui.button_log)
    file_path, file_type = QFileDialog.getOpenFileName(gui, "Open File", "", "CSV Files (*.csv);;Excel Files (*.xlsx);;JSON Files (*.json)")
    if file_path:
        try:
            if file_type.startswith('CSV'):
                gui.df = pd.read_csv(file_path)
            elif file_type.startswith('Excel'):
                gui.df = pd.read_excel(file_path)
            elif file_type.startswith('JSON'):
                gui.df = load_json(file_path)
            display_data_with_info(gui)
        except Exception as e:
            QMessageBox.critical(gui, "Error", f"Failed to load file: {str(e)}")

def load_json(file_path):
    df = pd.read_json(file_path)
    if df.empty or not isinstance(df, pd.DataFrame):
        raise ValueError("The JSON file is not valid for DataFrame loading.")
    return df

def save_file(gui):
    track_button_press('Save', gui.button_log)
    file_path, file_type = QFileDialog.getSaveFileName(gui, "Save File", "", "CSV Files (*.csv);;Excel Files (*.xlsx);;JSON Files (*.json)")
    if file_path:
        try:
            if file_type.startswith('CSV'):
                gui.df.to_csv(file_path, index=False)
            elif file_type.startswith('Excel'):
                gui.df.to_excel(file_path, index=False)
            elif file_type.startswith('JSON'):
                gui.df.to_json(file_path, orient='records')
            QMessageBox.information(gui, "Success", "File saved successfully")
        except Exception as e:
            QMessageBox.critical(gui, "Error", f"Failed to save file: {str(e)}")

def display_data_with_info(gui):
    gui.text_widget.clear()
    if gui.df is not None:
        markdown_table = gui.df.head(20).to_markdown(index=False)
        gui.text_widget.append(markdown_table)
        gui.text_widget.append("\nDataFrame Info:")
        gui.text_widget.append(f"Shape: {gui.df.shape}")
        gui.text_widget.append(f"Columns: {', '.join(gui.df.columns)}")
        gui.text_widget.append(f"Data Types:\n{gui.df.dtypes.to_string()}")