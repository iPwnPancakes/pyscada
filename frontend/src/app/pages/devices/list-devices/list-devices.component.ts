import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { IDevice } from '../../../lib/ScadaApi/IDevice';

@Component({
    selector: 'app-list-devices',
    standalone: true,
    imports: [],
    templateUrl: './list-devices.component.html',
    styleUrl: './list-devices.component.scss'
})
export class ListDevicesComponent {
    public devices: IDevice[] = [];

    constructor(private activatedRoute: ActivatedRoute) {}

    ngOnInit() {
        this.activatedRoute.data.subscribe({
            next: (data) => {
                this.devices = data['devices'] ?? [];
            }
        });
    }
}
