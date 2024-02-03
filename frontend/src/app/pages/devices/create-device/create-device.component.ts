import { Component } from '@angular/core';
import { MatError, MatFormField, MatLabel } from '@angular/material/form-field';
import { MatInput } from '@angular/material/input';
import { MatButton } from '@angular/material/button';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatDivider } from '@angular/material/divider';
import { Router } from '@angular/router';
import { ScadaApiService } from '../../../lib/ScadaApi/scada-api.service';

@Component({
    selector: 'app-create-device',
    standalone: true,
    imports: [MatFormField, MatLabel, MatInput, MatButton, ReactiveFormsModule, MatError, MatDivider],
    templateUrl: './create-device.component.html',
    styleUrl: './create-device.component.scss'
})
export class CreateDeviceComponent {
    createDeviceForm: FormGroup = new FormGroup({
        name: new FormControl<string>('', [Validators.required, Validators.minLength(3)])
    });

    constructor(private router: Router, private scadaApi: ScadaApiService) {
    }

    public onSubmit(): void {
        if (this.createDeviceForm.invalid) {
            return;
        }

        this.scadaApi.createDevice(this.createDeviceForm.value.name).subscribe({
            next: () => {
                this.router.navigate(['/devices']);
            },
            error: (error) => {
                console.error(error);
            }
        });
    }
}
