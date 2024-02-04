import { Injectable, OnDestroy } from '@angular/core';
import { WebSocketSubject } from 'rxjs/internal/observable/dom/WebSocketSubject';
import { webSocket } from 'rxjs/webSocket';
import { environment } from '../../../../environments/environment';
import { Observable, Subject } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class TagValueUpdateListenerService implements OnDestroy {
    private websocket: WebSocketSubject<any> | null = null;
    private observable: Observable<number | string | boolean> | null = null;
    private subscribers: Subject<number | string | boolean>[] = [];

    public createListener(tagId: number): Subject<number | string | boolean> {
        if (!this.websocket) {
            const websocketRoom = `tag/${ tagId }/values`;
            this.websocket = webSocket(`${ environment.SCADA_WEBSOCKET_URL }/${ websocketRoom }`);
            this.observable = new Observable<number | string | boolean>();
        }

        const listener = new Subject<number | string | boolean>();

        this.websocket.subscribe(listener);
        this.subscribers.push(listener);

        return listener;
    }

    public ngOnDestroy(): void {
        console.log('unsubscribing');
        this.subscribers.forEach(sub => sub.unsubscribe());
    }
}
