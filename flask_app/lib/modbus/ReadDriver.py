from pymodbus.client.tcp import ModbusTcpClient

from flask_app.models.Device import Device
from flask_app.models.ModbusConfig import ModbusConfig


class Read:
    def read(self, device: Device, modbus_config: ModbusConfig) -> int | float:
        network_config = device.network_config

        slave_id = modbus_config.slave_id
        register = modbus_config.register

        client = ModbusTcpClient(host=network_config.ip_address, port=network_config.port)

        response = client.read_holding_registers(slave=slave_id, address=register)

        client.close()

        if response.isError():
            raise response

        return response.registers[0]
