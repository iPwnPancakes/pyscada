import { IMqttConfig } from './IMqttConfig';
import { IModbusConfig } from './IModbusConfig';

export interface ITag {
    id: number;
    name: string;
    device_id: number;
    value_bool: boolean | null;
    value_int: number | null;
    value_float: number | null;
    value_string: string | null;
    device_configs: IMqttConfig[] | IModbusConfig[];
}
