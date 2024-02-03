import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { IDevice } from '../../../lib/ScadaApi/models/IDevice';

@Component({
    selector: 'app-view-device',
    standalone: true,
    imports: [],
    templateUrl: './view-device.component.html',
    styleUrl: './view-device.component.scss'
})
export class ViewDeviceComponent {
    public device!: IDevice;

    constructor(private route: ActivatedRoute) {}

    ngOnInit() {
        this.route.data.subscribe({
            next: (data) => {
                this.device = data['device'] ?? null;
            }
        });
    }
}
