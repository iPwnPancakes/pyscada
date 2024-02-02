import { Component } from '@angular/core';
import { MatFormField, MatLabel } from '@angular/material/form-field';
import { MatInput } from '@angular/material/input';
import { MatButton } from '@angular/material/button';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';

@Component({
    selector: 'app-create-device',
    standalone: true,
    imports: [MatFormField, MatLabel, MatInput, MatButton, ReactiveFormsModule],
    templateUrl: './create-device.component.html',
    styleUrl: './create-device.component.scss'
})
export class CreateDeviceComponent {
    createDeviceForm: FormGroup = new FormGroup({
        name: new FormControl('')
    });

    public onSubmit(): void {
        console.log(this.createDeviceForm);
    }
}
