import { Injectable, OnDestroy } from '@angular/core';
import { environment } from '../../../../environments/environment';
import { Observable, Subject } from 'rxjs';
import { io, Socket } from 'socket.io-client';

@Injectable({
    providedIn: 'root'
})
export class TagValueUpdateListenerService implements OnDestroy {
    private websocket!: Socket;
    private subscribers: Subject<number | string | boolean>[] = [];

    constructor() {
        this.websocket = io(`${ environment.SCADA_WEBSOCKET_URL }`);
    }


    public createListener(tagId: number): Subject<number | string | boolean> {
        this.websocket = io(`${ environment.SCADA_WEBSOCKET_URL }`);
        this.websocket.connect();
        this.websocket.on('connect', () => {
            this.websocket.emit('join', { room: `tag/${ tagId }/values` });
        });

        const listener = new Subject<number | string | boolean>();

        this.subscribers.push(listener);

        return listener;
    }

    public ngOnDestroy(): void {
        console.log('unsubscribing');
        this.subscribers.forEach(sub => sub.unsubscribe());
    }
}
