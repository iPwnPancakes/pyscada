import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { DeviceEndpoints } from './device-endpoints';
import { TagConfigEndpoints } from './tag-config-endpoints';

@Injectable({
    providedIn: 'root'
})
export class ScadaApiService {
    private readonly baseUrl = environment.SCADA_API_URL;

    public DEVICES: DeviceEndpoints;
    public TAG_CONFIG: TagConfigEndpoints;

    constructor(private http: HttpClient) {
        this.DEVICES = new DeviceEndpoints(http, this.baseUrl);
        this.TAG_CONFIG = new TagConfigEndpoints(http, this.baseUrl);
    }
}
