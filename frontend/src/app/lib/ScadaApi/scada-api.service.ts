import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { IDevice } from './IDevice';

@Injectable({
    providedIn: 'root'
})
export class ScadaApiService {
    private readonly baseUrl = environment.SCADA_API_URL;

    constructor(private http: HttpClient) {
    }

    public createDevice(name: string): Observable<void> {
        return this.http.post<void>(`${ this.baseUrl }/devices`, { name });
    }

    public getDevices(): Observable<IDevice[]> {
        return this.http.get<IDevice[]>(`${ this.baseUrl }/devices`);
    }
}
