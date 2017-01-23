def calculate_tax(tax_input):
    
    
    MAX_0 = 1000.00
    MAX_10 = 10000.00
    MAX_15 = 20200.00
    MAX_20 = 30750.00
    MAX_25 = 50000.00

    TAX_0 = 0.00
    TAX_10 = 0.10
    TAX_15 = 0.15
    TAX_20 = 0.20
    TAX_25 = 0.25
    TAX_30 = 0.30  
     
    if not isinstance(tax_input, dict):
        
        raise ValueError('The provided input is not a dictionary')
             
    for income in tax_input.keys():
    
        if not (isinstance(tax_input[income], float) or isinstance(tax_input[income], int)):
        
            raise ValueError('Allow only numeric input')
            
        tax_block_0 = MAX_0 * TAX_0
        
        block_0 =  tax_input[income] * TAX_0
    
        tax_block_10 = (MAX_10 - MAX_0) * TAX_10
        
        block_10 = ( tax_input[income] - MAX_0) * TAX_10
    
        tax_block_15 = (MAX_15 - MAX_10) * TAX_15
        
        block_15= ( tax_input[income] - MAX_10) * TAX_15
    
        tax_block_20 = (MAX_20 - MAX_15) * TAX_20
        
        block_20= ( tax_input[income] - MAX_15) * TAX_20
    
        tax_block_25 = (MAX_25 - MAX_20) * TAX_25
        
        block_25 = ( tax_input[income] - MAX_20) * TAX_25
    
        block_30 = ( tax_input[income] - MAX_25) * TAX_30
            
        if tax_input[income] > MAX_25 :
        
            tax_input[income] = block_30 + tax_block_25 \
                                + tax_block_20 + tax_block_15 \
                                + tax_block_10 + tax_block_0

        elif (tax_input[income] > MAX_20 and tax_input[income] <= MAX_25) :

            tax_input[income] = block_25 + tax_block_20 \
                                + tax_block_15 + tax_block_10 \
                                + tax_block_0

        elif (tax_input[income] > MAX_15 and tax_input[income] <= MAX_20) :

            tax_input[income] = block_20 + tax_block_15 \
                                + tax_block_10 + tax_block_0 

        elif (tax_input[income] > MAX_10 and tax_input[income] <= MAX_15) :
    
            tax_input[income] = block_15 + tax_block_10 \
                                + tax_block_0

        elif (tax_input[income] > MAX_0 and tax_input[income] <= MAX_10) :

            tax_input[income] = block_10 + tax_block_0

        elif (tax_input[income] <= MAX_0) :
    
            tax_input[income] = block_0
                                 
    tax_input
    
    iops = open('/mnt/sdcard/org.qpython.qpy/tax_test.txt', 'w')
    #iops.write('%s \n' % tax_input )
    iops.write(str(tax_input) + '\n')
    iops.close()
    j = open('/mnt/sdcard/org.qpython.qpy/tax_test.txt')
    line = j.readline()
    print line
    line.rstrip()


t = {'q':233000,'s':403660,'ff':566000,'z':30}

calculate_tax(t)
