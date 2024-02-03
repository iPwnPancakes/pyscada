export interface IModbusConfig {
    id: number;
    device_id: number;
    tag_id: number;
    protocol_id: number;
    protocol_name: 'Modbus';
    slave_id: number;
    register: number;
}
