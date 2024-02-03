import { IDeviceNetworkConfig } from './IDeviceNetworkConfig';
import { ITag } from './ITag';

export interface IDevice {
    id: number;
    name: string;
    network_config: IDeviceNetworkConfig | null;
    tags: ITag[];
}
