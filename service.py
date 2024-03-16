import os

from GPU import GPU_spec
from CPU import CPU_spec
from RecordingServ import recording_servers
from Vendors import vendors_doc_provider
from reportlab.pdfgen import canvas

def generate_action_logic(app):



    selected_vendor = app.vendor_var.get()
    selected_device = app.device_var.get()
    selected_license_type = app.license_type_var.get()
    avg_call_time = app.avg_call_time_var.get()
    expected_calls = app.expected_calls_var.get()
    num_agents = app.agents_var.get()
    num_extensions = app.extensions_var.get()
    

    # Check if analytics checkbox is selected
    analytics_required = app.analytics_var.get()
    # Check if DR checkbox is selected
    with_dr = app.with_dr_var.get()
    # Check if DR Backup checkbox is selected
    with_backup = app.with_backup_var.get()

   

    # Log the output to a file
    log_directory = "C:/traces"
    os.makedirs(log_directory, exist_ok=True)
    log_path = os.path.join(log_directory, "generation_log.txt")
    # pdf_path = os.path.join(log_directory, "generation_log.pdf")
    # Initialize analytics_option outside of the if block
    analytics_option = None
   
    specs_message=''
    with open(log_path, "w") as log_file:


        log_file.write(f'''
    -----------------------------------  
                 Input 
    -----------------------------------                                
    Selected Vendor: {selected_vendor}
    Selected Device: {selected_device}
    Selected License Type: {selected_license_type}
    Average Call Time: {avg_call_time}
    Expected Calls: {expected_calls}
    Number of Agents: {num_agents}
    Number of Extensions: {num_extensions}
    Analytics Required: {'Yes' if analytics_required else 'No'}
    With DR: {'Yes' if with_dr else 'No'}
    With Central Web: {'Yes' if with_backup else 'No'}
    -----------------------------------    
        ''')
        log_file.write(f"{vendors_doc_provider(app)}\n")
        
        log_file.write(f"{recording_servers(app)}\n")       

        if analytics_required:

            analytics_option = app.analytics_option_var.get()

            if analytics_option == "GPU":
                specs_message += GPU_spec(app,specs_message)

            else:

                specs_message += CPU_spec(app)


    

        log_file.write(f"{specs_message}\n")

    # with open(log_path, "r") as log_file:
    #     pdf_canvas = canvas.Canvas(pdf_path)
    #     y_coordinate = 800  # Initial Y coordinate
    #     for line in log_file:
    #         pdf_canvas.drawString(10, y_coordinate, line.strip())  # Adjust the coordinates as needed
    #         y_coordinate -= 12  # Adjust the spacing between lines
    #     pdf_canvas.save()

    print(f"Log generated at: {log_path}")
    # print(f"PDF generated at: {pdf_path}")


    

