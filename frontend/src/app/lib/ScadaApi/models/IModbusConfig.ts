import { IDeviceTagConfig } from './IDeviceTagConfig';

export interface IModbusConfig extends IDeviceTagConfig {
    protocol_name: 'Modbus';
    slave_id: number;
    register: number;
}
