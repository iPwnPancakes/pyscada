import { Component, Input } from '@angular/core';
import { IModbusConfig } from '../../../../lib/ScadaApi/models/IModbusConfig';
import { MatCardModule } from '@angular/material/card';

@Component({
    selector: 'app-modbus-form',
    standalone: true,
    imports: [MatCardModule],
    templateUrl: './modbus-form.component.html',
    styleUrl: './modbus-form.component.scss'
})
export class ModbusFormComponent {
    @Input() public config!: IModbusConfig;
}
