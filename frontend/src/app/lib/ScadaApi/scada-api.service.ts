import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';

@Injectable({
    providedIn: 'root'
})
export class ScadaApiService {
    private readonly baseUrl = environment.SCADA_API_URL;

    constructor(private http: HttpClient) {
    }

    public createDevice(name: string): Observable<Object> {
        return this.http.post(`${ this.baseUrl }/devices`, { name });
    }
}
