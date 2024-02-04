import { Component } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { IDevice } from '../../../lib/ScadaApi/models/IDevice';
import { MatTableModule } from '@angular/material/table';
import { MatCardModule } from '@angular/material/card';
import { TagValueUpdateListenerService } from './tag-value-update-listener.service';
import { ITag } from '../../../lib/ScadaApi/models/ITag';

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

    constructor(private route: ActivatedRoute, private wsListener: TagValueUpdateListenerService) {}

    ngOnInit() {
        this.route.data.subscribe({
            next: (data) => {
                this.device = data['device'] ?? null;
                this.device.tags.forEach(tag => {
                    let listener = this.wsListener.createListener(tag.id);

                    listener.subscribe({
                        next: value => this.onNewTagValue(tag, value),
                        error: err => {
                            console.error(err);
                        }
                    });
                });
            }
        });
    }

    private onNewTagValue(tag: ITag, value: number | string | boolean): void {
        this.device.tags = this.device.tags.map(currentTag => {
            if (currentTag.id === tag.id) {
                currentTag.value_int = Number(value);
            }

            return currentTag;
        })

        console.log(`New value for tag ${ tag.name }: ${ value }`);
    }
}
