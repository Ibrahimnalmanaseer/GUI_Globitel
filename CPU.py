def CPU_spec(app):

    core_16=16
    core_12=12
    core_8=8
    core_24=24
    core_32=32
    
    num_CPU_16=0
    num_CPU_12=0
    num_CPU_8=0
    num_CPU_24=0
    

    avg_call_time = (int(app.avg_call_time_var.get())/3600)/24
    expected_calls = int(app.expected_calls_var.get())

    total_hours = round(avg_call_time * expected_calls) if avg_call_time and expected_calls else 0

    total_cores_needed=total_hours*1.5

    
    with_dr = app.with_dr_var.get()


    number_CPU_32= round((total_cores_needed)//32)
    remaining_num_CPU= (total_cores_needed)%32


  
  

  

    while remaining_num_CPU > 0 :

        if remaining_num_CPU <core_32 and  remaining_num_CPU > core_24  :


            number_CPU_32 += 1
            remaining_num_CPU = 0            

        elif remaining_num_CPU <=core_24 and  remaining_num_CPU > core_16  :


            num_CPU_24 += 1
            remaining_num_CPU = 0 

        elif remaining_num_CPU <= core_16 and  remaining_num_CPU > core_12:


            num_CPU_16 += 1
            remaining_num_CPU=0

           

        elif remaining_num_CPU <=core_12 and  remaining_num_CPU > core_8:

            num_CPU_12 += 1
            remaining_num_CPU=0
            

        elif remaining_num_CPU <= core_8  :

            num_CPU_8 +=1
            remaining_num_CPU=0   

    

    

    message = f'''
    ----------------------------------------
              Analytics Server CPU
    ----------------------------------------
    Server Specifications:
    RAM: 16 GB
    SSD: 500
    OS: Ubuntu
    ----------------------------------------
    Total hours = {total_hours}
    Total Cores needed:{total_cores_needed}
    ========================================
    Total CPUs needed:
    Core_32:{number_CPU_32}
    Core_24:{num_CPU_24}
    Core_16:{num_CPU_16}
    Core_12:{num_CPU_12}
    Core_8 :{num_CPU_8}
    ========================================
    '''
    if with_dr :
        

      message+=f'''
    ========================================
    DR CPUs needed:
    Core_32:{number_CPU_32}
    Core_24:{num_CPU_24}
    Core_16:{num_CPU_16}
    Core_12:{num_CPU_12}
    Core_8 :{num_CPU_8}
    ========================================


    '''

    return message



       

