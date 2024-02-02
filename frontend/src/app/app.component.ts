import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { WithSidebarComponent } from './layouts/with-sidebar/with-sidebar.component';
import { NavbarComponent } from './core/navbar/navbar.component';
import { SidebarService } from './layouts/with-sidebar/sidebar.service';
import { DevicesModule } from './pages/devices/devices.module';

@Component({
    selector: 'app-root',
    standalone: true,
    imports: [
        RouterOutlet,
        WithSidebarComponent,
        NavbarComponent,
        DevicesModule
    ],
    templateUrl: './app.component.html'
})
export class AppComponent {
    constructor(private sidebarService: SidebarService) {
    }

    onMenuButtonClick() {
        this.sidebarService.open();
    }
}
