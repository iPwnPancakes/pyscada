import { Component } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { IDevice } from '../../../lib/ScadaApi/models/IDevice';
import { MatTableModule } from '@angular/material/table';
import { MatCardModule } from '@angular/material/card';

@Component({
    selector: 'app-view-device',
    standalone: true,
    imports: [MatTableModule, MatCardModule, RouterLink],
    templateUrl: './view-device.component.html',
    styleUrl: './view-device.component.scss'
})
export class ViewDeviceComponent {
    public device!: IDevice;
    public tagDisplayColumns: string[] = ['id', 'name', 'value', 'configs'];

    constructor(private route: ActivatedRoute) {}

    ngOnInit() {
        this.route.data.subscribe({
            next: (data) => {
                this.device = data['device'] ?? null;
            }
        });
    }
}
