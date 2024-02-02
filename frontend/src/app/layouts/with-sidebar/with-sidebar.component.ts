import { Component } from '@angular/core';
import { MatSidenav, MatSidenavContainer, MatSidenavContent } from '@angular/material/sidenav';
import { SidebarService } from './sidebar.service';

@Component({
    selector: 'app-with-sidebar',
    standalone: true,
    imports: [
        MatSidenav,
        MatSidenavContainer,
        MatSidenavContent
    ],
    templateUrl: './with-sidebar.component.html',
    styleUrl: './with-sidebar.component.scss'
})
export class WithSidebarComponent {
    isOpen: boolean = false;

    constructor(private sidebarService: SidebarService) {
        sidebarService.isOpen.subscribe(isOpen => this.isOpen = isOpen);
    }

    onCloseEvent() {
        this.sidebarService.close();
    }
}
