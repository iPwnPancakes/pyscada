import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IDevice } from './IDevice';

export class DeviceEndpoints {
    constructor(private readonly http: HttpClient, private readonly baseUrl: string) {}

    public create(name: string): Observable<void> {
        return this.http.post<void>(`${ this.baseUrl }/devices`, { name });
    }

    public all(): Observable<IDevice[]> {
        return this.http.get<IDevice[]>(`${ this.baseUrl }/devices`);
    }
}
