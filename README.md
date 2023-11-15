# UniversalFirmwareRefactor

## ENGLISH

### Universal firmware refactor is a tool for custom firmwares, replace easily your custom parameters between versions without change one by one and do it in just SECONDS

## Español

### El universal firmware refactor es una herramienta para firmwares personalizados, reemplace fácilmente sus parámetros personalizados entre versiones sin cambiar uno por uno y hágalo en solo SEGUNDOS

## Example
### STEP 1

first you have to copy default name and value of your firmware and paste it in <b>dic_Var_default_Configuration</b>, on this example we are going to use marlin for a 3D printer

<code>

    dic_Var_default_Configuration[
       'variable=value'
    
</code>

### STEP 2 

Now you have to write your custom values of your firmware and paste it in <b>dic_Var_Custom_Configuration</b>


<code>

    dic_Var_default_Configuration[
        'variable=custom value'    

</code>

#### note: the variables may vary on firmware programming language

### STEP 3 

In the file you put the directory and name of the file <b>WITH HIS EXTENSION </b>

<code>

    file = '*insert name of the file here*'

</code>

### STEP 4 

save and run 

<code>py .\universal_FW_refactor.py</code>