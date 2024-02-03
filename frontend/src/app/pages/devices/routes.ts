import { Routes } from '@angular/router';
import { CreateDeviceComponent } from './create-device/create-device.component';
import { ListDevicesComponent } from './list-devices/list-devices.component';
import { devicesResolver } from './list-devices/devices.resolver';

export const routes: Routes = [
    { path: 'devices', component: ListDevicesComponent, resolve: { devices: devicesResolver } },
    { path: 'devices/create', component: CreateDeviceComponent }
];
