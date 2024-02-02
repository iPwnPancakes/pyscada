import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class SidebarService {
    isOpen: BehaviorSubject<boolean>;

    constructor() {
        this.isOpen = new BehaviorSubject<boolean>(false);
    }

    open() {
        this.isOpen.next(true);
    }

    close() {
        this.isOpen.next(false);
    }
}
