


def recording_servers(app):
    


    message=''
    num_extensions = app.extensions_var.get()
    num_extensions_int = int(num_extensions) if num_extensions.isdigit() else 0
    with_backup = app.with_backup_var.get()

    num_servers = (num_extensions_int + 399) // 400  # Calculate the number of servers needed 
    with_dr = app.with_dr_var.get()
    central_web_needed=1

    if with_dr :
       

       
       message += f'''
    ----------------------------------------
                Recorder Server
    ----------------------------------------    
    Server Specifications:
    CPU: 12 cores 2.4 GHz
    RAM: 12 GB
    C Drive: 150 GB
    D Drive: 300 GB
    Operating System: Windows Server 2022 Standard
    SQL Server: SQL Server 2022 or 2019 Standard (extra 200 GB space on D if locally)
    Network Drive: 1 Giga Ethernet
    ========================================
    Recording_Servers needed: {num_servers}
    ========================================
    DR Servers needed: {num_servers}
    ========================================
    '''
        
     

    elif not with_dr:
      message += f'''
    ----------------------------------------
                Recorder Server
    ----------------------------------------    
    Server Specifications:
    CPU: 12 cores 2.4 GHz
    RAM: 12 GB
    C Drive: 150 GB
    D Drive: 300 GB
    Operating System: Windows Server 2022 Standard
    SQL Server: SQL Server 2022 or 2019 Standard (extra 200 GB space on D if locally)
    Network Drive: 1 Giga Ethernet
    ========================================
    Recording_Servers needed: {num_servers}
    ========================================
    '''

  

      
    if with_backup :
       
      if with_dr :
          
          message += f'''  

    ----------------------------------------
                Web Central Server
    ----------------------------------------    
    Server Specifications:
    CPU: 12 cores 2.4 GHz
    RAM: 12 GB
    C Drive: 150 GB
    D Drive: 300 GB
    Operating System: Windows Server 2022 Standard
    SQL Server: SQL Server 2022 or 2019 Standard (extra 200 GB space on D if locally)
    Network Drive: 1 Giga Ethernet  
    ========================================
    Central Web needed: {central_web_needed}
    ========================================
    DR Central Web needed: {central_web_needed}
    ========================================
      '''
    elif not with_dr:
      message += f'''  

    ----------------------------------------
                Web Central Server
    ----------------------------------------    
    Server Specifications:
    CPU: 12 cores 2.4 GHz
    RAM: 12 GB
    C Drive: 150 GB
    D Drive: 300 GB
    Operating System: Windows Server 2022 Standard
    SQL Server: SQL Server 2022 or 2019 Standard (extra 200 GB space on D if locally)
    Network Drive: 1 Giga Ethernet  
    ========================================
    Central Web needed: {central_web_needed}
    ========================================
      '''
       
    
    return message

      
  


  



            
    
           

    