import { Routes } from '@angular/router';
import { CreateDeviceComponent } from './create-device/create-device.component';
import { ListDevicesComponent } from './list-devices/list-devices.component';
import { devicesResolver } from './list-devices/devices.resolver';
import { ViewDeviceComponent } from './view-device/view-device.component';
import { deviceResolver } from './view-device/device.resolver';
import { ViewNetworkConfigComponent } from './view-network-config/view-network-config.component';
import { configResolver } from './view-network-config/config.resolver';

export const routes: Routes = [
    { path: 'devices', component: ListDevicesComponent, resolve: { devices: devicesResolver } },
    { path: 'devices/create', component: CreateDeviceComponent },
    { path: 'devices/:id', component: ViewDeviceComponent, resolve: { device: deviceResolver } },
    {
        path: 'devices/:device_id/tags/:tag_id/config/:config_id',
        component: ViewNetworkConfigComponent,
        resolve: { config: configResolver }
    }
];
