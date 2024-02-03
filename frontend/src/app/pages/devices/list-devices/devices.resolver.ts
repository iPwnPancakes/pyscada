import { ResolveFn } from '@angular/router';
import { ScadaApiService } from '../../../lib/ScadaApi/scada-api.service';
import { inject } from '@angular/core';
import { Observable } from 'rxjs';
import { IDevice } from '../../../lib/ScadaApi/models/IDevice';

export const devicesResolver: ResolveFn<Observable<IDevice[]>> = () => {
    return inject(ScadaApiService).DEVICES.all();
};
