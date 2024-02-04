import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IMqttConfig } from './models/IMqttConfig';
import { IModbusConfig } from './models/IModbusConfig';

export class TagConfigEndpoints {
    constructor(private readonly http: HttpClient, private readonly baseUrl: string) {}

    public get(config_id: number | string): Observable<IMqttConfig | IModbusConfig> {
        const url = `${ this.baseUrl }/configs/${ config_id }`;

        return this.http.get<IMqttConfig | IModbusConfig>(url);
    }
}
