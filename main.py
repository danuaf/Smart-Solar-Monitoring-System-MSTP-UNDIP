from time import sleep
from controller.db_controller import DbController
from controller.modbus_controller import ModbusController
import random # untuk testing pengganti nilai sensor

if __name__ == "__main__":
    db_path = "database/tesdata1.db" 
    db_controller = DbController(db_path)

    devices = {
        "Pyranometer": {
            "slave_address": 12,
            "registers": {
                "UV_Radiation": {"address": 123, "decimals": 2}
            }
        },
        "RTD": {
            "slave_address": 11, "registers": {
                "Temperature": {"address": 0, "decimals": 1}
            }
        },
        "Dissolve_Oxygen": {
            "slave_address": 2, "registers": {
                "Dissolve_Oxygen": {"address": 0, "decimals": 0}
            }
        },
        "Inventer_SRNE": {
            "slave_address": 1, "registers": {
                "Load_Active_Power": {"address": 539, "decimals": 0},
                "Battery_Level": {"address": 256, "decimals": 0},
                "Battery_Voltage": {"address": 257, "decimals": 1},
                "PV_Voltage": {"address": 263, "decimals": 1},
                "PV_Current": {"address": 264, "decimals": 1},
                "PV_Power": {"address": 265, "decimals": 0},
                "Charge_Power": {"address": 270, "decimals": 0},
                "Battery_Charge_State": {"address": 267, "decimals": 0},
                "Machine_State": {"address": 528, "decimals": 0},
                "Inverter_Current": {"address": 537, "decimals": 1},
                "Main_Charge_Current": {"address": 542, "decimals": 1},
                "PV_Change_Current": {"address": 548, "decimals": 1},
                "PV_Daily_Consumption": {"address": 61487, "decimals": 1},
                "Battery_Charge_Daily": {"address": 61485, "decimals": 1},
                "Battery_Discharge_Daily": {"address": 61486, "decimals": 1},
                "Load_Daily_Consumption": {"address": 61485, "decimals": 1},
                "Uptime": {"address": 61485, "decimals": 0},
                "PV_Generated": {"address": 61496, "decimals": 1},
                "Main_Load_Power_Daily": {"address": 61501, "decimals": 1},
                "DCDC_Temperature": {"address": 544, "decimals": 1},
                "DCAC_Temperature": {"address": 545, "decimals": 1},
                "Translator_Temperature": {"address": 546, "decimals": 1},
                "Load_Percentage": {"address": 543, "decimals": 0}
            }
        },
        "VFD_NFlixin": {
            "slave_address": 9, "registers": {
                "Running_Frequency": {"address": 28672, "decimals": 2},
                "Output_Voltage": {"address": 28675, "decimals": 0},
                "Output_Current": {"address": 28676, "decimals": 2}
            }
        }
    }

    # Buat Table Perangakt dan Parameter di SQLite
    for device_name, device_info in devices.items():
        register_names = list(device_info["registers"].keys())
        db_controller.create_table(device_name, register_names)

    while True :
        # Baca dan Kirim data ke SQLite
        for device_name, device_info in devices.items():
            data_to_insert = {}

            for register_name, register_info in device_info["registers"].items():
                address = register_info["address"]
                decimals = register_info["decimals"]

                register_value = random.randint(1,100) # Untuk testing pengganti nilai sensor
                # register_value = ModbusController().read_register(address, decimals)

                if register_value is not None:
                    data_to_insert[register_name] = register_value

            if data_to_insert:
                db_controller.insert_data(device_name, data_to_insert)

        # Interval 3 Detik
        sleep(3)
