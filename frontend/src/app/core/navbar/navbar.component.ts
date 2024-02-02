import { Component, EventEmitter, Output } from '@angular/core';
import { MatToolbar } from '@angular/material/toolbar';
import { MatIcon } from '@angular/material/icon';
import { MatIconButton } from '@angular/material/button';

@Component({
    selector: 'app-navbar',
    standalone: true,
    imports: [
        MatToolbar,
        MatIcon,
        MatIconButton
    ],
    templateUrl: './navbar.component.html',
})
export class NavbarComponent {
    @Output() menuButtonClicked = new EventEmitter<void>();
}
