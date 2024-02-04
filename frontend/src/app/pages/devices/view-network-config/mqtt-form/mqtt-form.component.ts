import { Component, Input } from '@angular/core';
import { IMqttConfig } from '../../../../lib/ScadaApi/models/IMqttConfig';
import { MatCardModule } from '@angular/material/card';

@Component({
    selector: 'app-mqtt-form',
    standalone: true,
    imports: [MatCardModule],
    templateUrl: './mqtt-form.component.html',
    styleUrl: './mqtt-form.component.scss'
})
export class MqttFormComponent {
    @Input() public config!: IMqttConfig;
}
