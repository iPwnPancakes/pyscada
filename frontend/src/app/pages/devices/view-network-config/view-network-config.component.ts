import { Component } from '@angular/core';
import { IMqttConfig } from '../../../lib/ScadaApi/models/IMqttConfig';
import { IModbusConfig } from '../../../lib/ScadaApi/models/IModbusConfig';
import { ActivatedRoute } from '@angular/router';
import { MqttFormComponent } from './mqtt-form/mqtt-form.component';
import { ModbusFormComponent } from './modbus-form/modbus-form.component';

@Component({
    selector: 'app-view-network-config',
    standalone: true,
    imports: [
        MqttFormComponent,
        ModbusFormComponent
    ],
    templateUrl: './view-network-config.component.html',
    styleUrl: './view-network-config.component.scss'
})
export class ViewNetworkConfigComponent {
    public config!: IMqttConfig | IModbusConfig;

    constructor(private readonly route: ActivatedRoute) {
    }

    ngOnInit(): void {
        this.route.data.subscribe((data) => {
            this.config = data['config'];
        });
    }
}
