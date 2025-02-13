import dearpygui.dearpygui as dpg

# -------------------------
# Callback stubs
# -------------------------

def upload_file_callback(sender, app_data):
    """
    Called when user selects a file.
    Sets a label to show the file chosen.
    """
    dpg.set_value("file_label", f"File: {app_data['file_name']} Successfully Uploaded")

def populate_graphs_callback():
    """
    Called when user clicks 'Populate Graphs and Load Camera Feed'.
    In a real app, you would load data from the uploaded file,
    parse it, and fill in the plot series and any camera/video feed.
    """
    # For demonstration, just show some dummy lines on the plots
    dpg.set_item_label("thrust_series", "Thrust Data")
    dpg.set_item_label("pressure_series", "Pressure Data")
    
    # Thrust data (time vs thrust)
    time_data     = [0, 1, 2, 3, 4, 5]
    thrust_values = [0, 1000, 1800, 2000, 1950, 1500]
    dpg.set_value("thrust_series", [time_data, thrust_values])
    
    # Pressure data (time vs pressure)
    pressure_values = [100, 500, 650, 800, 830, 700]
    dpg.set_value("pressure_series", [time_data, pressure_values])
    
    # You could also update the “average thrust,” etc. labels here.

def exit_callback():
    """
    Called when 'Exit' is clicked in the top bar.
    """
    dpg.stop_dearpygui()


# -------------------------
# Building the UI
# -------------------------

def build_ui():
    """
    Build the entire UI layout inside the primary window.
    """
    # Main menu bar across the top
    with dpg.menu_bar():
        # Just top-level items for simplicity
        dpg.add_menu_item(label="File Upload", callback=lambda: dpg.configure_item("file_dialog_id", show=True))
        dpg.add_menu_item(label="Download")
        dpg.add_menu_item(label="About")
        dpg.add_menu_item(label="Help")
        dpg.add_menu_item(label="Exit", callback=exit_callback)
    
    # Title banner
    dpg.add_text("FreakAlyze")
    dpg.add_spacer(height=5)
    
    # Separate into two main sections horizontally: left panel and right panel
    with dpg.group(horizontal=True):
        
        # Left Panel
        with dpg.child_window(width=300, autosize_y=True):
            # Placeholder for "Choose a file or drag it here"
            dpg.add_text("Choose a file or drag it here", wrap=250)
            
            # Show the name of the file once loaded
            dpg.add_text("", tag="file_label")
            
            # Button that triggers graph/camera loading
            dpg.add_button(label="Populate Graphs and Load Camera Feed", callback=populate_graphs_callback)
        
        # Right Panel
        with dpg.group():
            
            # Plots/Results section
            with dpg.child_window(width=-1, height=350):
                # Thrust Plot
                with dpg.plot(label="Thrust Data", height=160, width=-1):
                    dpg.add_plot_axis(dpg.mvXAxis, label="Time (s)", tag="x_axis_thrust")
                    with dpg.plot_axis(dpg.mvYAxis, label="Thrust (N)", tag="y_axis_thrust"):
                        # We'll add an empty series here and populate it later
                        dpg.add_line_series([], [], label="Thrust Data", tag="thrust_series")
                
                # Pressure Plot
                with dpg.plot(label="Pressure Data", height=160, width=-1):
                    dpg.add_plot_axis(dpg.mvXAxis, label="Time (s)", tag="x_axis_pressure")
                    with dpg.plot_axis(dpg.mvYAxis, label="Pressure (PSI)", tag="y_axis_pressure"):
                        # We'll add an empty series here and populate it later
                        dpg.add_line_series([], [], label="Pressure Data", tag="pressure_series")
            
            # Key stats at the bottom
            with dpg.child_window(width=-1, height=80):
                dpg.add_text("Average Thrust: 1,800.70 N")
                dpg.add_text("Max Thrust: 2,857.59 N")
                dpg.add_text("Average Pressure: 549.67 PSI")
                dpg.add_text("Max Pressure: 829.81 PSI")
                dpg.add_text("Motor Designation: M1801")
                dpg.add_text("Burn Time: 5.56 s")
                dpg.add_text("Total Impulse: 10064.17 Ns")
    
    dpg.add_spacer(height=10)
    
    # "Rocket Test Video" section
    dpg.add_separator()
    dpg.add_text("Rocket Test Video", color=(255, 140, 0))
    
    # A child window to hold a mock video thumbnail or camera feed
    with dpg.child_window(width=-1, height=200):
        # For demonstration, we just show a button with some text or a placeholder image
        dpg.add_button(label="Play Video (Placeholder)")

# -------------------------
# Main script
# -------------------------

if __name__ == "__main__":
    dpg.create_context()
    dpg.create_viewport(title="FreakAlyze", width=1000, height=700)
    dpg.setup_dearpygui()
    
    # Primary Window (no title bar so we can simulate a “custom” top bar)
    with dpg.window(tag="Primary Window", label="", no_title_bar=True,
                    width=1000, height=700, pos=(0, 0)):
        build_ui()
    
    # File Dialog (hidden until opened)
    with dpg.file_dialog(directory_selector=False, show=False, callback=upload_file_callback, tag="file_dialog_id"):
        dpg.add_file_extension(".*")  # allow any file
    
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
