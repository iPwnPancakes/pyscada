export interface IMqttConfig {
    id: number;
    device_id: number;
    tag_id: number;
    protocol_id: number;
    protocol_name: 'MQTT';
    address: string;
}
