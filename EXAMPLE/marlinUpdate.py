# Variables custom para Configuration.h
dic_Var_Custom_Configuration = [
    '#define STRING_CONFIG_H_AUTHOR "(MR. V, CUSTOM FW)"',
    '#define CUSTOM_MACHINE_NAME "IAN MK1"',
    '#define PIDTEMPBED',
    '#define PROBE_MANUALLY',
    '#define MANUAL_PROBE_START_Z 0.2',
    '#define LCD_BED_LEVELING',
    '#define EEPROM_SETTINGS',
    '#define NOZZLE_PARK_FEATURE',
    '#define LCD_LANGUAGE es',
    '#define SDSUPPORT',
    '#define PID_EDIT_MENU',
    '#define PID_AUTOTUNE_MENU',
    '#define PROBE_MANUALLY',
    '#define MESH_BED_LEVELING',
    '#define PIDTEMPBED'
    '#define HEATER_0_MINTEMP   0',
    '#define BED_MINTEMP        0',

]
# Variables default para Configuration.h
dic_Var_default_Configuration = [
    '#define STRING_CONFIG_H_AUTHOR "(none, default config)"',
    '//#define CUSTOM_MACHINE_NAME "3D Printer"',
    '//#define PIDTEMPBED',
    '//#define PROBE_MANUALLY',
    '//#define MANUAL_PROBE_START_Z 0.2',
    '//#define LCD_BED_LEVELING',
    '//#define EEPROM_SETTINGS',
    '//#define NOZZLE_PARK_FEATURE',
    '#define LCD_LANGUAGE en',
    '//#define SDSUPPORT',
    '//#define PID_EDIT_MENU',
    '//#define PID_AUTOTUNE_MENU',
    '//#define PROBE_MANUALLY',
    '//#define MESH_BED_LEVELING',
    '//#define PIDTEMPBED'
    '#define HEATER_0_MINTEMP   5',
    '#define BED_MINTEMP        5',
]
# Variables custom Configuration_adv.h
dic_Var_Custom_Configuration_ADV = [
    '#define BACKLASH_COMPENSATION',
    '#define ADAPTIVE_STEP_SMOOTHING',
    '#define STATUS_MESSAGE_SCROLLING',
    '#define ADVANCED_PAUSE_FEATURE',
    '#define ADAPTIVE_STEP_SMOOTHING',
    '#define LCD_INFO_MENU',
    '#define STATUS_MESSAGE_SCROLLING',
    '#define SCROLL_LONG_FILENAMES',
    '#define LONG_FILENAME_HOST_SUPPORT',
    '#define ADVANCED_PAUSE_FEATURE'
]

# Variables default para Configuration_adv.h
# NOTA: el nombre y valor puede variar en versiones posteriores del FW
#
dic_Var_default_Configuration_ADV = [
    '//#define BACKLASH_COMPENSATION',
    '//#define ADAPTIVE_STEP_SMOOTHING',
    '//#define STATUS_MESSAGE_SCROLLING',
    '//#define ADVANCED_PAUSE_FEATURE',
    '//#define ADAPTIVE_STEP_SMOOTHING',
    '//#define LCD_INFO_MENU',
    '//#define STATUS_MESSAGE_SCROLLING',
    '//#define SCROLL_LONG_FILENAMES',
    '//#define LONG_FILENAME_HOST_SUPPORT',
    '//#define ADVANCED_PAUSE_FEATURE'
]

# Contador de variables Configuration.h
cant_var_custom = len(dic_Var_Custom_Configuration)
cant_var_default = len(dic_Var_default_Configuration)

# Contador de variables Configuration_adv.h
cant_var_custom_adv = len(dic_Var_Custom_Configuration_ADV)
cant_var_default_adv = len(dic_Var_default_Configuration_ADV)

def reemplazarValorVariable(valor_default, valor_custom, tipo_Archivo):

    directorio = tipo_Archivo

    archivo = open(directorio, "r", encoding="utf-8")

    if valor_default != valor_custom:

        print(valor_default + " | " + valor_custom)

        texto = archivo.read()

        texto = texto.replace(valor_default, valor_custom)

        archivo = open(directorio, "w", encoding="utf-8")

        archivo.write(texto)

        archivo.close

        print("variable actualizada exitosamente")

    elif valor_custom == valor_default:

        print("los valores son identicos")

        archivo.close


if cant_var_custom != cant_var_default and cant_var_custom_adv != cant_var_default:

    print("la cantidad de variables custom y default son diferentes")

elif cant_var_custom == cant_var_default:

    print("todo bien")

    configuation_H = 'Configuration.h'

    print("modificando: " + configuation_H)

    for dic_Var_default_Configuration, dic_Var_Custom_Configuration in zip(dic_Var_default_Configuration, dic_Var_Custom_Configuration):

        reemplazarValorVariable(dic_Var_default_Configuration, dic_Var_Custom_Configuration, configuation_H)

    configuration_adv_H = 'Configuration_adv.h'

    print("modificando: " + configuration_adv_H)
    for dic_Var_default_Configuration_ADV, dic_Var_Custom_Configuration_ADV in zip(dic_Var_default_Configuration_ADV, dic_Var_Custom_Configuration_ADV):

        reemplazarValorVariable(dic_Var_default_Configuration_ADV, dic_Var_Custom_Configuration_ADV, configuration_adv_H)

