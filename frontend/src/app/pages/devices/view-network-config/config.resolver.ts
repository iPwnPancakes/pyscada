import { ResolveFn } from '@angular/router';
import { IMqttConfig } from '../../../lib/ScadaApi/models/IMqttConfig';
import { IModbusConfig } from '../../../lib/ScadaApi/models/IModbusConfig';
import { inject } from '@angular/core';
import { ScadaApiService } from '../../../lib/ScadaApi/scada-api.service';
import { throwError } from 'rxjs';

export const configResolver: ResolveFn<IMqttConfig | IModbusConfig> = (route, state) => {
    let configId = route.paramMap.get('config_id');

    if (!configId) {
        return throwError(() => new Error('Invalid route parameters'));
    }

    return inject(ScadaApiService).TAG_CONFIG.get(configId);
};
