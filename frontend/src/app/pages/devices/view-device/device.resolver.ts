import { mapToResolve, ResolveFn, Router } from '@angular/router';
import { inject } from '@angular/core';
import { ScadaApiService } from '../../../lib/ScadaApi/scada-api.service';
import { Observable, throwError } from 'rxjs';
import { IDevice } from '../../../lib/ScadaApi/models/IDevice';

export const deviceResolver: ResolveFn<IDevice> = (route) => {
    const id = route.paramMap.get('id');
    if (!id) {
        return throwError(() => 'No device ID provided');
    }

    return inject(ScadaApiService).DEVICES.get(id);
};
