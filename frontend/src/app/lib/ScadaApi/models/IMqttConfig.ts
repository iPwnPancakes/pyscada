import { IDeviceTagConfig } from './IDeviceTagConfig';

export interface IMqttConfig extends IDeviceTagConfig {
    protocol_name: 'MQTT';
    address: string;
}
