from pymodbus.client.tcp import ModbusTcpClient

from flask_app.models.Device import Device
from flask_app.models.ModbusConfig import ModbusConfig


def write_modbus(device: Device, modbus_config: ModbusConfig, value: int | float) -> None:
    network_config = device.network_config

    slave_id = modbus_config.slave_id
    register = modbus_config.register

    client = ModbusTcpClient(host=network_config.ip_address, port=network_config.port)

    response = client.write_register(slave=slave_id, address=register, value=value)

    client.close()

    if response.isError():
        raise response
